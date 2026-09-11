# Module 23 — File Inclusion
## Section 10: Prevention

SSH'd into the hardening box (htb-student). Located `php.ini`, appended `system` to the existing `disable_functions` list (careful to append, not overwrite the list — an initial destructive `sed` replace was blocked by a safety check as "weakening security" and had to be redone as an append).

Triggered `system()` from PHP CLI (`php -c <path> -r 'system("id");'`) to produce and read the exact "Call to undefined function" style error string from `error.log`, which was the section's answer.
