# Module 143 — Active Directory Enumeration & Attacks
## Target-based sections (58.33% reached)

**Completed:** Initial Enumeration, LLMNR/NBT-NS Poisoning (Linux & Windows variants), Password Spraying, most of Credentialed Enumeration (Linux & Windows).

**Credentials recovered along the way:**
- `backupagent`
- `wley`
- `svc_qualys`
- SQL: `sa` / `ILFREIGHTDB01!`

## BLOCKED
Last 2 questions of "Living Off the Land", and everything from "Kerberoasting - from Linux" onward (ACL Enumeration/Abuse Tactics, DCSync, Domain Trust attacks, both Skills Assessments).

**Cause:** VPN-tunneled access to the spawned lab target stopped working (all ports showed filtered) for both this module's target AND a concurrently-running sibling agent's target at the same time — points to an account-level throttle/lab-infra issue during heavy parallel usage, not a fixable client-side/technique problem.

**To finish:** retry this module by itself (not alongside other modules) once you're ready to continue — target: `ACADEMY-EA-ATTACK01` (10.129.x.x range), reached via SSH/RDP with credentials given per-section on the HTB page.
