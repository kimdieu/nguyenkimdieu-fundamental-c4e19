from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title":"Tho cn coc",
            "content":"""
                Hom nay trang len cao qua
                Anh muon hon em vao ma
            """,
            "author":"TAnh",
            "gender": 1
        },
        {
            "title":"Tho xam",
            "content":"Thu xinh nhu cun",
            "author":"Thu xinh",
            "gender": 0

        },
        {
            "gender": 0,
            "author":"nguoi la",
            "title":"tho"
        }
        ]
    
    return render_template(
        "index.html", posts= posts)

@app.route('/hello')
def hello():
    return "Hello C4E 19"

@app.route('/say-hi/<name>/<age>')
def say_hi(name, age):
    return "Hi {0} you're {1} year(s) old this year (2018).".format(name, age)

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    sum = num1 + num2
    return "{0} + {1} = {2}".format(num1,num2,sum)

if __name__ == '__main__':
  app.run(debug=True)
 