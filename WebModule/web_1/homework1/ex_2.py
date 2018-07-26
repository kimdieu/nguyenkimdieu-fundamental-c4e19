from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def user(username):
    user = {
	"quan" : {
			"name" : "Nguyen Anh Quan",
			"age" : 6
            },
    "tuananh" : {
                "name" : "Huynh Tuan Anh",
                "age" : 23
            }
    }

    if username in user:
        prof = user[username]
        return render_template("ex2.html", prof = prof)

    else:
        return ("User not found")

if __name__ == '__main__':
  app.run(debug=True)
