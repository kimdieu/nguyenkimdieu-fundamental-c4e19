from flask import *
from model.service import Service
from model.customer import Customer
from model.user import User
from model.order import Order
import mlab
import datetime
from random import choice

app = Flask(__name__)

app.secret_key = 'a super secret key'

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

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
    if 'logged_in' in session:
        if session['logged_in']:
            customer_id = Service.objects.with_id(customer_id)
            return render_template('detail.html', customer_id=customer_id)
    else:
        return redirect(url_for('login'))

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

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    
    if request.method == 'GET':
        return render_template('sign_in.html')

    elif request.method == 'POST':
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(
            fullname=fullname,
            email=email,
            username=username,
            password=password
        )

        new_user.save()
        
        return "Your information is saved."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']

        server = User.objects(username=username, password=password)

        if len(server) != 0:
            # print (server[0].id)
            session['logged_in'] = True
            session['user_id'] = str(server[0].id)
            return redirect(url_for('searchch'))
        else:
            return ("Sai tên đăng nhập hoặc mật khẩu :(")

@app.route('/logout')
def logout():
    del session['logged_in']
    return redirect(url_for('searchch'))

@app.route('/order/<customerid>')
def order(customerid):
    service_id = customerid
    user_id = session['user_id']
    time = datetime.datetime.now()
    is_accepted = choice([True, False])

    new_order = Order(
        service_id=service_id,
        user_id=user_id,
        time = time,
        is_accepted = is_accepted
    )
    new_order.save()

    return "Đã gửi yêu cầu"

if __name__ == '__main__':
  app.run(debug=True)
 