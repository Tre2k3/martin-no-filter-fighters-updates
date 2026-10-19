# Windows automatic-upgrade beta test

**Status: Beta 13.4.5 prerelease and beta.yml published; installed-game upgrade remains unverified.**

This is an isolated test from `Martin No Filter Fighters Beta` 13.4.4 to 13.4.5. The stable feed is untouched.

- Beta app identity: `com.tdhampton.martinnofilterfighters.beta`
- Beta update feed: https://tre2k3.github.io/martin-no-filter-fighters-updates/updates/beta/
- Published manifest: https://tre2k3.github.io/martin-no-filter-fighters-updates/updates/beta/beta.yml
- Published test release: https://github.com/Tre2k3/martin-no-filter-fighters-updates/releases/tag/beta-test-13.4.5

## Test now

1. Ensure 13.4.4 Beta, NOT 13.4.5, is installed.
2. Open Beta, choose Game Updates → Check app (mouse or controller).
3. Confirm the app detects 13.4.5 and prompts to download.
4. Download the update, allow it to verify, and choose Restart & Install at a safe menu.
5. Relaunch and confirm 13.4.5 installed with game settings intact and gameplay available offline.
6. If it fails, capture a screenshot of the friendly status and collect local diagnostic logs; do not paste private keys or other secrets.

**Important:** The release assets are unsigned Windows binaries and publicly accessible; not suitable for broad player distribution. The on-disk release installer must match the manifest SHA-512 or the updater will reject it. Do not promote this to stable until a signed Windows installer and full upgrade/regression tests are complete.

The private Ed25519 signing key signs media packs, NOT Windows installers. Keep private keys outside this repository.
