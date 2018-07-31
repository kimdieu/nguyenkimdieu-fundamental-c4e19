from model.customer import Customer
from random import randint, choice
import mlab
from faker import Faker

mlab.connect()

fake = Faker()

for i in range (20):
    new_customer = Customer(
        name=fake.name(),
        gender=randint(0,1),
        email=fake.email(),
        phone=fake.phone_number(),
        job=fake.job(),
        company=fake.company(),
        contacted=choice([True,False])
    )

    new_customer.save()
