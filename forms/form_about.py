from flask_wtf import FlaskForm
from wtforms import FileField,StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired

from flask_ckeditor import CKEditorField

class AboutForm(FlaskForm):
    title=StringField(
        "Tiêu đề",
          validators=[DataRequired(message="Không được để trống")],
          render_kw={'class':'form-control'}
    )
    desc=CKEditorField(
        "Mô tả",
          validators=[DataRequired()],
          render_kw={'class':'form-control'}
    )
    image=FileField(
        "Hình Sản Phẩm",
          render_kw={'class':'form-control'}
    )
    is_active=BooleanField("Kích hoạt",default=True)
    submit=SubmitField(
        "Lưu",
        render_kw={'class':'btn btn-primary btn-sm'}
    )
   