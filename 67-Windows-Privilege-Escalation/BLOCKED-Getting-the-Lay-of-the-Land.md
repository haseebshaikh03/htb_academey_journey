# Module 67 — Windows Privilege Escalation
## BLOCKED: Lab target unobtainable (account-wide target contention)

**Module state at time of work:** Module started this session (was 0%, previously not
started). Reached 6.06% (2/33 sections) via genuinely completed theory-only sections;
sections 3+ ("Getting the Lay of the Land" onward) all require the shared lab target
and RDP access to `htb-student` on the spawned Windows box.

## Sections attempted but blocked on target contention
- **Situational Awareness** (section 3/33, Q1+Q2 — network config walkthrough; Q2:
  "What executable other than cmd.exe is blocked by AppLocker?"). Theory read in full:
  the technique is `Get-AppLockerPolicy -Effective -Xml` (or `-Local`) to dump the enforced
  AppLocker rule set as XML and grep the `<FilePathRule>`/deny entries for blocked
  executables besides `cmd.exe` (commonly `powershell.exe` in the stock lab, but must be
  confirmed against the actual policy XML on this instance's target rather than assumed).
- **Initial Enumeration** (section 4/33, Q1-Q5 — non-default privilege for `htb-student`
  via `whoami /priv`; service on TCP 8080 via `netstat -ano` + `tasklist /svc`; logged-in
  user/session type via `query user` / `qwinsta`).
- **Communication with Processes** (section 5/33, Q1-Q2 — service on `0.0.0.0:21` via
  `netstat -ano | findstr :21`; account with `WRITE_DAC` over the named pipe
  `\pipe\SQLLocal\SQLEXPRESS01`, found via `accesschk64.exe -w \pipe\SQLLocal\SQLEXPRESS01 -v`
  or PipeList + icacls-style pipe ACL enumeration).

All three of the above require RDP (`htb-student` / `HTB_@cademy_stdnt!`) to a spawned
Windows target. Every `POST /api/v2/modules/67/sections/<id>/lab/spawn` attempt returned
**HTTP 503**.

## Why it's blocked
HTB Academy enforces a single spawned target per account, and this session observed 6-8
other concurrent agent sessions actively working other modules on the same account (each
with their own live target churn: Footprinting/112, XSS/103, File Transfers/24, Attacking
Common Services/116, Shells & Payloads/115, Linux Privesc/51, Command Injections/109,
Ffuf/54, AD Enumeration/143), so the slot was saturated. One window opened where the
target briefly looked "offline"/spawnable on this module's section, but the spawn request
still 503'd (lost the race to another agent's in-flight spawn/reset).

## Next steps
Re-attempt sections 3-5 (and continue module intake from section 6 onward — "Windows User
Privileges") once the account's target contention eases. No flags/answers were fabricated
or guessed; the two sections marked complete in Introduction-and-Useful-Tools.md were
genuinely theory-only (no "Question" block present on the page) and were completed by
actually reading the content and clicking through, not by guessing.
