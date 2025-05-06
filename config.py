import os
import string
import random


class Config:
    SECRET_KEY=os.urandom(24) # khóa bảo mật dùng để bảo vệ session và form
    SQLALCHEMY_DATABASE_URI="mysql://root@localhost/quansort"
    SQLALCHEMY_TRACK_MODIFICATIONS=False #vô hiệu hóa theo dõi sự thay đổi SQLALCHEMY


class EmailConfig:
    MAIL_SERVER = 'smtp.gmail.com'#nếu mua bên pavietnam thì hỏi server là gì để thay vô
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = '' # Thay bằng email của bạn
    MAIL_PASSWORD = '' # Thay bằng mật khẩu đã xác thực
    MAIL_DEFAULT_SENDER=("BICHLIEN","comtambichlien@gmail.com")

def Tao_mat_khau(length=8):
    kytu=string.ascii_letters+string.digits
    return "".join(random.choice(kytu) for i in range(length))

# cấu hình gogoole
class ConfigGoogle:
    SECRET_KEY = os.urandom(24)#tạo ngẫu nhiên key : chuỗi ngẫu nhiên
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/flaskdev'
    GOOGLE_CLIENT_ID = ''
    GOOGLE_CLIENT_SECRET = ''
    GOOGLE_ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
    GOOGLE_AUTHORIZE_URL = 'https://accounts.google.com/o/oauth2/auth'
    GOOGLE_USERINFO_ENDPOINT = 'https://www.googleapis.com/oauth2/v3/userinfo'
    OAUTHLIB_INSECURE_TRANSPORT = True  # Only for development