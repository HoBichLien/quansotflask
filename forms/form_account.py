from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField,SubmitField,PasswordField,FileField
from wtforms.validators import DataRequired, Length,Email,Regexp,ValidationError,Optional
from shop.models.account import Account

class RegisterForm(FlaskForm):
    fullname=StringField(
        "Họ Và Tên", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Length(min=2,max=160,message='Nhập từ 2 - 32 ký tự')
        ],
        render_kw={'class':'form-control','placeholder':'Nhập họ và tên'} #thêm class form-control
    )
    email=StringField(
        "Email", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Email()
        ],
        
        render_kw={'class':'form-control','placeholder':'Nhập email'} 
        
    )
    password=PasswordField(
        "Mật khẩu", 
        validators=[
            Optional(),
            Length(min=6,max=32,message='Nhập từ 6 - 32 ký tự'),
            Regexp('^[a-zA-Z0-9]*$',message='Mật khẩu chỉ được phép nhập ký tự và số')
        ],
        render_kw={'class':'form-control','placeholder':'nhập mật khẩu'} 
    )
    phone=StringField(
        "Phone", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Length(min=10,max=12,message='Nhập từ 10 - 12 số'),
            Regexp('^[0-9]*$',message='Số điện thoại chỉ được phép nhập số')
        ],
        render_kw={'class':'form-control','placeholder':'Nhập số điện thoại'} 
    )
    address=StringField(
        "Địa chỉ", 
        
        render_kw={'class':'form-control','placeholder':'Nhập địa chỉ '} 
    )
    image=FileField(
        "Avatar",
        render_kw={'class':'form-control'} 
    )
    submit=SubmitField(
        'Đăng Ký',
        render_kw={'class':'btn btn-primary btn-sm'} 
    )
    is_active=BooleanField("Kích hoạt",default=True)
    role=StringField(
        "Phân quyền",
        render_kw={'class':'form-control'})

    # def validate_email(self,email):
    #     if Account.query.filter_by(email=email.data).first():
    #         raise ValidationError("Email đã tồn tại, vui lòng nhập email khác")
        
    def validate_email(self, field):
        account = getattr(self, "_obj", None)  # Lấy dữ liệu account nếu đang edit

        # Nếu đang chỉnh sửa và email không thay đổi, bỏ qua kiểm tra
        if account and account.email == field.data:
            return  

        # Nếu email đã tồn tại trong database, báo lỗi
        if Account.query.filter_by(email=field.data).first():
            raise ValidationError("Email đã tồn tại, vui lòng chọn email khác!")


class LoginForm(FlaskForm):
    email=StringField(
        "Email", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Email()
        ],
        render_kw={'class':'form-control','placeholder':'Nhập email'} 
    )
    password=PasswordField(
        "Mật khẩu", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Length(min=6,max=32,message='Nhập từ 6 - 32 ký tự'),
            Regexp('^[a-zA-Z0-9]*$',message='Mật khẩu chỉ được phép nhập ký tự và số')
        ],
        render_kw={'class':'form-control','placeholder':'Nhập mật khẩu'} 
    )
    remember=BooleanField('Remember',default=True)
    submit=SubmitField(
        'Đăng nhập',
        render_kw={'class':'btn btn-primary btn-sm'} 
    )
# quên mk
class FogetForm(FlaskForm):
    email=StringField(
        "Email", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Email()
        ],
        render_kw={'class':'form-control','placeholder':'Nhập email'} 
    )
    phone=StringField(
        "Phone", 
        validators=[
            DataRequired(message='Vui lòng không để trống'),
            Length(min=10,max=32,message='Nhập từ 10 - 12 ký tự'),
            Regexp('^[0-9]*$',message='Phone  chỉ được phép nhập  số')
        ],
        render_kw={'class':'form-control','placeholder':'Nhập số diện thoại'} 
    )

    submit=SubmitField(
        'Khôi phục',
        render_kw={'class':'btn btn-primary btn-sm'} 
    )