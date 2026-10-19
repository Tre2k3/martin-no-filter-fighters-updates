#!/usr/bin/env python3
"""Stage real electron-builder update YAML for GitHub Pages; never publishes anything.
Usage: python scripts/stage_release_metadata.py --dist desktop/dist --version 13.4.5 --out release-staging --channel stable
Dependencies: pip install pyyaml
Upload the matching signed artifacts to the SAME TAG on GitHub Releases before publishing staged YAML.
"""
import argparse
import base64
import hashlib
import pathlib
import re
import urllib.parse
import yaml

OWNER = 'Tre2k3'
REPO = 'martin-no-filter-fighters-updates'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dist', required=True, type=pathlib.Path)
    ap.add_argument('--version', required=True)
    ap.add_argument('--out', required=True, type=pathlib.Path)
    ap.add_argument('--channel', choices=('stable', 'beta'), default='stable')
    ns = ap.parse_args()
    if not re.fullmatch(r'\\d+\\.\\d+\\.\\d+(?:-[A-Za-z0-9.-]+)?', ns.version):
        ap.error('Supply a semantic version (e.g. 13.4.5)')
    dist = ns.dist.resolve()
    if not dist.is_dir():
        ap.error('dist directory does not exist')
    mapping = [('latest.yml','latest.yml' if ns.channel=='stable' else 'beta.yml'),
               ('latest-mac.yml','latest-mac.yml' if ns.channel=='stable' else 'beta-mac.yml')]
    base = f'https://github.com/{OWNER}/{REPO}/releases/download/v{urllib.parse.quote(ns.version, safe="")}/'
    staged = []
    for src_name,dst_name in mapping:
        src = dist / src_name
        if not src.exists():
            continue
        data = yaml.safe_load(src.read_text(encoding='utf-8'))
        if not isinstance(data, dict) or str(data.get('version')) != ns.version:
            raise SystemExit(f'Invalid version or YAML: {src}')
        files = data.get('files')
        if not isinstance(files,list) or not files:
            raise SystemExit(f'No files array: {src}')
        original_urls = {}
        for item in files:
            if not isinstance(item,dict):
                raise SystemExit(f'Malformed asset: {item}')
            original = item.get('url')
            if not isinstance(original,str) or not original or pathlib.PurePosixPath(original).name != original or original in ('.','..'):
                raise SystemExit(f'Unsafe filename {original!r}')
            artifact = dist / original
            if not artifact.is_file():
                raise SystemExit(f'Missing artifact {artifact}')
            contents = artifact.read_bytes()
            actual_sha = base64.b64encode(hashlib.sha512(contents).digest()).decode('ascii')
            if item.get('sha512') != actual_sha:
                raise SystemExit(f'Invalid SHA-512 {original}')
            if item.get('size') is not None and item['size'] != len(contents):
                raise SystemExit(f'Invalid size {original}')
            url = base + urllib.parse.quote(original,safe='')
            original_urls[original] = url
            item['url'] = url
            if item.get('blockMapUrl'):
                blk = pathlib.PurePosixPath(item['blockMapUrl']).name
                if not (dist/blk).is_file():
                    raise SystemExit(f'Missing blockmap {blk}')
                item['blockMapUrl'] = base + urllib.parse.quote(blk,safe='')
        if isinstance(data.get('path'),str) and data['path'] in original_urls:
            data['path'] = original_urls[data['path']]
        ns.out.mkdir(parents=True, exist_ok=True)
        out = ns.out / dst_name
        out.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8')
        staged.append(out)
    if not staged:
        raise SystemExit('No generated Windows NSIS or macOS update YAML found')
    print('STAGED, NOT PUBLISHED:')
    for p in staged:
        print(p)
    print('Upload and verify signed release assets, run real-device upgrade QA, THEN publish feed metadata.')

if __name__ == '__main__':
    main()
