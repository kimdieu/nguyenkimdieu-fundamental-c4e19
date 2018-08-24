from model.service import Service
import mlab
from faker import Faker
from random import randint, choice, sample

mlab.connect()

fake = Faker()

image_list = ['https://kenh14cdn.com/2017/1475129038474401-1485915456325.jpg', 
              'http://static.ilike.com.vn:8880/uploads/2018/07/aec223b9gy1ftbwiusstij21ev1evtxh-1532686944437811952872.jpg',
              'https://znews-photo-td.zadn.vn/w1024/Uploaded/kcwvouvs/2017_09_15/20729587_877826279043507_3679078010070318122_n.jpg',
              'http://media.tinmoi.vn/2013/10/21/nu-sinh-duoc-ton-vinh-nu-than-1.jpg',
              'https://anh.eva.vn//upload/1-2016/images/2016-03-22/1622059_1671230623141576_7013179149578667299_n-1458611822-width960height960.jpg',
              '../static/image/hotgirl.jpg',
              '../static/image/hotbao.jpg']

for image_link in image_list:

    description_list = sample(["ngoan hiền", "dễ thương", "năng động", "lễ phép với bề trên", "nhạy cảm", "hài hước", "thân thiện", "yêu động vật", "ưa mạo hiểm"], 3)
    measurement_list = [randint(80,90), randint(50,70), randint(80,100)]
    
    new_service = Service(
        name=fake.name(),
        yob= randint(1990,2000),
        gender=randint(0,1),
        height=randint(150,190),
        phone=fake.phone_number(),
        address=fake.address(),
        status=choice([True, False]),
        description= "{0}, {1}, {2}.".format(*description_list),
        measurements= "{0} - {1} - {2}".format(*measurement_list),
        image= image_link
    )

    new_service.save()