import re
from flask import Flask
from shop import create_app, db
from flask_mail import Mail

def highlight_text(text):
    """Tô màu đỏ & in nghiêng 'LIEN NAM', tô màu xanh 'Chất lượng - Phong cách - Giá tốt'."""
    if text:
        text = re.sub(r'(LIEN NAM)', r'<span style="color: red; font-style: italic;">\1</span>', text)
       
    return text

app = create_app()  # Tạo app trước
app.jinja_env.filters['highlight_text'] = highlight_text  # Đăng ký filter
# Khởi tạo Flask-Mail
mail = Mail(app)
# Khởi tạo database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    
    app.run(debug=True)
