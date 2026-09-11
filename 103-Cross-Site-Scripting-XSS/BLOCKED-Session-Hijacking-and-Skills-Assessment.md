# Module 103 — Cross-Site Scripting (XSS)
## BLOCKED sections: Session Hijacking + Skills Assessment (blind XSS)

### Session Hijacking (`/hijacking/index.php`)
Tried 5 payload variants across `fullname`/`username`/`imgurl` fields (external `<script src>`, inline `fetch`, `onerror` breakout). No callback ever hit the log server after 20+ cumulative minutes waiting. No admin-trigger endpoint discoverable (`admin.php`, `bot.php` etc. all 404).

### Skills Assessment — WordPress 5.7.2 "Security Blog" (`/assessment/`)
Hint: "You can't see me, but i can see you!" → confirms blind-XSS intent.
Comment form fields: `author`, `email`, `url`, `comment` (POSTs to `wp-comments-post.php`).
Tried 8 distinct payload placements/styles (script in comment body, external script-src in author, attribute breakout in url, combined img-onerror+script). Nothing ever fired, and the "Recent Comments" widget never showed the submitted comments — meaning either:
(a) no admin-bot is actually visiting/reviewing comments on this target instance, or
(b) WordPress's default `kses` filter is stripping script/event-handler content from comments before storage (can't verify from outside as an anonymous poster since pending comments aren't visible).

**Recommendation:** revisit with a longer wait time after each submission, or check whether the "admin bot" needs to be manually triggered from a button on the HTB Academy page itself (some blind-XSS labs require clicking a "Notify Admin" button rather than relying on a periodic bot).
