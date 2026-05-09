from flask import Flask

'''
It creates an instance of the Flask class , 
which will be your WSGI application
'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to best flask course. This should be amazing course"

@app.route("/index")
def index():
    return "Welcome to index page"


if __name__ == "__main__":
    app.run(debug = True)

