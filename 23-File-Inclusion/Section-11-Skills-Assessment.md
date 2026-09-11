# Module 23 — File Inclusion
## Section 11: Skills Assessment

**Recon found 3 endpoints:**
1. `/api/application.php` — unauthenticated file upload, no type validation
2. `/api/image.php?p=` — image-disclosure endpoint, vulnerable to a **non-recursive** `../` filter — bypass with `....//` (double-dot-double-slash)
3. `contact.php` source (read via the LFI above) revealed a genuine `include()` sink: `?region=`, protected by a filter that blocks a single URL-encoding — bypassed with **double URL-encoding**: `%252e%252e%252f` (decodes once to `%2e%2e%2f`, then again to `../`)

**Chain:** upload a PHP payload via `/api/application.php` → include it via the `contact.php?region=` double-encoded traversal → RCE as `www-data` (confirmed `uid=33(www-data)`).

Read the flag file (`flag_09ebca.txt`) via the RCE.

**Answer:** `eedbb78d4800aa45573840ed6bd2d1e3`
