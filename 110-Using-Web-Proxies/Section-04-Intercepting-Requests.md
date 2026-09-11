# Module 110 — Using Web Proxies
## Section 4: Intercepting Requests

Target has a "ping" utility page with an `ip` parameter.

## Approach
Intercept the request in your proxy, modify the `ip` parameter to chain an OS command via `;` (e.g. append `;cat flag.txt;`), forward it, and read the command output in the response.
