# Module 143 — Active Directory Enumeration & Attacks
## Target-based sections (58.33% reached)

**Completed:** Initial Enumeration, LLMNR/NBT-NS Poisoning (Linux & Windows variants), Password Spraying, most of Credentialed Enumeration (Linux & Windows).

**Credentials recovered along the way:**
Several sets of domain/service-account credentials were captured via LLMNR/NBT-NS poisoning (Responder) and then confirmed/expanded via password spraying against the domain. Specific usernames and passwords are recorded in the HTB Academy section answers directly, not duplicated here — re-run Responder + spraying against the target to reproduce them if needed.

## BLOCKED
Last 2 questions of "Living Off the Land", and everything from "Kerberoasting - from Linux" onward (ACL Enumeration/Abuse Tactics, DCSync, Domain Trust attacks, both Skills Assessments).

**Cause:** VPN-tunneled access to the spawned lab target stopped working (all ports showed filtered) for both this module's target AND a concurrently-running sibling agent's target at the same time — points to an account-level throttle/lab-infra issue during heavy parallel usage, not a fixable client-side/technique problem.

**To finish:** retry this module by itself (not alongside other modules) once you're ready to continue — reach the target via SSH/RDP with credentials recovered per-section as described above.
