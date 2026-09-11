# Module 110 — Using Web Proxies
## Section 8: Encoding/Decoding

## Approach
Download the section's attached file. Its content is encoded in layers — decode with Burp's Decoder (or manually):
1. Base64-decode repeatedly (multiple passes)
2. URL-decode once at the end
Peel one layer at a time and check if the result still looks encoded before applying the next decode.
