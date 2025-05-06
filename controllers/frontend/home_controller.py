from flask import Flask,redirect,render_template,Blueprint,request,flash,url_for,session,jsonify,Response
from shop.models.category import Category
from shop.models.product import Product,Order,OrderDetail
from shop.models.account import Account
from shop.models.about import About
from shop.models.blog import Blog
from sqlalchemy.sql.expression import func
from shop.forms.form_contact import ContactForm
from shop import db
from shop.models.contact import Contact
from shop.utils import generate_slug
from shop.models.menu import MenuItem
from shop.forms.form_profile import ProfileForm
from werkzeug.utils import secure_filename
from flask_login import current_user,login_required
from shop import db,bcrypt
import os
import time
from datetime import datetime
from flask import current_app as app


h_route=Blueprint("trang-chu",__name__,template_folder='../../templates/frontend')


def menu_list(items):
    html=''
    for item in items:
        if item.is_active:
            if item.children.count()>0:
                 html+=f'''
                    <div id="main-nav" class="stellarnav d-flex  ">
                            <ul class="menu-list">

                            <li class="menu-item has-sub">
                                <a href="#" class="item-anchor active d-flex align-item-center" data-effect="pages">{item.name}<i class="icon icon-chevron-down"></i></a>
                                    <ul class="submenu">
                                        <li > {menu_list(item.children)}</li>
                                    </ul>
                            </li>
                        </div>
                '''
            else:
                html+=f'<a href="{item.url}" class="item-anchor " data-effect="About">{item.name}</a>'
    return html
