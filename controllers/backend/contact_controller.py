from flask import render_template, request, redirect, flash, url_for, Blueprint
from shop import db
from shop.models.contact import Contact  # Import model Contact
from shop.forms.form_contact import ContactForm  # Import form ContactForm
from flask_mail import Mail, Message


contact_route = Blueprint("contact", __name__)
# Khởi tạo Flask-Mail
mail = Mail()
# Hiển thị danh sách liên hệ trong Admin
@contact_route.route("/admin/list")
def index():
    contacts = Contact.query.all()  # Load danh sách liên hệ từ database
    return render_template("backend/contact/list.html", contacts=contacts)

# Trang liên hệ cho người dùng gửi form
@contact_route.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():  # Kiểm tra nếu form hợp lệ
        new_contact = Contact(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            message=form.message.data,
            status="Chưa xử lý"
        )
        db.session.add(new_contact)
        db.session.commit()
        flash("Gửi liên hệ thành công!", "success")
        return redirect(url_for('contact.contact'))  # Đúng Blueprint
    return render_template('frontend/contact.html', form=form)

# Admin xử lý phản hồi
@contact_route.route('/edit/<int:id>', methods=['GET','POST'])
def reply_contact(id):
    contact = Contact.query.get(id)
    
    if request.method == 'POST':
        reply_message = request.form.get('reply_message')
        
        # Cập nhật database
        contact.admin_reply = reply_message
        contact.status = "Đã xử lý"
        db.session.commit()

        # Gửi email phản hồi cho người dùng
        subject = "Phản hồi liên hệ từ website"
        body = f"Chào {contact.name},\n\nCảm ơn bạn đã liên hệ với chúng tôi. Dưới đây là phản hồi từ admin:\n\n{reply_message}\n\nTrân trọng,\nAdmin"
        
        try:
            msg = Message(subject, recipients=[contact.email], body=body)
            mail.send(msg)
            flash("✅ Đã gửi phản hồi đến người dùng qua email!", "success")
        except Exception as e:
            import traceback
            print("❌ Lỗi gửi email:")
            print(traceback.format_exc())  # In ra toàn bộ lỗi
            flash(f"❌ Lỗi gửi email: {e}", "danger")

        return redirect(url_for('quan-sot.contact.index'))  # Quay về danh sách liên hệ

    return render_template("backend/contact/form.html", contact=contact)

