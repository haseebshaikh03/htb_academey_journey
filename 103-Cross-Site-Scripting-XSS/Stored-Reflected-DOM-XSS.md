# Module 103 — Cross-Site Scripting (XSS)

## Stored XSS
Flag obtained via a `Set-Cookie` header response — no injection needed for this particular section's flag capture step.

## Reflected XSS
Flag obtained via `Set-Cookie` on `index.php?task=test`.

## DOM XSS
Sink used `eval(atob(atob(...)))` — a **double base64-decode** before `eval`. Crafted payload double-base64-encoded to survive both decode layers and execute.

**Flag:** `HTB{pur3ly_cl13n7_51d3}`

## XSS Discovery
Found a reflected XSS injection point in the `email` field of a registration form.
