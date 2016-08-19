from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login',methods="GET","POST")

def login():
   
    return render_template("login.html",error=reeor)
    return render_template("login.html")
    if(request.form["text"]== "saran" and request.form["password"]== "saran"):
        return render_template("welcome.html")

    else:
        return render_template("try.html")
         
@app.route('/welcome')

def welcome():
    return render_template("welcome.html")

@app.route('/calc',methods=["POST","GET"])

def calc(): 
    return render_template("calc.html")

@app.route('/result',methods=["POST"])

def result():
    return str(int(request.form["a"])+int(request.form["b"]))

if __name__ == "__main__":
    app.run()

