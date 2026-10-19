# Martin: No Filter Fighters — Dedicated Update Hosting

**Status: Hosting repository prepared. No automatic desktop updates are live yet.**

This public repository stores SMALL desktop release manifests. Actual Windows and Mac installers will be published as GitHub Release assets, only AFTER code signing, testing, and owner approval. This is **not** the private game source repository.

## Planned public endpoints

- Status: https://tre2k3.github.io/martin-no-filter-fighters-updates/health.json
- Stable app feed: https://tre2k3.github.io/martin-no-filter-fighters-updates/updates/stable/
- Beta app feed: https://tre2k3.github.io/martin-no-filter-fighters-updates/updates/beta/
- Content manifest (not published): https://tre2k3.github.io/martin-no-filter-fighters-updates/content/manifest.json
- Desktop installers: https://github.com/Tre2k3/martin-no-filter-fighters-updates/releases

## GitHub Pages activation — required one-time owner action

1. Open https://github.com/Tre2k3/martin-no-filter-fighters-updates/settings/pages
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Select branch `main` and folder `/docs`, then **Save**.
4. Wait for deployment; open the status endpoint above and confirm it returns JSON.
5. The absence of `latest.yml` is intentional until a real installer release exists.

## Configure the game publisher (once, locally)

Use the updater-enabled v13.4.4 **SOURCE**, not an old portable EXE. After Pages is live, run `scripts/configure_game_publisher.ps1` in this repository on your Windows PC, pointing `-GameSourceRoot` at your extracted game source folder. This invokes the game's local publisher setup and generates private Ed25519 signing credentials under your home folder. **Never upload private keys**.

For Windows automatic application updates, build an Electron **NSIS installer**, sign it using an authentic publisher certificate, publish the installer and blockmap assets to a versioned GitHub Release, and only after successful install-to-next-version testing publish `latest.yml` into `docs/updates/stable/`.

For macOS, build on macOS, code-sign and notarize the app, publish a signed ZIP for updating plus a DMG for installation, then publish `latest-mac.yml` after macOS upgrade testing.

`scripts/stage_release_metadata.py` rewrites generated update YAML to immutable GitHub Releases URLs and verifies file size and SHA-512. The script stages local files; it does **not** publish anything.

For art/audio packs, the game requires an Ed25519 signed manifest, safe file types and validated hashes. GitHub Pages is NOT a suitable high-bandwidth content CDN for a viral game; use separately configured object storage for large packs.

### Release checklist

1. Build new version from vetted source, preserving app identifiers and saves.
2. Run automated tests and independent gameplay regression checks.
3. Build and sign platform-specific installers; verify locally.
4. Upload exact release artifacts, verify direct download links and file checksums.
5. Install old version, upgrade to new on real Windows/macOS systems; check offline, failure, restart, and saved progress.
6. Publish stable YAML feed LAST. This makes the update visible to installed players.

**Never commit:** signing keys, certificates, access tokens, unreleased game assets, or large binaries. Publishing a feed announces an update to real players.

Existing portable ZIP installations require a one-time installer transition; a GitHub repository alone cannot update them.
