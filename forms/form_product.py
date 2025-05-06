from flask_wtf import FlaskForm
from wtforms import IntegerField,FileField,StringField,TextAreaField,BooleanField,SelectField,SubmitField,FloatField
from wtforms.validators import DataRequired,Length,NumberRange,ValidationError
from shop.models.category import Category
from flask_ckeditor import CKEditorField

class ProductForm(FlaskForm):
    name=StringField(
        "Tên Sản Phẩm",
          validators=[DataRequired(),Length(min=1,max=160)],
          render_kw={'class':'form-control'}
    )
    color=StringField(
        "Màu sắc",
          validators=[DataRequired(),Length(min=0,max=160)],
          render_kw={'class':'form-control'}
    )
    chatlieu=StringField(
        "Chất liệu",
          validators=[DataRequired(),Length(min=6,max=160)],
          render_kw={'class':'form-control'}
    )
    price=FloatField(
        "Giá Sản Phẩm",
          validators=[DataRequired(),NumberRange(min=0)],
          render_kw={'class':'form-control'}
    )
    desc=CKEditorField(
        "Mô tả",
          validators=[DataRequired(),Length(min=6)],
          render_kw={'class':'form-control'}
    )
    tonkho=IntegerField(
        "Tồn kho",
          validators=[DataRequired(),NumberRange(min=0)],
          render_kw={'class':'form-control'}
    )
    image=FileField(
        "Hình Sản Phẩm",
          render_kw={'class':'form-control'}
    )
    cannang=FloatField(
        "Cân nặng (kg) ",
          validators=[DataRequired(),NumberRange(min=0)],
          render_kw={'class':'form-control'}
    )
    chieucao=FloatField(
        "Chiều cao (cm)",
          validators=[DataRequired(),NumberRange(min=0)],
          render_kw={'class':'form-control'}
    )
    size_type=StringField(
        "Loại size (S,M,XL,XXL...)",
          validators=[DataRequired()],
          render_kw={'class':'form-control'}
    )
    kichthuoc=FloatField(
        "Kích thước (cm) ",
          validators=[DataRequired(),NumberRange(min=0)],
          render_kw={'class':'form-control'}
    )
    is_active=BooleanField("Kích hoạt",default=True)
    category_id=SelectField(
        "Danh mục sản phẩm",
          coerce=int,default=0,
          render_kw={'class':'form-control'}
    )
    submit=SubmitField(
        "Lưu",
        render_kw={'class':'btn btn-primary btn-sm'}
    )
   
    def validate_category_id(self,field):
        if not Category.query.get(field.data):
            raise ValidationError("Danh mục không hợp lệ!!!!")
