from shop import db
from datetime import datetime

class Product(db.Model):
    __tablename__="products"
   
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)  # Tên sản phẩm
    color = db.Column(db.String(150), nullable=False)  # Màu sắc
    chatlieu = db.Column(db.String(250), nullable=False)  # Chất liệu
    price = db.Column(db.Float, nullable=False)  # Giá bán
    desc = db.Column(db.Text, nullable=False)  # Mô tả sản phẩm
    create_at = db.Column(db.DateTime, default=datetime.utcnow)  # Ngày tạo
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)  # Ngày cập nhật
    tonkho = db.Column(db.Integer, nullable=False)  # Tồn kho
    is_active = db.Column(db.Boolean, default=True)  # Trạng thái hoạt động
    image = db.Column(db.String(150), nullable=False)  # Hình ảnh sản phẩm
    
    # Trường để lọc size theo cân nặng, chiều cao
    cannang = db.Column(db.Float, nullable=True)  # Cân nặng (kg)
    chieucao = db.Column(db.Float, nullable=True)  # Chiều cao (cm)
    size_type = db.Column(db.String(50), nullable=True)  # Loại size (S, M, L, XL, XXL...)

    # Thông tin kích thước chi tiết
    kichthuoc = db.Column(db.Float, nullable=True)  # Kích thước số
    
    #  Danh mục sản phẩm
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    category = db.relationship("Category", backref='products')

    def __repr__(self):
        return f'<Product {self.name} - {self.size_type}>'
    

    #order detail

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Thêm các trường mới
    shipping_fee = db.Column(db.Float, default=0)
    discount = db.Column(db.Float, default=0)
    payment_method = db.Column(db.String(50))
    status = db.Column(db.String(50), default='Chờ xác nhận')
    shipping_name = db.Column(db.String(100))
    shipping_phone = db.Column(db.String(20))
    shipping_address = db.Column(db.String(255))
    note = db.Column(db.Text)
    total_payment = db.Column(db.Float, nullable=False)
    updated_by = db.Column(db.String(50),nullable=False)

    order_details = db.relationship('OrderDetail', backref='order', lazy='subquery')


class OrderDetail(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total = self.quantity * self.price
