Enumerate the SMTP service and submit the banner, including its version as the answer.
└──╼ [★]$ telnet $TARGET 25
Trying 10.129.124.142...
Connected to 10.129.124.142.
Escape character is '^]'.
HELO
220 InFreight ESMTP v2.11
501 Syntax: HELO hostname
Answer: InFreight ESMTP v2.11

Enumerate the SMTP service even further and find the username that exists on the system. Submit it as the answer.
Use the footprinting wordlist listed in the resources section.

smtp-user-enum -M VRFY -U footprinting-wordlist.txt -t $TARGET -w 20
Answer: robin
