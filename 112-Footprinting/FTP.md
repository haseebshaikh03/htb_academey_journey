# Module 112 — Footprinting
## FTP section

Target IP: 10.129.202.5 (ACADEMY-FOOT-NIX01, spawned)

**Anonymous FTP access confirmed** via `curl` (EPSV mode). Found `flag.txt` in FTP root, retrieved it:

**Flag:** `HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}`

## BLOCKED — FTP banner-format question
Question: "Which version of the FTP server is running on the target system? Submit the entire banner as the answer."
Live banner confirmed byte-exact (via `od -c` across multiple reconnects): `220 InFreight FTP v1.1`

Tried and all **rejected**:
- `220 InFreight FTP v1.1`
- `InFreight FTP v1.1`
- `InFreight FTP 1.1`
- `220 infreight ftp v1.1` (lowercase)
- `220 InFreight FTP 1.1` (no "v")
- `InFreight FTP`

This looks like a genuine grader quirk, not a wrong-banner problem — the raw banner itself is confirmed correct. Check HTB's discussion thread for this exact question for the expected format.
