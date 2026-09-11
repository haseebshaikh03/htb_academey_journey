# Module 58 — SQLMap Essentials
## Section 9: Bypassing Web Application Protections (4 cases)

- **User-Agent-based WAF block:** fixed by setting a normal browser `--user-agent`/`--random-agent` flag in sqlmap.
- **Single-use nonce protection:** handled with sqlmap's `--eval` flag to compute/refresh the nonce per-request from a Python snippet.
- **CSRF-token protection:** handled with `--csrf-token=<token-param-name>` (sqlmap fetches & resubmits the token automatically per request).
- **Final case (case8):** UNION-based approach was fragile here; switching to `--technique=B` (boolean-blind) instead was the fix.

**Flag (case8):** `HTB{y0u_h4v3_b33n_c5rf_70k3n1z3d}`
