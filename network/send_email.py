#!/usr/bin/env python3
"""
    Sending e-mails with Python
    Author: Miguel Rentes
    https://github.com/rentes/python3-code-snippets/blob/master/network/send_email.py
    Python version: 3.7.2
    This simple script expects one argument: a string with the e-mail body text
"""
import smtplib, ssl, sys

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "<place the sender gmail address here>"
receiver_email = "<place the receiver e-mail here>"
password = "<place the sender password here>"
message = """\
Subject: <place the e-mail subject here>

""" + sys.argv[1]

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)