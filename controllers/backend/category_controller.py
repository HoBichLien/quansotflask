from flask import flash,Blueprint,render_template,redirect,url_for
from shop.models.category import Category
from shop.forms.form_category import CategoryForm
from shop import db

cate_route=Blueprint("cate",__name__,template_folder='../../templates/backend/category')

@cate_route.route("/")
def index():
    form=Category.query.all()
    return render_template("list.html",form=form)

@cate_route.route("/add",methods=['GET','POST'])
def add():
    form=CategoryForm()
    form.parent_id.choices=[(0,"Chọn danh mục")]+[(cat.id,cat.name) for cat in Category.query.all()]
    if form.validate_on_submit():
        new_cate = Category(
            name=form.name.data,
            desc=form.desc.data,
            is_active=form.is_active.data,
            parent_id=form.parent_id.data if form.parent_id.data !=0 else None
        )
        db.session.add(new_cate)
        db.session.commit()
        flash("Thêm danh mục thành công!", "info")
        return redirect(url_for("quan-sot.cate.index"))
    return render_template("form.html",form=form)

@cate_route.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    dm=Category.query.get_or_404(id)
    form=CategoryForm(obj=dm)
    form.parent_id.choices=[(0,"Chọn danh mục")]+[(cat.id,cat.name) for cat in Category.query.all() if cat.id !=id]
    if form.validate_on_submit():
        dm.name=form.name.data
        dm.desc=form.desc.data
        dm.is_active=form.is_active.data
        dm.parent_id=form.parent_id.data if form.parent_id.data !=0 else None
       
        db.session.commit()
        flash("Cập nhật danh mục thành công!", "success")
        return redirect(url_for("quan-sot.cate.index"))
    return render_template("form.html",form=form)

@cate_route.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    dm=Category.query.get_or_404(id)
    db.session.delete(dm)
    db.session.commit()
    flash("Xóa danh mục thành công!", "danger")
    return redirect(url_for("quan-sot.cate.index"))