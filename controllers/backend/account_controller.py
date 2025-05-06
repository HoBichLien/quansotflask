from flask import Flask,redirect,render_template,request,url_for,Blueprint,flash
import os
from shop import db,bcrypt
from shop.models.account import Account
from shop.forms.form_account import RegisterForm
import time
from werkzeug.utils import secure_filename

acc_route=Blueprint("acc",__name__)

upload_folder='shop/static/upload/'
allow_extension={'png','jpg','gif','jpeg'}

def allow_files(filename):
     return'.' in filename and filename.rsplit('.',1)[1].lower() in allow_extension

@acc_route.route("/")
def index():
    form=Account.query.all()
    return render_template("backend/account/list.html",form=form)

@acc_route.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    acc = Account.query.get_or_404(id)
    form = RegisterForm(obj=acc)
    form._obj = acc
    if form.validate_on_submit():
        # Giữ nguyên ảnh cũ nếu không có ảnh mới
        tenhinh = acc.image if acc.image else None  

        # Nếu có ảnh mới được upload
        if 'image' in request.files and allow_files(request.files['image'].filename):
            hinh = request.files['image']
            hinhgoc = secure_filename(hinh.filename)
            chuoi = str(int(time.time()))
            tenhinh = f'{chuoi}_{hinhgoc}'
            hinh.save(os.path.join(upload_folder, tenhinh))

        # Cập nhật thông tin nhưng giữ nguyên email
        acc.fullname = form.fullname.data
        if form.password.data:  # Nếu có nhập mật khẩu mới
            acc.password = bcrypt.generate_password_hash(form.password.data)  # Hàm hash mật khẩu

        acc.phone = form.phone.data
        acc.address = form.address.data
        acc.image = tenhinh  # Cập nhật ảnh mới nếu có
        acc.role = form.role.data
        acc.is_active = form.is_active.data

        db.session.commit()
        flash("Sửa tài khoản thành công!", "success")
        return redirect(url_for('quan-sot.acc.index'))

    return render_template("backend/account/form.html", form=form)


@acc_route.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    acc=Account.query.get_or_404(id)
    db.session.delete(acc)
    db.session.commit()
    flash("Xóa người dùng thành công!!!","danger")
    return redirect(url_for('quan-sot.acc.index'))