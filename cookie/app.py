from flask import Flask,request,render_template
from flask.helpers import make_response

app = Flask(__name__)

@app.route("/")
def index():

          return render_template("index.html")

@app.route("/new")
def new():
          admin  = "yuvaraj"
          resp = make_response("<h1> Hey you got this is adming cookie</h1>")
          resp.set_cookie("user",admin)

          return resp
@app.route("/login")
def login():
          userid = request.cookies.get('user')
          if userid == "yuvaraj":
                    return "<h1>PHY{i_L0v3_Y0u}</h1>"
          else:
                    return "<h2> 403 Unauthorized </h2>"
