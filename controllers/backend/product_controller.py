import os
from flask import Flask,redirect,render_template,request,flash,url_for,Blueprint
from shop import db
from shop.models.category import Category
from shop.models.product import Product
from shop.forms.form_product import ProductForm
from werkzeug.utils import secure_filename
import time

pro_route=Blueprint("pro",__name__)

upload_folder='shop/static/upload/'
allow_extension={'png','jpg','gif','jpeg'}

def allow_files(filename):
     return'.' in filename and filename.rsplit('.',1)[1].lower() in allow_extension


@pro_route.route("/")
def index():
    pro=Product.query.all()
    return render_template("backend/product/list.html",pro=pro)

@pro_route.route("/add",methods=['GET','POST'])
def add():
    form=ProductForm()
    form.category_id.choices=[(0,"Chọn danh mục")]+[(c.id,c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        tenhinh=None
        if 'image' in request.files and allow_files(request.files['image'].filename):
            hinh=request.files['image']
            hinhgoc=secure_filename(hinh.filename)
            chuoi=str(int(time.time()))
            tenhinh=f'{chuoi}_{hinhgoc}'
            hinh.save(os.path.join(upload_folder,tenhinh))
        sp=Product(
           name=form.name.data,
           color=form.color.data,
           chatlieu=form.chatlieu.data,
           price=form.price.data,
           desc=form.desc.data,
           tonkho=form.tonkho.data,
           image=tenhinh,
           cannang=form.cannang.data,
           chieucao=form.chieucao.data,
           size_type=form.size_type.data,
           kichthuoc=form.kichthuoc.data,
           is_active=form.is_active.data,
           category_id = form.category_id.data,
        )
        db.session.add(sp)
        db.session.commit()
        flash("Thêm sản phẩm thành công!!!","info")
        return redirect(url_for('quan-sot.pro.index'))
    return render_template("backend/product/form.html",form=form)

@pro_route.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    pro=Product.query.get_or_404(id)
    form=ProductForm(obj=pro)
    form.category_id.choices=[(0,"Chọn danh mục")]+[(c.id,c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        # tenhinh=None
        if 'image' in request.files and allow_files(request.files['image'].filename):
            # xóa hình cũ
            hinhcu=pro.image
            duongdan=os.path.join(upload_folder,hinhcu)
            if os.path.isfile(duongdan):
                os.remove(duongdan)
            # cập nhật hình mới
            hinh=request.files['image']
            hinhgoc=secure_filename(hinh.filename)
            chuoi=str(int(time.time()))
            tenhinh=f'{chuoi}_{hinhgoc}'
            hinh.save(os.path.join(upload_folder,tenhinh))

        else:
            tenhinh=pro.image
        pro.name=form.name.data
        pro.color=form.color.data
        pro.chatlieu=form.chatlieu.data
        pro.price=form.price.data
        pro.desc=form.desc.data
        pro.tonkho=form.tonkho.data
        pro.image=tenhinh
        pro.cannang=form.cannang.data
        pro.chieucao=form.chieucao.data
        pro.size_type=form.size_type.data
        pro.kichthuoc=form.kichthuoc.data
        pro.is_active=form.is_active.data
        pro.category_id = form.category_id.data
        db.session.commit()
        flash("Sửa sản phẩm thành công!!!","success")
        return redirect(url_for('quan-sot.pro.index'))
    return render_template("backend/product/form.html",form=form)

@pro_route.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    sp=Product.query.get_or_404(id)
    tenhinh=sp.image
    duongdan=os.path.join(upload_folder,tenhinh)
    if os.path.isfile(duongdan):
        os.remove(duongdan)
    db.session.delete(sp)
    db.session.commit()
    flash("Xóa sản phẩm thành công!!!","danger")
    return redirect(url_for('quan-sot.pro.index'))
