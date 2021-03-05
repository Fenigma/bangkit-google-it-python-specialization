#!/usr/bin/env python3

import datetime
import os

from reports import generate_report
from emails import send_email, generate_email

if __name__ == "__main__":
    # create PDF report
    OUTFILE = "/tmp/processed.pdf"
    date = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on " + date

    paragraph = []
    paragraph_text_dir = "/home/student-01-7207a75628ea/supplier-data/descriptions"
    files = os.listdir(paragraph_text_dir)
    for fname in files:
        with open(os.path.join(paragraph_text_dir, fname)) as f:
            content = f.read().strip().split("\n")
            content = "name: " + content[0] + "<br/>" + "weight: " + content[1]
            paragraph.append(content) 

    generate_report(OUTFILE, title, paragraph)

    # create and send email
    sender = "automation@example.com"
    recipient = "student-01-7207a75628ea@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = OUTFILE

    email = generate_email(sender, recipient, subject, body, attachment_path)
    send_email(email)