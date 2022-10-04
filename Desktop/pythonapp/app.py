from crypt import methods
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def hello():
    # return "Hello, flask"
def index():
    return render_template("index.html",user="홍길동",data={'level':60,'point':3600})
    
if __name__ == "__main__":
    # app.run(host="localhost",port="8200",debug=True)
    app.run()



