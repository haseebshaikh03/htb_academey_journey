Lab: IMAP/POP3

Q1: Figure out the exact organization name from the IMAP/POP3 service and submit it as the answer.
Answer: InlaneFreight Ltd

Q2: What is the FQDN that the IMAP and POP3 servers are assigned to?
Answer: dev.inlanefreight.htb

Q3: Enumerate the IMAP service and submit the flag as the answer. (Format: HTB{...})
Use OpenSSL to enumerate the IMAP service.

└──╼ [★]$ openssl s_client -connect $TARGET:imaps
Connecting to 10.129.42.195
Answer: HTB{roncfbw7iszerd7shni7jr2343zhrj}

Q4: What is the customized version of the POP3 server?
Use OpenSSL to enumerate the POP3 server.

+OK InFreight POP3 v9.188
Answer: InFreight POP3 v9.188

Q5: What is the admin email address?
Log in to the IMAP server using the credentials robin:robin. Then enumerate the shown inboxes and their mail.

1 login robin robin

// View all mailboxes
1 list "" *
* LIST (\Noselect \HasChildren) "." DEV
* LIST (\Noselect \HasChildren) "." DEV.DEPARTMENT
* LIST (\HasNoChildren) "." DEV.DEPARTMENT.INT
* LIST (\HasNoChildren) "." INBOX
1 OK List completed (0.007 + 0.000 + 0.006 secs).

// View the DEV.DEPARTMENT.INT mailbox
2 select "DEV.DEPARTMENT.INT"
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 1 EXISTS // 1 email exists
* 0 RECENT
* OK [UIDVALIDITY 1636414279] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
2 OK [READ-WRITE] Select completed (0.005 + 0.000 + 0.004 secs).

// View the email headers
3 fetch 1 all
* 1 FETCH (FLAGS (\Seen) INTERNALDATE "08-Nov-2021 23:51:24 +0000" RFC822.SIZE 167 ENVELOPE ("Wed, 03 Nov 2021 16:13:27 +0200" "Flag" (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("CTO" NIL "devadmin" "inlanefreight.htb")) (("Robin" NIL "robin" "inlanefreight.htb")) NIL NIL NIL NIL))

Answer: devadmin@inlanefreight.htb

Q6: Try to access the emails on the IMAP server and submit the flag as the answer. (Format: HTB{...})
Continue enumerating the email in the inbox to get the flag.

3 fetch 1 body[text]
* 1 FETCH (BODY[TEXT] {34}
HTB{983uzn8jmfgpd8jmof8c34n7zio}
)
3 OK Fetch completed (0.001 + 0.000 secs).
Answer: HTB{983uzn8jmfgpd8jmof8c34n7zio}
