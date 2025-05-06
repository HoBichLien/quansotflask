from shop import db
from datetime import datetime

class About(db.Model):
    __tablename__="about"
   
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)  # Tên sản phẩm
    desc = db.Column(db.Text, nullable=False)  # Mô tả sản phẩm
    create_at = db.Column(db.DateTime, default=datetime.utcnow)  # Ngày tạo
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)  # Ngày cập nhật
    is_active = db.Column(db.Boolean, default=True)  # Trạng thái hoạt động
    image = db.Column(db.String(150), nullable=False)  # Hình ảnh sản phẩm
    

    def __repr__(self):
        return f'About {self.title}'