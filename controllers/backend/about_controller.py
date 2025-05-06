from flask import redirect,request,render_template,Blueprint,url_for,flash,Flask
from shop import db
import os
from shop.models.about import About
from shop.forms.form_about import AboutForm
import time
from werkzeug.utils import secure_filename

about_route=Blueprint("about",__name__)


upload_folder='shop/static/upload/'
allow_extension={'png','jpg','gif','jpeg'}

def allow_files(filename):
     return'.' in filename and filename.rsplit('.',1)[1].lower() in allow_extension

@about_route.route("/")
def index():
    ab=About.query.all()
    return render_template("backend/about/list.html",ab=ab)

@about_route.route("/add",methods=['GET','POST'])
def add():
    form=AboutForm()
    if form.validate_on_submit():
        tenhinh=None
        if 'image' in request.files and allow_files(request.files['image'].filename):
            hinh=request.files['image']
            hinhgoc=secure_filename(hinh.filename)
            chuoi=str(int(time.time()))
            tenhinh=f'{chuoi}_{hinhgoc}'
            hinh.save(os.path.join(upload_folder,tenhinh))
        ab=About(
           title=form.title.data,
           desc=form.desc.data,
           image=tenhinh,
           is_active=form.is_active.data,
        )
        db.session.add(ab)
        db.session.commit()
        flash("Thêm tiêu đề thành công!!!","info")
        return redirect(url_for('quan-sot.about.index'))
    return render_template("backend/about/form.html",form=form)

@about_route.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    about=About.query.get_or_404(id)
    form=AboutForm(obj=about)
    if form.validate_on_submit():
        # tenhinh=None
        if 'image' in request.files and allow_files(request.files['image'].filename):
            # xóa hình cũ
            hinhcu=about.image
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
            tenhinh=about.image
        about.title=form.title.data
        about.desc=form.desc.data
        about.image=tenhinh
        about.is_active=form.is_active.data
        db.session.commit()
        flash("Sửa tiêu đề thành công!!!","success")
        return redirect(url_for('quan-sot.about.index'))
    return render_template("backend/about/form.html",form=form)

@about_route.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    ab=About.query.get_or_404(id)
    tenhinh=ab.image
    duongdan=os.path.join(upload_folder,tenhinh)
    if os.path.isfile(duongdan):
        os.remove(duongdan)
    db.session.delete(ab)
    db.session.commit()
    flash("Xóa tiêu đề thành công!!!","danger")
    return redirect(url_for('quan-sot.about.index'))