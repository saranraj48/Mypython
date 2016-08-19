from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login',methods="GET","POST")

def login():
    error = None
            if valid_login(request.form["Username"],request.form["Password"]):
                return log_the_user_in(request.form["username"])
            else:
                error = "Invalid username/password"
    return render_template("login.html",error=reeor)
    
         
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

