# Windows automatic-upgrade beta test

**Status: Not released. No active beta update manifest.**

This page documents a controlled test from a separate installation named **Martin No Filter Fighters Beta v13.4.4** to **v13.4.5**. It does not change the stable installation or the public release of the game.

Beta Windows app identity: `com.tdhampton.martinnofilterfighters.beta`

Beta feed: `https://tre2k3.github.io/martin-no-filter-fighters-updates/updates/beta/`

Expected metadata path (only AFTER validation): `docs/updates/beta/beta.yml`

Expected GitHub Release tag: `beta-test-13.4.5`

## Before publishing beta.yml
- Build the beta 13.4.4 baseline installer; install and launch it.
- Build 13.4.5, verify installer and .exe.blockmap.
- Make a GitHub **pre-release** with exact tag `beta-test-13.4.5`; upload both.
- Verify the HTTPS installer and blockmap download URLs.
- Stage beta.yml with the checked SHA-512 and size, pointing at those immutable GitHub Release URLs.
- Only after the above, commit the beta.yml file to this repository's `docs/updates/beta/` directory.
- Test in-app Check → Download → Restart/install → 13.4.5 launch, settings retention and offline gameplay.
- Leave `docs/updates/stable/` unchanged.

**Warning:** GitHub prereleases and beta feeds are public on a public repo. Do not publish unsigned beta binaries for general distribution; keep the test constrained and move to authentically code-signed builds before public release.

The current Ed25519 private key on the developer's Windows computer signs *media/content manifests*, not Windows installers. Never upload private keys.

If updating fails, remove the beta manifest (not the stable feed), collect the local logs, and investigate before publishing again.
