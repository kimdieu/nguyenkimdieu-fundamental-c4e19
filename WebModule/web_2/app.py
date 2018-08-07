from flask import *
from model.service import Service
from model.customer import Customer
import mlab
app = Flask(__name__)

mlab.connect()

# design database

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service=all_service)

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(
            name=name,
            yob=yob,
            phone=phone,
            gender=gender
        )

        new_service.save()

        return redirect(url_for('admin'))

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

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

# web_3
@app.route('/search')
def searchch():
    all_service= Service.objects()
    return render_template('search.html', all_service=all_service)

@app.route('/detail/<customer_id>')
def detail(customer_id):
    customer_id = Service.objects.with_id(customer_id)
    return render_template('detail.html', customer_id=customer_id)

@app.route('/update-service/<customer_id>', methods=["GET", "POST"])
def update_service(customer_id):
    customer_id = Service.objects.with_id(customer_id)
    
    if request.method == "GET":
        return render_template('update_service.html', customer_id=customer_id)

    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        customer_id.update(set__name=name, set__yob=yob, set__phone=phone, set__gender=gender)
        customer_id.save()
        customer_id.reload()

        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
 