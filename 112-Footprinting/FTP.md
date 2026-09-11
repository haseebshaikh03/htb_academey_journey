# Module 112 — Footprinting
## FTP section

Target: ACADEMY-FOOT-NIX01 (spawned instance).

**Approach — anonymous FTP access:** confirmed anonymous login is allowed using `curl` (EPSV mode) / `ftp` / `smbclient`-style anonymous auth against the target's FTP service. Once connected, listed the FTP root and found a flag file, then downloaded and read it to get the section's flag.

## Approach — FTP banner-format question
Question: "Which version of the FTP server is running on the target system? Submit the entire banner as the answer."
Approach: connect to the FTP port directly (e.g. `nc <target> 21`, or `od -c` on the raw connect output) to capture the exact server banner text byte-for-byte, then submit that literal banner string as the answer. If the grader rejects it, try minor formatting variants (with/without the leading response code, case, "v" prefix) since these questions are sometimes picky about exact formatting — check HTB's discussion thread for this specific question if none of the natural variants are accepted.
