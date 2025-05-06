from flask_wtf import FlaskForm
from wtforms import IntegerField,FileField,StringField,TextAreaField,BooleanField,SelectField,SubmitField,FloatField
from wtforms.validators import DataRequired,Length,NumberRange,ValidationError
from shop.models.category import Category
from flask_ckeditor import CKEditorField

class BlogForm(FlaskForm):
    name=StringField(
        "Tên Sản Phẩm",
          validators=[DataRequired()],
          render_kw={'class':'form-control'}
    )
    designer=StringField(
        "Nhà thiết kế",
          validators=[DataRequired()],
          render_kw={'class':'form-control'}
    )
    desc=CKEditorField(
        "Mô tả",
          validators=[DataRequired(),Length(min=6)],
          render_kw={'class':'form-control'}
    )
    image=FileField(
        "Hình Sản Phẩm",
          render_kw={'class':'form-control'}
    )
    status = SelectField("Trạng thái", choices=[
        ("Chưa duyệt mẫu", "Chưa duyệt mẫu"),
        ("Đã duyệt", "Đã duyệt"),
        ("Đang sản xuất", "Đang sản xuất")
    ], default="Chưa duyệt mẫu",render_kw={'class':'form-control'})  # Mặc định là "Chưa duyệt mẫu"
    submit=SubmitField(
        "Lưu",
        render_kw={'class':'btn btn-primary btn-sm'}
    )
   
   