# trang chủ
@h_route.route("/")
def index():
    title="QUẦN SỌT NAM"
    keyword="quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao 1"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    list_allcate =(Product.query
                    .filter_by(is_active=True)
                    .order_by(Product.create_at.desc())
                    .limit(4)
                    .all())
    list_all =(Product.query
                    .filter_by(is_active=True)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_1 =(Product.query
                    .filter_by(category_id=3)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_2 =(Product.query
                    .filter_by(category_id=4)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_3 =(Product.query
                    .filter_by(category_id=12)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_4 =(Product.query
                    .filter_by(category_id=13)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_5 =(Product.query
                    .filter_by(category_id=14)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_6 =(Product.query
                    .filter_by(category_id=15)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_7 =(Product.query
                    .filter_by(category_id=16)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_8 = (Product.query
          .order_by(func.random())  # Sắp xếp ngẫu nhiên
          .limit(8)
          .all())
   
    return render_template("pages/home.html",**locals())

# trang sản phẩm
@h_route.route("/xa-kho")
def sanpham():
    title="QUẦN SỌT NAM KAKI"
    keyword="quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    list_allcate =(Product.query
                    .filter_by(is_active=True)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_all =(Product.query
                    .filter_by(is_active=True)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_1 =(Product.query
                    .filter_by(category_id=3)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_2 =(Product.query
                    .filter_by(category_id=4)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_3 =(Product.query
                    .filter_by(category_id=12)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_4 =(Product.query
                    .filter_by(category_id=13)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_5 =(Product.query
                    .filter_by(category_id=14)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_6 =(Product.query
                    .filter_by(category_id=15)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_7 =(Product.query
                    .filter_by(category_id=16)
                    .order_by(Product.create_at.desc())
                    .limit(8)
                    .all())
    list_8 = (Product.query
          .order_by(func.random())  # Sắp xếp ngẫu nhiên
          .limit(8)
          .all())
    
    # #phân trang
    # query=Product.query.filter_by(is_active=True)
    # page=request.args.get('page',1,type=int)
    # per_page=3  
    # product_list=query.paginate(page=page,per_page=per_page)  
    # sanpham_pt=product_list.items
    # pages = product_list.pages  
    return render_template("pages/sanpham.html",**locals())
@h_route.route('/filter/<price_range>')
def filter_by_price(price_range):
    title="LỌC QUẦN SỌT NAM KAKI"
    keyword="lọc theo quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    if price_range == '200000-plus':
        min_price = 200000
        products = Product.query.filter(Product.price > min_price).all()
        selected_range = f"Trên {min_price:,.0f} VND".replace(",", ".")
    else:
        try:
            min_price, max_price = map(int, price_range.split('-'))
            products = Product.query.filter(Product.price >= min_price, Product.price <= max_price).all()
            selected_range = f"{min_price:,.0f} - {max_price:,.0f} VND".replace(",", ".")
        except ValueError:
            # fallback nếu sai định dạng
            products = []
            selected_range = "Không xác định"
    return render_template('pages/gia.html',**locals())

@h_route.route("/search")
def search_product():
    title="TÌM QUẦN SỌT NAM KAKI"
    keyword="lọc theo quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    keyword = request.args.get('q', '').strip()
    
    if keyword:
        products = Product.query.filter(Product.name.ilike(f"%{keyword}%")).all()
    else:
        products = []

    return render_template('pages/search_result.html',**locals())

@h_route.route("/<name>-<int:id>")
def detail(name,id):
    title="QUẦN SỌT NAM GIÁ RẺ"
    keyword="quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    sp=Product.query.get_or_404(id)
    cate=Category.query.all()



    title=sp.name #set tiêu đề tên sp chi tiết
    keyword=sp.name
    desc=sp.desc

    #hot product
    hot=Product.query.filter(Product.is_active==True).limit(5).all()
    # lien quan
    splienquan=Product.query.filter(
        Product.category_id==sp.category_id,
        Product.id != sp.id,
        Product.is_active==True
        ).limit(4).all()
    list = (Blog.query
          .order_by(func.random())  # Sắp xếp ngẫu nhiên
          .limit(9)
          .all())
    return render_template("pages/detail.html",**locals())

@h_route.route('/giohang', methods=['GET', 'POST'])
def cart():
    # try:
        title="GIỎ HÀNG QUẦN SỌT NAM CHẤT LƯỢNG CAO"
        keyword="quần sọt hàn quốc"
        desc="quàn sọt chất lượng cao"
        menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
        menu_home=menu_list(menu_item)
        return render_template("pages/cart.html",**locals())
    # except Exception as e:
    #     return redirect(url_for('trang-chu.index'))
@h_route.route("/cart", methods=["GET","POST"])
def giohang():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    
    if 'cart' not in session:
        session['cart'] = {}  #tạo giỏ hàng rỗng

    giohang = session['cart']
    #giỏ hàng siêu thị
    if str(product_id) in giohang:
        giohang[str(product_id)]['quantity'] += quantity
    else:
        sp = Product.query.get(product_id)
        if sp:
            giohang[str(product_id)] = {
                'name': sp.name,
                'price': sp.price,
                'quantity': quantity,
                'image': sp.image
            }
        else:
            return jsonify({'status': 'error', 'message': 'Product not found'}), 404

    session['cart'] = giohang
    session.modified = True  # lưu thay đổi trong session

    return jsonify({'status': 'success', 'cart': giohang})

@h_route.route('/update-cart', methods=['POST'])
def update_cart():
    product_id = request.json.get('id')
    soluong = request.json.get('sl', 0)
    nhaptay = request.json.get('nhaptay', 1)

    cart = session.get('cart', {})

    if str(product_id) not in cart:
        return jsonify({'success': False, "message": "Product not found"}), 404

    sanpham = cart[str(product_id)]
    if nhaptay:
        new_quantity = max(1, soluong)
    else:
        new_quantity = max(1, sanpham['quantity'] + soluong)

    # Cập nhật lại số lượng trong giỏ hàng
    sanpham['quantity'] = new_quantity

    # Tính tổng giá và phí ship
    productTotal = sanpham['price'] * sanpham['quantity']
    cart_Total = sum(item['price'] * item['quantity'] for item in cart.values())

    # Tính phí ship theo điều kiện
    ship_fee = 30000 if cart_Total < 100000 else 0
    tongcoship = cart_Total + ship_fee

    # Gợi ý thông báo
    if ship_fee == 0:
        ship_message = "Bạn được miễn phí vận chuyển 🎉"
    else:
        ship_message = "Đơn hàng dưới 100.000đ, phí vận chuyển là 30.000đ"

    session['cart'] = cart
    session.modified = True

    return jsonify({
        'success': True,
        'new_quantity': new_quantity,
        'productTotal': productTotal,
        'cart_Total': cart_Total,
        'ship_fee': ship_fee,
        'tongcoship': tongcoship,
        'ship_message': ship_message
    })

@h_route.route('/shopping-delete',methods=['POST'])
def remove_cart():
    id=request.json.get('product_id')
    cart=session.get('cart',{})

    if str(id) in cart:
        del cart[str(id)]

    session['cart']=cart
    session.modified=True
    return jsonify({'status':'success','cart':cart})
# trang liên hệ
@h_route.route("/quan-sot-chat-luong-cao", methods=['GET', 'POST'])
def contact():
    title="QUẦN SỌT NAM CHẤT LƯỢNG CAO"
    keyword="quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    list_8 = (Product.query
          .order_by(func.random())  # Sắp xếp ngẫu nhiên
          .limit(8)
          .all())
    form = ContactForm()
    if form.validate_on_submit():
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
        return redirect(url_for('trang-chu.contact'))  # Điều hướng đúng Blueprint
    return render_template("pages/contact.html", **locals())


@h_route.route("/quan-sot-gia-tot")
def blog():
    title="QUẦN SỌT NAM GIÁ TỐT"
    keyword="quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    list_8 = (Product.query
          .order_by(func.random())  # Sắp xếp ngẫu nhiên
          .limit(8)
          .all())
    
    list = (Blog.query
          .order_by(func.random())  # Sắp xếp ngẫu nhiên
          .limit(9)
          .all())
    #phân trang
    query=Product.query.filter_by(is_active=True)
    page=request.args.get('page',1,type=int)
    per_page=3  
    product_list=query.paginate(page=page,per_page=per_page)  
    return render_template("pages/blog.html",**locals())

# trang about giới thiệu
@h_route.route("/quan-sot-phong-cach-han-quoc")
def about():
    title="QUẦN SỌT PHONG CÁCH HÀN QUỐC"
    keyword="quần sọt hàn quốc"
    desc="quàn sọt chất lượng cao"
    menu_item=MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home=menu_list(menu_item)
    ab = (About.query.all())
    return render_template("pages/about.html",**locals())

# trang profile
upload_folder='shop/static/upload/'

def create_order(user, cart, shipping_info=None, payment_method=None):
    total_payment = sum(item['price'] * item['quantity'] for item in cart.values())
    
    new_order = Order(
        user_id=user.id,
        total_payment=total_payment,
        shipping_fee=0,
        discount=0,
        status='Chờ xác nhận',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        updated_by=user.fullname,
        payment_method=payment_method,
        shipping_name=shipping_info.get('name') if shipping_info else None,
        shipping_phone=shipping_info.get('phone') if shipping_info else None,
        shipping_address=shipping_info.get('address') if shipping_info else None,
    )
    db.session.add(new_order)
    db.session.commit()

    for item in cart.values():
        order_detail = OrderDetail(
            order_id=new_order.id,
            product_name=item['name'],
            quantity=item['quantity'],
            price=item['price'],
            total=item['price'] * item['quantity']
        )
        db.session.add(order_detail)
    
    db.session.commit()
    return new_order


@h_route.route("/tai-khoan-ca-nhan",methods=['GET','POST'])
@login_required

def profile():
    title = "QUẦN SỌT PHONG CÁCH HÀN QUỐC"
    keyword = "quần sọt hàn quốc"
    desc = "quần sọt chất lượng cao"
    
    menu_item = MenuItem.query.filter(MenuItem.parent_id.is_(None)).all()
    menu_home = menu_list(menu_item)

    user = Account.query.get(current_user.id)
    orders = Order.query.filter_by(user_id=user.id).order_by(Order.id.desc()).all()
    form = ProfileForm(obj=user)

    if form.validate_on_submit():
        # Cập nhật thông tin cá nhân
        user.fullname = form.fullname.data
        user.phone = form.phone.data
        user.address = form.address.data

        # Cập nhật mật khẩu nếu có
        if form.password.data:
            user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Xử lý ảnh đại diện
        image_file = request.files.get("image")
        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            upload_dir = os.path.join(app.root_path, "static", "upload")
            image_path = os.path.join(upload_dir, filename)

            # Xóa ảnh cũ nếu có
            if user.image:
                old_image_path = os.path.join(upload_dir, user.image)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            image_file.save(image_path)
            user.image = filename

        db.session.commit()
        flash('Thông tin đã được cập nhật thành công!', 'success')
        return redirect(url_for('trang-chu.profile'))

    return render_template("pages/profile.html", **locals())



@h_route.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    user = Account.query.get(current_user.id)
    cart = session.get('cart', {})
    menu_item = MenuItem.query.filter(MenuItem.parent_id.is_(None)).order_by(MenuItem.order).all()
    menu_home = menu_list(menu_item)

    form = ProfileForm(obj=user)

    if request.method == 'POST':
        if cart:
            shipping_info = {
                'name': user.fullname,
                'phone': user.phone,
                'address': user.address
            }
            payment_method = request.form.get('payment_method')
            create_order(user, cart, shipping_info, payment_method)
            session.pop('cart', None)
            flash('Đặt hàng thành công!')
        return redirect(url_for('trang-chu.profile'))

    return render_template("pages/checkout.html", **locals())

@h_route.route("/sitemap.xml")
def sitemap():
    sanpham=Product.query.filter_by(is_active=True).all()#lấy tất cả sp
    danhmuc=Category.query.filter_by(is_active=True).all()#lấy tất cả danh mục

    baseurl="http://127.0.0.1:5000/" #tên miền(domain)
    xml=[]
    xml.append('<?xml version="1.0" encoding="UTF-8"?>')
    xml.append('<?xml-stylesheet type="text/xsl" href="/static/sitemap.xsl"?>')
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    #tạo  url xml cho trang chủ 
    xml.append(f""" 
       <url>
               <loc>{baseurl}</loc>
               <lastmod>{datetime.utcnow().date()}</lastmod>
               <changefreq>daily</changefreq>
               <priority>1.0</priority>
       </url>
    """)
      #tạo  url xml cho danh mục
    for cate in danhmuc:
        cate_url=url_for("trang-chu.sanpham",cat_id=cate.id)
        
        xml.append(f""" 
            <url>
                    <loc>{baseurl}{cate_url}</loc>
                    <lastmod>{cate.update_at.date()}</lastmod>
                    <changefreq>daily</changefreq>
                    <priority>0.9</priority>
            </url>
        """)
          #tạo  url xml cho sản phẩm
    for sp in sanpham:
        sp_url=url_for("trang-chu.detail",name=generate_slug(sp.name),id=sp.id)
        
        xml.append(f""" 
            <url>
                    <loc>{baseurl}{sp_url}</loc>
                    <lastmod>{sp.update_at.date()}</lastmod>
                    <changefreq>daily</changefreq>
                    <priority>0.8</priority>
            </url>
        """)
     
    xml.append('</urlset>')
    res=Response("\n".join(xml),mimetype='application/xml')
    # res.headers['Content-Type']='application/xml; charset=utf-8'
    res = Response("\n".join(xml), mimetype='text/xml')

    return res