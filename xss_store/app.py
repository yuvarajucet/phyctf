from flask import Flask,Response,request,render_template,make_response
import db
import random

app = Flask(__name__)
#test cmmand

@app.route("/")
def index():
          randvalue = random.randint(1111,9999)
          UUID = str(randvalue)
          User = "User"
          Secret_Key = "xymkzymmx=="
          resp = make_response(render_template("index.html"))
          resp.set_cookie("UUID",UUID)
          resp.set_cookie("USER",User)
          resp.set_cookie("Secret_Key",Secret_Key)
          return resp


@app.route("/acf")
def cookiesetfun():   
          randvalue = random.randint(1111,9999)
          UUID = str(randvalue)
          User = "Admin"
          Secret_Key = "YWRtaW5jcmVhZAo="
          comments = db.fetch_comment()
          resp = make_response(render_template("post.html",comment=comments,user="Admin"))
          resp.set_cookie("UUID",UUID)
          resp.set_cookie("USER",User)
          resp.set_cookie("Secret_Key",Secret_Key)
          return resp



@app.route("/cmt",methods=['POST','GET'])
def cmt():
          secret_key = request.cookies.get('Secret_Key')
          if secret_key == "YWRtaW5jcmVhZAo=":
                    msg = "dashboard"
                    return render_template("post.html",user="Admin",dashboard=msg)

          else:

                    if request.method == "POST":
                              comment = request.form['cmets']
                              comment = comment.replace("alert","")
                              comment = comment.replace("prompt","")
                              comment = comment.replace("print","")
                              comment = comment.replace("<!--","")
                              comment = comment.replace("<h1>","")
                              comment = comment.replace("<h2>","")
                              comment = comment.replace("<h3>","")
                              comment = comment.replace("<h4>","")
                              comment = comment.replace("<h5>","")
                              comment = comment.replace("<h6>","")
                              comment = comment.replace("<style>","")
                              comment = comment.replace("<html>","")
                              db.add_comment(comment)
          comments = db.fetch_comment()
          return render_template("post.html",user="user",comment=comments)
          
@app.route("/dashboard")
def dashboard():
          admin_user_key = request.cookies.get('Secret_Key')
          print(admin_user_key)
          if admin_user_key == "YWRtaW5jcmVhZAo=":
                    return render_template("dashboard.html",info="Admin loggedin")
                    
          else:
                    msg = "First you need to get Admin Cookie then try to access dashboard"
                    return render_template("post.html",user=msg)

@app.route("/null",methods=['POST','GET'])
def getflag():
          if request.method == "POST":
                    msg = "Cipher Flag: NM{QRK_LSS_GOFV_N_RGQY_KOPOCF}"
                    return render_template("dashboard.html",info=msg)
          else:
                    msg = "Try in diffrent method"
                    return render_template("dashboard.html",flag=msg)

