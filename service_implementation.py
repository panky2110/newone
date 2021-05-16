from contact_book.service import ContactService
from contact_book.config import db
from contact_book.models import Contact

class ContactServiceImpl(ContactService):

    def __init__(self):
        db.create_all()

    def add_contact(self,contact):
        db.session.add(contact)
        db.session.commit()
        return "Record added succussfuly"

    def update_contact(self, dbcontact, contact):
        dbcontact.cname = contact.cname
        dbcontact.cmail = contact.cmail
        dbcontact.cphone = contact.cphone
        dbcontact.caddress = contact.caddress

    def get_contact(self, cid):
        return Contact.query.filter_by(cid=cid).first()

    def get_all_contact(self):
        return Contact.query.all()

    def delete_contact(self, cid):
        dbcontact = self.get_contact(cid)
        if dbcontact:
            db.session.delete(dbcontact)
            db.session.commit()
            return 'record deleted'
        return "No record with given id"

    def get_contact_byname(self, cname):
        return Contact.query.filter_by(cname=cname).first()

    def get_contact_bymail(self, cmail):
        return Contact.query.filter_by(cmail=cmail).first()