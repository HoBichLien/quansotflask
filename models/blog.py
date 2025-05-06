from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from shop import db

class Blog(db.Model):
    __tablename__="blogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)  # Tên sản phẩm
    designer = db.Column(db.String(255), nullable=False)  # Tên người thiết kế
    create_at = db.Column(db.DateTime, default=datetime.utcnow)  # Ngày thiết kế
    image = db.Column(db.String(512), nullable=True)  # Link hình ảnh sản phẩm
    status = db.Column(db.String(255), default="Chưa duyệt mẫu")  # Trạng thái sản xuất
    desc = db.Column(db.Text, nullable=False)  # Mô tả sản phẩm

    def __repr__(self):
        return f"<Blog {self.name}>"