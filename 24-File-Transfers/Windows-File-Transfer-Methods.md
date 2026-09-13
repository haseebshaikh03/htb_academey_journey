# Module 24 — File Transfers
## Section: Windows File Transfer Methods

**Q1 — Approach:** download `flag.txt` from the web root (e.g. via `wget`/`curl`/PowerShell `Invoke-WebRequest`). Answer is the retrieved flag file's content.

**Q2 — upload `upload_win.zip` to the target via RDP, run `hasher` on it, submit hash:**
**BLOCKED (network flakiness in the lab, not a technique problem)** — no GUI was used; this was driven fully via CLI.

**CLI-only workaround built and partially working:**
1. Downloaded the question's attached zip directly from HTB's public CDN link (visible as the "Download File" href on the page, no auth needed) and extracted it in the container — avoids needing the browser or any GUI file-manager at all.
2. Spawned the target, confirmed reachable, then drove `xfreerdp3` non-interactively under `xvfb-run` (headless X virtual framebuffer — no visible window, no human GUI interaction) with:
   - `/drive:linux,/tmp/uw` — redirects a local folder (containing the extracted `upload_win.txt` and a small `run.bat`) as a share visible on the target at `\\tsclient\linux\`.
   - `/shell:'cmd.exe /c \\tsclient\linux\run.bat'` — replaces the RDP session's shell with a batch script that copies the file to the Desktop, runs `hasher` on it, and writes the result back to the same redirected share (`\\tsclient\linux\hasher_out.txt`) — so the hash could be read back from the container filesystem without ever looking at a screen.
3. Confirmed via logs this gets **past authentication and channel setup** every time (`registered [drive] device #1: linux` appears reliably) — the mechanism itself works.

**Where it actually fails:** the RDP TCP session to this specific target (`10.129.x.x`, `ACADEMY-MISC-MS02`) is extremely unstable from this environment — repeatedly:
- Plain `ping`/`nc` connectivity to the target flips between fully reachable and 100% packet loss every 1-2 minutes, independent of anything this session does (confirmed the shared OpenVPN tunnel itself stays up throughout).
- Even when reachable, the RDP session reliably gets through login/channel negotiation and then dies with `BIO_read returned a system error 110: Connection timed out` before the alternate-shell command finishes and writes its output file.

This reproduced across two independently-spawned fresh target instances and roughly a dozen tuned attempts (RemoteApp `/app:` mode, alternate-`/shell:` mode, various timeouts/quoting), so it isn't a one-off. It matches the original note ("RDP session connected but hung indefinitely") — this is lab/VPN-path flakiness for this particular target, likely worsened by multiple concurrent agents sharing the same account's single VPN/target slot.

**If retried:** the exact commands above are reusable and should work as soon as the network path to the target is stable for the ~15-20s needed after login for the batch script to run — worth trying again during a quieter period, or from a direct (non-relayed) client.

**Q2 approach recap for the record (technique, not the literal answer):** upload the given zip via any transfer method to the target, extract it, run the target's `hasher` utility on the extracted file from the command line, submit the printed hash.
