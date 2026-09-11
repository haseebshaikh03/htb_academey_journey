# Module 110 — Using Web Proxies
## Section 13: ZAP Scanner

## Approach
Run ZAP's automated scanner against the target. Check the scan results/alerts for anything unusual in the page source — in this case a hidden WordPress comment pointing to a debug endpoint vulnerable to OS command injection via a URL parameter (same pattern as Section 4).
