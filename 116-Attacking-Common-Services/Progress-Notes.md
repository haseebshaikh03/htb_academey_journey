# Module 116 — Attacking Common Services
## Progress notes (47.37% reached)

Theory read in full for: Introduction, Protocol-Specific Attacks, FTP, SMB, SQL Databases, RDP, DNS, SMTP.

**SMTP section:** got one stable target (10.129.130.179, ~120min lease) and ran VRFY/RCPT-TO username enumeration probing — the mail server started rate-limiting/filtering after rapid probes, and the lease tore down before the mailbox-content question could be finished.

**RDP section — registry-key question, 3 guesses all rejected:**
- `LocalAccountTokenFilterPolicy`
- `DisableRestrictedAdmin`
- full `HKLM\...` path
None accepted — needs the exact key name/path per the section's own lab, re-check theory text carefully for the precise registry value name expected.

**Blocked (target contention, not a technique issue) — needs a target you hold uncontested:**
- FTP: port/username/flag questions
- SMB: share name / user password / SSH flag
- SQL Databases: `mssqlsvc` password / flag
- DNS: zone-transfer flag
- Skills Assessment (final section): not yet reached

**Cause:** account-wide single-target-slot contention while multiple modules were being worked in parallel — confirmed directly (other modules' target hostnames, e.g. `ACADEMY-FINC-RFI`, `ACADEMY-LPE-NIX02`, kept appearing in this module's target widget instead of this module's own box). Re-run this module alone (not alongside others) to finish it.
