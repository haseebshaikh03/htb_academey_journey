# Module 116 — Attacking Common Services
## Progress notes (52.63% reached, up from 47.37%)

Theory read in full for: Introduction, Protocol-Specific Attacks, FTP, SMB, SQL Databases, RDP, DNS, SMTP.

**Newly completed this pass — Latest Email Service Vulnerabilities (theory, no target needed):**
This is a reading-only theory page (no answer box) covering CVE-2020-7247, the OpenSMTPD "chain-of-command" hole that lets an unauthenticated attacker get RCE by embedding a semicolon-separated system command in the SMTP envelope-sender field of a crafted message. Completed by reading through the section and using the module's own "Mark Complete & Next" control.

**SMTP section:** got one stable target with a limited-time lease and ran VRFY/RCPT-TO username enumeration probing — the mail server started rate-limiting/filtering after rapid probes, and the lease tore down before the mailbox-content question could be finished. Approach: enumerate valid usernames via SMTP VRFY/RCPT TO, then use a discovered mailbox to read the message content the question asks about.

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
- Attacking Common Services - Easy/Medium/Hard (the 3 remaining skills-assessment sections): not yet reached

**Cause:** account-wide single-target-slot contention while multiple modules were being worked in parallel — confirmed directly (other modules' target hostnames kept appearing in this module's target widget instead of this module's own box; and in this pass, clicking "Spawn the target system" repeatedly reverted to the unspawned state / showed "Target spawning" then silently reset). Re-run this module alone (not alongside others) to finish it.
