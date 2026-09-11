# Module 147 — Password Attacks
## BLOCKED: remaining ~14 sections (46.15% reached)

All of the following need a spawned lab target, and hit the account's single-target-slot contention (running many parallel agents each spawning their own target caused constant evictions):

- Network Services (hydra/netexec brute force across SSH/SMB/RDP/WinRM) — got as far as cracking `dennis : rockstar` for SSH before losing the target
- Password Spraying / Credential Stuffing / Default Credentials
- Attacking SAM/SYSTEM/SECURITY hives
- Attacking LSASS
- Attacking Windows Credential Manager
- Attacking AD / NTDS.dit
- Credential Hunting in Windows
- Credential Hunting in Linux (the target-based part)
- Credential Hunting in Network Shares
- Pass the Hash / Pass the Ticket / Pass the Certificate
- Final Skills Assessment

**To finish:** re-run these ONE AT A TIME (not in parallel with other modules) so the single HTB lab-target slot isn't fought over. Each section's theory (already partially read) tells you the exact tool/technique needed — this is a "keep retrying with a target you actually hold" problem, not a technique problem.
