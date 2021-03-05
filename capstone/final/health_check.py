#!/usr/bin/env python3

import psutil, shutil, socket, os
from emails import generate_error_email, send_email

def send_error_mail(error_type):
    sender = "automation@example.com"
    recipient = "student-01-7207a75628ea@example.com "
    body = "Please check your system and resolve the issue as soon as possible"
    subject = ""
    if error_type == "cpu":
        subject = "Error - CPU usage is over 80%"
    elif error_type == "disk":
        subject = "Error - Available disk space is less than 20%"
    elif error_type == "memory":
        subject = "Error - Available memory is less than 500MB"
    elif error_type == "localhost":
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    
    email = generate_error_email(sender, recipient, subject, body)
    send_email(email)

def run():
    # Check CPU usage percent
    cpu_usage_percent = psutil.cpu_percent(interval=1)
    if cpu_usage_percent > 80:
        send_error_mail("cpu")

    # Check available disk percent
    available_disk = shutil.disk_usage("/")
    available_disk_percent = available_disk[2] * 100.0 / available_disk[0] 
    if available_disk_percent < 20:
        send_error_mail("disk")

    # Check available memory
    available_memory = psutil.virtual_memory().available
    mb_500 = 500 * 1024 * 1024
    if available_memory < mb_500:
        send_error_mail("memory")

    # Check resolving localhost
    localhost_resolved = socket.gethostbyname("localhost")
    if localhost_resolved != "127.0.0.1":
        send_error_mail("localhost")

run()
