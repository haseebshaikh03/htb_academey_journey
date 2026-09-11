# Module 110 — Using Web Proxies
## Section 13: ZAP Scanner

Ran ZAP's automated scanner against the target. It found a hidden WordPress comment in the page source linking to a debug endpoint:

`/devtools/ping.php?ip=`

This endpoint is vulnerable to OS command injection via the `ip` parameter (same style as Section 4).

**Flag:** `HTB{5c4nn3r5_f1nd_vuln5_w3_m155}`
