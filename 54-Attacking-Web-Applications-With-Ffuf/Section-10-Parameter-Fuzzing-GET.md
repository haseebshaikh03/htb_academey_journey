# Module 54 — Attacking Web Applications With Ffuf
## Section 10: Parameter Fuzzing (GET)

`ffuf -w <param-names-list> -u "http://target/page.php?FUZZ=test"` — filter out the baseline "no such param" response size to find the real one.

## Approach
GET parameter name discovered by fuzzing candidate parameter names against the target page and filtering out the baseline "unrecognized parameter" response size to isolate the one accepted by the application.
