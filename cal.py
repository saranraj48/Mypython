from flask import Flask,render_template,request

app = Flask(__name__)

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

