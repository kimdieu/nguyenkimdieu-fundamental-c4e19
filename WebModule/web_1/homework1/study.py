from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def Study_hw():
    return ("Study_hw")

@app.route('/about-me')
def info():
    info = {
        "name" : "Dieu Nguyen",
        "dob" : "03/08/1999",
        "skul" : "Thăng Long University of Hanoi",
        "hobbies" : "To find out what my true hobby is"
    }
    return render_template("studies.html", info = info )

@app.route('/school')
def school():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
  app.run(debug=True)