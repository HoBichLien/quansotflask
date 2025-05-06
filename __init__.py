from flask import Flask,Blueprint,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from shop.config import Config,ConfigGoogle,EmailConfig
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,login_required,current_user
from flask_mail import Mail
from authlib.integrations.flask_client import OAuth
from shop.utils import generate_slug
import os
from datetime import datetime

db=SQLAlchemy()
app=Flask(__name__)

# app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'),static_url_path='/shop/static')
bcrypt=Bcrypt(app)
#khởi tạo mới 1 login manager để quản lý
login_manager = LoginManager()
# tải cấu hình email vào ứng dụng flask
app.config.from_object(EmailConfig)
#khởi tạo mail
mail=Mail(app)
#cấu hình auth tải cấu hính API của gmail vào flask
app.config.from_object(ConfigGoogle)
oauth=OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    access_token_url=app.config['GOOGLE_ACCESS_TOKEN_URL'],
    authorize_url=app.config['GOOGLE_AUTHORIZE_URL'],
    userinfo_endpoint=app.config['GOOGLE_USERINFO_ENDPOINT'],
    client_kwargs={'scope': 'openid email profile'},
    jwks_uri="https://www.googleapis.com/oauth2/v3/certs"
)

def create_app():
    
    app.config.from_object(Config)
    db.init_app(app)
    # bcrypt
    login_manager.init_app(app)
    login_manager.login_view="secure.login"
    #đưa generate_slug vào jinja chỗ khi tạo bị lỗi hay hiện trên giao diện
    app.jinja_env.filters["slug"]=generate_slug

    #route backend
    
    from shop.controllers.backend.manager_controller import m_route
    from shop.controllers.backend.category_controller import cate_route
    from shop.controllers.backend.product_controller import pro_route
    from shop.controllers.backend.account_controller import acc_route
    from shop.controllers.backend.about_controller import about_route
    from shop.controllers.backend.contact_controller import contact_route
    from shop.controllers.backend.blog_controller import blog_route
    from shop.controllers.backend.menu_controller import menu_route
    from shop.controllers.backend.oder_controller import oder_route

    # đăng ký blueprint backend
    sys_route=Blueprint("quan-sot",__name__)
    #kiểm tra role
    @sys_route.before_request
    @login_required
    def check_admin():
        if not current_user.has_role("admin"):
            flash("Bạn không có quyền truy cập","warning")
            return redirect(url_for('secure.login'))
    sys_route.register_blueprint(m_route,url_prefix='/trong-kho')
    sys_route.register_blueprint(cate_route,url_prefix='/phan-loai')
    sys_route.register_blueprint(pro_route,url_prefix='/san-pham')
    sys_route.register_blueprint(acc_route,url_prefix='/nguoi-dung')
    sys_route.register_blueprint(about_route,url_prefix='/gioi-thieu')
    sys_route.register_blueprint(contact_route,url_prefix='/lien-he')
    sys_route.register_blueprint(blog_route,url_prefix='/thiet-ke')
    sys_route.register_blueprint(menu_route,url_prefix='/menu')
    sys_route.register_blueprint(oder_route,url_prefix='/donhang')
    app.register_blueprint(sys_route,url_prefix='/quan-sot-nam')

     #route frontend
     # đăng ký blueprint frontend
    from shop.controllers.frontend.home_controller import h_route
    from shop.controllers.frontend.secure_controller import secure_route
    app.register_blueprint(h_route,url_prefix='/quansot')
    app.register_blueprint(secure_route,url_prefix='/dangki')
    return app

    
   
