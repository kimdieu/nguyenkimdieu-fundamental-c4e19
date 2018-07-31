from flask import Flask, render_template
from model.service import Service
from model.customer import Customer
import mlab
app = Flask(__name__)

mlab.connect()

# design database

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def link():
    return render_template('10_cus.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender, yob__lte = 1998, address__icontains= "Hanoi")
    
    return render_template('search.html', all_service=all_service)

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

@app.route('/tenmale')
def tenmale():
    ten_male = Customer.objects(gender=1, contacted= False)[:10]
    return render_template('customer.html', all_customer=ten_male)



if __name__ == '__main__':
  app.run(debug=True)
 