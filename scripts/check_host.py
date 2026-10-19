#!/usr/bin/env python3
"""Public read-only check. No tokens or credentials are required."""
import json
import urllib.error
import urllib.request

BASE = "https://tre2k3.github.io/martin-no-filter-fighters-updates/"
ROUTES = ("health.json", "updates/stable/latest.yml",
          "updates/stable/latest-mac.yml", "content/manifest.json")

for route in ROUTES:
    try:
        request = urllib.request.Request(BASE + route, headers={"User-Agent": "NFF-update-host-healthcheck/1"})
        with urllib.request.urlopen(request, timeout=15) as response:
            body = response.read(1024 * 1024)
            print(route, "HTTP", response.status, "bytes", len(body))
            if route == "health.json":
                print(json.dumps(json.loads(body), indent=2))
    except urllib.error.HTTPError as exc:
        print(route, "HTTP", exc.code,
              "(expected until a real release is published)" if exc.code == 404 else "")
    except Exception as exc:
        print(route, type(exc).__name__, str(exc))
