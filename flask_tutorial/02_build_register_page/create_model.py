#  我們先import設置的model
from model import User
from model import Contact
from model import db

# firstly
# #  增加一個使用者為admin
# user = User(username='admin',email='admin@abc.com')
# #  增加一個聯絡人
# contact = Contact(contact_style='mobile', contact_context='3345678')
# #  將聯絡人寫入使用者
# user.contacts.append(contact)
# #  將資料寫入
# db.session.add(user)
# db.session.commit()

# secondly
user = User(username='Cust', email='Cust@abc.com')
contact = Contact.query.filter_by(id=1).first()
user.contacts.append(contact)
db.session.add(user)
db.session.commit()
