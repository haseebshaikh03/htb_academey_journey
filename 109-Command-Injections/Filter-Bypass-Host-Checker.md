# Module 109 — Command Injections
## Filter Bypass section (Host Checker app)

Target app blacklisted: spaces, `;`, `&`, `|`, `/`, and words `find, grep, tail, cat, echo, sed, awk, head`.

## Approach
**Bypass techniques combined:**
- Tab character instead of space
- Newline as command separator (instead of `;`/`&`/`|`)
- `$(rev<<<"word")` to reconstruct a blacklisted word backwards (defeats word-blacklist)
- `${PWD:0:1}` to produce a literal `/` character without typing it

Used the above bypasses to enumerate the filesystem and locate the file whose path was the section's answer.
