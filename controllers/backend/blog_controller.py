import os
from flask import Flask,redirect,render_template,request,flash,url_for,Blueprint
from shop import db
from shop.models.blog import Blog
from shop.forms.form_blog import BlogForm
from werkzeug.utils import secure_filename
import time


blog_route=Blueprint("blog",__name__)

upload_folder='shop/static/upload/'
allow_extension={'png','jpg','gif','jpeg'}

def allow_files(filename):
     return'.' in filename and filename.rsplit('.',1)[1].lower() in allow_extension
@blog_route.route("/")
def index():
    pro=Blog.query.all()
    return render_template("backend/blog/list.html",pro=pro)

@blog_route.route("/add", methods=['GET', 'POST'])
def add():
    form = BlogForm()

    if form.validate_on_submit():
        tenhinh = None
        if 'image' in request.files and allow_files(request.files['image'].filename):
            hinh = request.files['image']
            hinhgoc = secure_filename(hinh.filename)
            chuoi = str(int(time.time()))
            tenhinh = f'{chuoi}_{hinhgoc}'
            hinh.save(os.path.join(upload_folder, tenhinh))

        sp = Blog(
            name=form.name.data,
            designer=form.designer.data,
            desc=form.desc.data,
            image=tenhinh,
            status=form.status.data,  # Lấy giá trị từ form
        )
        db.session.add(sp)
        db.session.commit()
        flash("Thêm thông tin thành công!!!", "info")
        return redirect(url_for('quan-sot.blog.index'))

    return render_template("backend/blog/form.html", form=form)


@blog_route.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    pro=Blog.query.get_or_404(id)
    form=BlogForm(obj=pro)
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
        pro.designer=form.designer.data
        pro.desc=form.desc.data
        pro.image=tenhinh
        pro.status=form.status.data
        db.session.commit()
        flash("Sửa thông tin thành công!!!","success")
        return redirect(url_for('quan-sot.blog.index'))
    return render_template("backend/blog/form.html",form=form)

@blog_route.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    sp=Blog.query.get_or_404(id)
    tenhinh=sp.image
    duongdan=os.path.join(upload_folder,tenhinh)
    if os.path.isfile(duongdan):
        os.remove(duongdan)
    db.session.delete(sp)
    db.session.commit()
    flash("Xóa thông tin thành công!!!","danger")
    return redirect(url_for('quan-sot.blog.index'))