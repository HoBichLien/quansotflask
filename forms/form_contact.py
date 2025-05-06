from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField("Tên", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Số điện thoại", validators=[DataRequired()])
    message = TextAreaField("Nội dung", validators=[DataRequired()])
    submit = SubmitField("Gửi liên hệ")