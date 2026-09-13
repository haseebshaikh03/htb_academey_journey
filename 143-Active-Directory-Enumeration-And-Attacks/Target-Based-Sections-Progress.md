# Module 143 — Active Directory Enumeration & Attacks
## Target-based sections (58.33% reached)

**Completed:** Initial Enumeration, LLMNR/NBT-NS Poisoning (Linux & Windows variants), Password Spraying, most of Credentialed Enumeration (Linux & Windows).

**Credentials recovered along the way:**
Several sets of domain/service-account credentials were captured via LLMNR/NBT-NS poisoning (Responder) and then confirmed/expanded via password spraying against the domain. Specific usernames and passwords are recorded in the HTB Academy section answers directly, not duplicated here — re-run Responder + spraying against the target to reproduce them if needed.

## BLOCKED
Last 2 questions of "Living Off the Land", and everything from "Kerberoasting - from Linux" onward (ACL Enumeration/Abuse Tactics, DCSync, Domain Trust attacks, both Skills Assessments).

**Cause:** VPN-tunneled access to the spawned lab target stopped working (all ports showed filtered) for both this module's target AND a concurrently-running sibling agent's target at the same time — points to an account-level throttle/lab-infra issue during heavy parallel usage, not a fixable client-side/technique problem.

**To finish:** retry this module by itself (not alongside other modules) once you're ready to continue — reach the target via SSH/RDP with credentials recovered per-section as described above.

## Re-check (this session, 2026-09-12)
Retried spawning the module's target twice more: the widget cycled "Spawn the target system" -> "Target spawning." -> back to "Spawn the target system" without ever producing a usable IP, and one IP that briefly appeared (10.129.201.234) was unreachable (nmap -Pn against 445/3389/135 showed all filtered — the same failure mode documented above). This confirms the account-wide single-target-slot contention is still active; no target-gated question in this module could be attempted this pass.

Full page-level list of the 15 still-incomplete sections (page numbers 16-18, 20-23, 25-26, 28-31, 34-35 of 36): Living Off the Land, Kerberoasting - from Linux, Kerberoasting - from Windows, ACL Enumeration, ACL Abuse Tactics, DCSync, Privileged Access, Bleeding Edge Vulnerabilities, Miscellaneous Misconfigurations, Attacking Domain Trusts - Child->Parent (2 pages), Attacking Domain Trusts - Cross-Forest (2 pages), and both Skills Assessment pages.
