# Module 24 — File Transfers
## Section: Windows File Transfer Methods

**Q1 — download `flag.txt` from web root (e.g. via `wget`/`curl`/PowerShell `Invoke-WebRequest`):**
**Answer:** `b1a4ca918282fcd96004565521944a3b`

**Q2 — upload `upload_win.zip` to the target via RDP, run `hasher` on it, submit hash:**
**BLOCKED** — this needs an actual interactive RDP GUI session (mstsc.exe) to drag/drop-upload a file and run a GUI tool. Attempted via a Docker→WSL→Windows RDP relay chain; the RDP session connected but hung indefinitely at "Configuring remote session..." — likely target-VM flakiness. Needs a direct (non-relayed) RDP client session to finish — do this one manually from your own Windows desktop.
