# Module 103 — Cross-Site Scripting (XSS)

## Stored XSS
## Approach
Answer obtained via a `Set-Cookie` header in the response — no injection needed for this particular section's answer-capture step.

## Reflected XSS
## Approach
Answer obtained via `Set-Cookie` on `index.php?task=test`.

## DOM XSS
## Approach
Sink used `eval(atob(atob(...)))` — a **double base64-decode** before `eval`. Crafted payload double-base64-encoded so it survives both decode layers before executing, revealing the answer.

## XSS Discovery
Found a reflected XSS injection point in the `email` field of a registration form.
