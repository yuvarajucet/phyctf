from flask import Flask,request,render_template,make_response
import requests

app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
          return render_template("index.html")

@app.route("/login")
def login():
          return render_template("login.html")

@app.route("/login1",methods=['POST','GET'])
def login1():
          if request.method == "POST":
                    email = request.form['email']
                    passw = request.form['password']
                    oripass = request.cookies.get('userpassword1')

                    if email == "sunnyleone@sunny.com":
                              if passw == oripass:
                                        return render_template("login.html",info="PHY{W0w_Y0u_D0n3_Acc0un7_t@k30v3r}")
                              else:
                                        return render_template("login.html",info=" username or password Wrong")
                    else:
                              return render_template("login.html",info="You trying others account please try given account..")



@app.route("/forget")
def forget():
          return render_template("forget.html",info="Enter the email address to send Forget link")

@app.route("/resetrequest",methods=['POST','GET'])
def resetrequest():
          if request.method == "POST":
                    email = request.form['email']
                    if email == "sunnyleone@sunny.com":
                              try:
                                        host = request.headers['X-Forwarded-Host']
                                        resetlink = "https://"+host+"/passwordreset?token=Jk7df9IAtF=="
                                                  
                              except:
                                        host = request.headers['host']
                                        resetlink = "https://"+host+"/passwordreset?token=Jk7df9IAtF=="
                              
                              requests.get(resetlink)

                              return render_template("forget.html",info="Password reset link send to your email address")
                    else:
                              return render_template("forget.html",info="You trying Others email..")

@app.route("/passwordreset")
def passwordreset():
          token = request.args.get("token")
          if token == "Jk7df9IAtF==":
                    return render_template("passwordreset.html")
          else:
                    return render_template("forget.html",info="Enter the email address to send forget link")



@app.route("/reset",methods=['POST','GET'])
def reset():
          if request.method == "POST":
                    passw = request.form['pass']
                    pass1 = request.form['pass1']
                    if passw == pass1:
                              resp = make_response(render_template("login.html",info="Password Reset Success!"))
                              resp.set_cookie("userpassword1",passw)
                              return resp
                    else:
                              return render_template("passwordreset.html",info="Password Mismatch!")