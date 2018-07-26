from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Cach 1 (without render_template)
# @app.route('/bmi/<int:weight>/<int:height>')
# def BMI(weight, height):
#     m_height = height / 100
#     BMI = weight / (m_height * m_height)

#     if BMI < 16:
#         return ("Hi, your Body Mass Index = {0} ==> Severely underweight :(( ".format(BMI))

#     elif BMI < 18.5:
#         return ("Hi, your Body Mass Index = {0} ==> Underweight :( ".format(BMI))

#     elif BMI < 25:
#         return ("Hi, your Body Mass Index = {0} ==> Normal :)) ".format(BMI))

#     elif BMI < 30:
#         return ("Hi, your Body Mass Index = {0} ==> Overweight :( ".format(BMI))

#     else:
#         return ("Hi, your Body Mass Index = {0} ==> Obese :((( ".format(BMI))

# Cach 2 (with render_template)
@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight, height):
    m_height = height / 100
    BMI = weight / (m_height * m_height)

    if BMI < 16:
        warning = "Severely underweight :(("
        return render_template("ex1.html", BMI = BMI, warning = warning)

    elif BMI < 18.5:
        warning = "Underweight :("
        return render_template("ex1.html", BMI = BMI, warning = warning)

    elif BMI < 25:
        warning = "Normal :))"
        return render_template("ex1.html", BMI = BMI, warning = warning)

    elif BMI < 30:
        warning = "Overweight :("
        return render_template("ex1.html", BMI = BMI, warning = warning)

    else:
        warning = "Obese :(("
        return render_template("ex1.html", BMI = BMI, warning = warning)


if __name__ == '__main__':
  app.run(debug=True)
 