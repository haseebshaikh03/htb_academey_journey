# Module 112 — Footprinting
## SMB section (partial — target contention interrupted this)

```
smbclient -L //<target>/ -N
```
Enumerated the target's share listing this way (also cross-checked with `enum4linux`).

**Q2 — name of the accessible share:** found by reading the non-default share name out of the `smbclient -L` / `enum4linux` share listing (ignore the standard `IPC$` and printer-driver shares).

**Blocked:** questions 1, 3, 4, 5, 6 (SMB banner, flag.txt contents, domain name, share comment, full share path) — the target IP flipped to a different module's box mid-section due to account-wide single-target-slot contention with other parallel agents, and stayed offline (`NT_STATUS_IO_TIMEOUT`) afterward. Re-run this module alone to get a stable target and finish these.

## Remaining sections not started (module at 23.81%)
Chapter 3 "Host Based Enumeration" sections 8-21, Chapter 4 "Remote Management Protocols" (2 sections), Chapter 5 "Skills Assessment" (3 sections).
