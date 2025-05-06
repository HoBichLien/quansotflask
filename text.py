import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "comtambichlien@gmail.com"
EMAIL_PASSWORD = "guqt wldr oabk vcrl"
TO_EMAIL = "emailnguoinhan@gmail.com"  # Thay bằng email cần nhận

# Tạo nội dung email
msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg["Subject"] = "Test Email từ Python"
body = "Xin chào, đây là email test gửi từ Python!"
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    server.quit()
    print("✅ Gửi email thành công!")
except Exception as e:
    print(f"❌ Lỗi khi gửi email: {e}")
