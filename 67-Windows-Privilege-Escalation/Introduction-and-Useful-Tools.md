# Module 67 — Windows Privilege Escalation
## Sections: Introduction to Windows Privilege Escalation / Useful Tools

**Context:** Theory-only sections (no lab target / question required). Read in full and
marked complete.

## Approach / key points
1. **Why privesc matters on an engagement:**
   - Proves impact by accessing data a low-priv foothold shouldn't reach.
   - On a domain-joined box, escalating to `NT AUTHORITY\SYSTEM` is often the path to
     dumping cached domain credentials and pivoting into AD attacks.
   - Recovered credentials/service-account secrets support lateral movement even when
     full SYSTEM isn't achievable.
2. **Broad categories of Windows privilege escalation** (map used to structure enumeration):
   - Abusing Windows **group** privileges (e.g. `Backup Operators`, `Server Operators`).
   - Abusing Windows **user** privileges/token rights (`SeImpersonate`, `SeBackup`,
     `SeDebug`, `SeTakeOwnership`, etc.).
   - **OS/kernel** level exploits (unpatched CVEs, missing hotfixes).
   - **Credential theft** (stored creds in files/registry/memory, autologon, credential
     manager, browser stores).
   - Service, registry, and scheduled-task **misconfigurations** (weak ACLs, unquoted
     service paths, `AlwaysInstallElevated`).
   - **DLL hijacking** / insecure file permissions.
3. **Tooling survey (Useful Tools section):**
   - `winPEAS` — broad automated Windows enumeration script, color-coded findings.
   - `Seatbelt` — C# situational-awareness/enumeration tool, good for EDR-aware engagements
     where a compiled binary is preferred over a script.
   - `PowerUp` / `PrivescCheck` — PowerShell-based privesc-vector enumeration.
   - `Watson` / `Sherlock` — check installed patches against known local-privesc exploit
     CVEs (missing-KB detection).
   - `accesschk.exe` (Sysinternals) — enumerate effective ACLs on files, registry keys,
     services, and named pipes; essential when hunting for weak permissions manually.
   - **Manual fallback** (no tooling allowed / heavily monitored EDR box): built-in
     commands only — `whoami /priv`, `whoami /groups`, `systeminfo`, `net user`,
     `net localgroup administrators`, `tasklist /svc`, `netstat -ano`, `schtasks /query`,
     `reg query` against common autorun/credential keys.

No flag or lab question was involved in these two sections — content was theory/tooling
overview only, confirmed by the absence of a "Question" block on either page.
