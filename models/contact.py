from shop import db
from datetime import datetime
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default="Chưa xử lý")  # Trạng thái xử lý của admin
    admin_reply = db.Column(db.Text, nullable=True)  # Phản hồi của admin
    create_at=db.Column(db.DateTime,default=datetime.utcnow)
