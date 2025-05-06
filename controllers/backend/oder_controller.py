import os
from flask import Flask,redirect,render_template,request,flash,url_for,Blueprint
from shop import db
from flask_login import current_user,login_required
from shop.models.product import Order,OrderDetail
from shop.forms.form_product import ProductForm
from werkzeug.utils import secure_filename
from flask import abort
from datetime import datetime


oder_route=Blueprint("oder",__name__)

@oder_route.route('/don-hang')
@login_required
def admin_orders():
    if current_user.role != 'admin': 
        abort(403)
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('backend/oder/orders.html', orders=orders)

@oder_route.route('/donhang/orders/<int:order_id>', methods=['GET', 'POST'])
@login_required
def admin_order_detail(order_id):
    if current_user.role != 'admin':
        abort(403)

    order = Order.query.get_or_404(order_id)

    if request.method == 'POST':
        # Lấy dữ liệu từ form
        status = request.form.get('status')
        note = request.form.get('note')  # nếu có
        if status:
            order.status = status
            order.updated_by = current_user.fullname
            order.updated_at = datetime.utcnow()  # cập nhật thời gian
            order.note = note
            db.session.commit()
            flash('Cập nhật trạng thái đơn hàng thành công!', 'success')
            return redirect(url_for('quan-sot.oder.admin_order_detail', order_id=order.id))

    return render_template('backend/oder/order_detail.html', order=order)
