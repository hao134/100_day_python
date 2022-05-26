from model import db, User

# firstly create model, uncomment next line
# db.create_all()

admin = User('admin', 'admin@abc.com')
user1 = User('user1', 'user1@abc.com')
# 寫入資料
db.session.add(admin)
db.session.add(user1)
db.session.commit()
