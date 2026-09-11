# Module 112 — Footprinting
## SMB section (partial — target contention interrupted this)

```
smbclient -L //<target>/ -N
```
Share listing found: `print$` (Printer Drivers), `sambashare`, `IPC$`.

**Q2 answer — name of the accessible share:** `sambashare`

**Blocked:** questions 1, 3, 4, 5, 6 (SMB banner, flag.txt contents, domain name, share comment, full share path) — the target IP flipped to a different module's box (10.129.192.87, ACADEMY-MSF2-WIN01) mid-section due to account-wide single-target-slot contention with other parallel agents, and stayed offline (`NT_STATUS_IO_TIMEOUT`) afterward. Re-run this module alone to get a stable target and finish these.

## Remaining sections not started (module at 23.81%)
Chapter 3 "Host Based Enumeration" sections 8-21, Chapter 4 "Remote Management Protocols" (2 sections), Chapter 5 "Skills Assessment" (3 sections).
