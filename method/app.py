from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
          return render_template("index.html")


@app.route("/flag",methods=['POST','GET'])
def flag():
          if request.method == "POST":
                    flag = "PHY{N0w_y0u_@r3_H@ck3r}"
                    return render_template("flag.html",flag=flag)
          elif request.method == "GET":
                    flag = "Inga flag illa Machi.... Yeppoum GET panna nenaikka kudaathu.. Okeeey..."
                    return render_template("flag.html",flag=flag)