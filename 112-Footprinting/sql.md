MySQL
MySQL is an open-source SQL relational database management system developed and supported by Oracle.
A database is simply a structured collection of data organized for easy use and retrieval.

Lab: MySQL
Enumerate the MySQL server and determine the version in use. (Format: MySQL X.X.XX)

└──╼ [★]$ sudo nmap $TARGET -sV -sC -p3306 --script mysql*

Answer: MySQL 8.0.27


During our penetration test, we found weak credentials "robin:robin". We should try these against the MySQL server. What is the email address of the customer "Otto Lang"?
Log in and enumerate the database.

└──╼ [★]$ mysql -u robin -probin -h $TARGET --skip-ssl

Answer: ultrices@google.htb
