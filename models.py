from contact_book.config import db

class User(db.Model):
    id = db.Column('aid',db.Integer(),primary_key=True)
    username = db.Column('username',db.String(100),unique=True)
    password = db.Column('password',db.String(100))

class Contact(db.Model):
    __tablename__ = 'Contact_Info'
    cid = db.Column('cid', db.Integer(), primary_key=True)
    cname = db.Column('cname', db.String(100), unique=True)
    cmail = db.Column('cmail', db.String(100), unique=True)
    cphone = db.Column('cphone', db.String(100))
    caddress = db.Column('caddress', db.String(100))


# if __name__ == '__main__':
"""
code add contacts
    # import random
    # NAME = ['Pankaj' , 'pankajchavan' , 'PANKAJ' , 'PANKAJCHAVAN']
    # ADDRESS = ["MUMBAI" , "PUNE" , "PCMC" , "NASHIK"]
    # for item in range(100):
    #     cname = NAME[random.randint(0,3)]+str(random.randint(1,1000))
    #     cmail = cname+'@gmail.com'
    #     cphone = '8087'+'907'+str(random.randint(100,999))
    #     caddress= ADDRESS[random.randint(0,3)]
    #     contact= Contact(cname = cname,
    #                      cmail = cmail,
    #                      cphone = cphone,
    #                      caddress = caddress)
    #     db.session.add(contact)
    #     db.session.commit()
"""

"""

Code to add User
user auth

user = User(username = 'username',password = password)
"""
