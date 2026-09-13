# Module 147 — Password Attacks
## BLOCKED: remaining ~13 sections (46.15% reached)

All of the following need a spawned lab target, and the account's single global target
slot is under heavy, confirmed contention this session — see "Contention evidence" below.

### Sections still needed
- **Remote Password Attacks → Network Services** (see recon below, in progress)
- Remote Password Attacks → Spraying, Stuffing, and Defaults
- Extracting Passwords from Windows Systems (5 of 6 sections)
- Extracting Passwords from Linux Systems (1 of 2 sections)
- Extracting Passwords from the Network (1 of 2 sections)
- Windows Lateral Movement Techniques (4 sections)
- Skills Assessment (1 section)

### Network Services — recon done this session
- Target for this section: `ACADEMY-PWATTACKS-WINSRV` (Windows). Open ports confirmed via `nmap -Pn -p22,135,139,445,3389,5985,5986,3306,21`: **22 (SSH), 135 (msrpc), 139/445 (SMB), 3389 (RDP), 5985 (WinRM)**. 21/3306/5986 closed.
- Question 1 provides a **"Download File"** link on the section page → a zip containing `username.list` (104 entries) and `password.list` (203 entries) — this is the wordlist to brute the WinRM login with. Fetch it via the link shown under the section's first question (button labelled "Download File"), unzip, and use both lists.
- Goal: "Find the user for the WinRM service and crack their password. Then log in and find a flag file."
- **Tooling note:** `netexec`/`crackmapexec` are NOT installed in the shared `htb` container, and `pip install netexec` fails (no matching package in this environment's index — likely proxy-restricted). `hydra` and `medusa` ARE installed but **hydra has no native `winrm` module**. `hydra ... smb` works but is very slow (SMB forces `-t 1`, and 104×203 = 21112 combinations ran for 45+s with zero hits before the target was lost to contention).
- **Recommended approach for next attempt:** don't brute the full cartesian product blindly.
  1. Use `rpcclient -U '' -N <target> -c 'enumdomusers'` or `smbclient -N -L //<target>/` for a null-session user enumeration first, to narrow down which of the 104 usernames are real domain accounts (SMB null sessions are often allowed on these intentionally-weak academy boxes).
  2. Once narrowed to a handful of real usernames, either password-spray those specifically against SMB with `hydra -L narrowed_users.txt -P password.list -t 1 -f <target> smb` (much faster), or write a small python3 script using `requests`+`requests-ntlm`/`pywinrm` (check if installed) to test Basic/NTLM auth directly against `http://<target>:5985/wsman`, since that's the literal target service asked about.
  3. Log in via WinRM once creds are found (`evil-winrm` not installed either — check `gem install evil-winrm` or use a raw `pywinrm` python script to run `dir`/`type` and find the flag file).

### Contention evidence (why nothing got submitted this session)
Confirmed directly, twice, independently:
- Spawned a target for Module 103's Session Hijacking section (`10.129.187.139`), made progress on the exercise, and ~90 seconds later the module's Target(s) panel silently switched to a completely different, unrelated box (`10.129.172.255` / `ACADEMY-MISC-MS02`) — not something this session spawned.
- Spawned `ACADEMY-PWATTACKS-WINSRV` for this module's Network Services section, started a hydra SMB brute-force, and within ~45 seconds the target became unreachable (`NT_STATUS_HOST_UNREACHABLE` / connection timeouts), and the module page's Target(s) panel then showed **`ACADEMY-MISC-MS02`** again — again a different, unrelated box.
- This means the account's "one target at a time" limit is enforced **globally across the whole account**, not per-module-tab, and other concurrently-running agent sessions are actively spawning/stealing it every 1-2 minutes. Any section needing more than ~60-90 uninterrupted seconds of target access (which is all of the remaining ones) is not currently reliable to finish.

**To finish:** re-run these ONE AT A TIME once other agents' modules are done (or coordinate a time window), using the narrowed-enumeration approach above for Network Services rather than a blind full-wordlist brute force, since that alone should already fit inside a short contention-free window.
