# Module 54 — Attacking Web Applications With Ffuf
## Section 12: Value Fuzzing

## Approach
Once the parameter name (from Section 10) was known, fuzzed its **value** (e.g. numeric IDs / usernames) with ffuf to find the value that returns the flag.

Flag found by fuzzing the values of the previously-discovered parameter until a response containing it was returned.
