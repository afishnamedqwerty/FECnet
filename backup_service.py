import shutil
import os
import smtplib
from email.message import EmailMessage

def backup_db():
    try:
        # Create a backup of the PostgreSQL database
        shutil.copy('path/to/database/file', 'path/to/backup/file')

        print("Database backup successful.")

    except Exception as e:
        print(f"Backup Error: {e}")

        # Notify admin about the backup failure
        msg = EmailMessage()
        msg.set_content(f"Database backup failed: {e}")
        msg['Subject'] = 'Database Backup Failed'
        msg['From'] = 'admin@example.com'
        msg['To'] = 'admin@example.com'

        server = smtplib.SMTP('smtp.example.com')
        server.send_message(msg)
        server.quit()
