# Enable the public update website

1. Go to https://github.com/Tre2k3/martin-no-filter-fighters-updates/settings/pages
2. Choose **Deploy from a branch**, then **main** and **/docs**. Save.
3. Visit https://tre2k3.github.io/martin-no-filter-fighters-updates/health.json
4. Confirm the `state` is `configured-awaiting-first-release`.

The empty stable/beta feeds are intentional. Do not upload `latest.yml` until signed installers are tested and approved. The Windows/Mac desktop apps are not self-updating merely because this repository exists.
