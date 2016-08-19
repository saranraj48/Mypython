from flask import Flask

app = Flask("__name__")

@app.route('/')

def ans():
    return str(10*5)
  

if __name__ == "__main__":
    app.run()

