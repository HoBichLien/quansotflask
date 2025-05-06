from flask import redirect,render_template,Blueprint

m_route=Blueprint("trong-kho",__name__,template_folder='../../templates/backend/manager')

@m_route.route("/")
def index():
    return render_template("dashboard.html")

@m_route.route("/config")
def config():
    return render_template("config.html")
