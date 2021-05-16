from flask import request,jsonify
from contact_book.config import db,app
from contact_book.service_implementation import ContactServiceImpl
from contact_book.models import Contact,User

import json
# from restapi.contactinfo import Contact
service = ContactServiceImpl()

@app.route('/contact' ,methods = ['GET'])
def get_all_contact():
    contacts = service.get_all_contact()
    contact_list = []
    if contacts:
        for contact in contacts:
            contact = contact.__dict__
            contact_dict = { 'cid' : contact.get('cid'),
                             'cname' : contact.get('cname'),
                             'cphone' : contact.get('cphone'),
                             'caddress' : contact.get('caddress')}
            contact_list.append(contact_dict)
    return json.dumps(contact_list)

@app.route('/add' ,methods = ['POST'])
def add_contact():
    jsondata = request.get_json()
    if jsondata:
        if jsondata.get('cname') and jsondata.get('cmail') and jsondata.get('cphone') and jsondata.get('caddress'):
            cname = jsondata.get('cname')
            cmail = jsondata.get('cmail')
            dummy1 = service.get_contact_byname(cname)
            dummy2 = service.get_contact_bymail(cmail)

            if dummy1 and dummy2:
                return json.dumps({"Error" : "Contact Already Present"})
            else:
                contact = Contact(cname= jsondata.get('cname'),cmail=jsondata.get('cmail'),
                          cphone=jsondata.get('cphone'),caddress=jsondata.get('caddress'))
                service.add_contact(contact)
                return json.dumps({"succuss" : "Record Inserted Succussfuly"})
        else:
            return json.dumps({"error " : "Mandatory Fields cname,cmail,cphone,caddress are not given"})

    return json.dumps({"error " : "Empty Data Not Allowed"})

@app.route('/update/<int:cid>' ,methods = ['PUT'])
def update_contact(cid):
    contact = service.get_contact_byname(cid)
    if contact:
        jsondata=request.get_json()
        if jsondata:
            if jsondata.get('cname') and jsondata.get('cmail') and jsondata.get('cphone') and jsondata.get('caddress'):
                dbcontact = Contact(cname=jsondata.get('cname'), cmail=jsondata.get('cmail'),
                                  cphone=jsondata.get('cphone'), caddress=jsondata.get('caddress'))
                service.update_contact(dbcontact,contact)
                return json.dumps({"succuss": "Record Updated Succussfuly"})
            return json.dumps({"error ": "Mandatory Fields cname,cmail,cphone,caddress are not given"})
        return json.dumps({"Error " : "Empty Data Not Allowed"})
    return json.dumps({"Error"  : f"Contact {cid} Not Present"})

@app.route('/delete/<int:cid>' ,methods = ['DELETE'])
def delete_contact(cid):
    contact = service.get_contact_byname(cid)
    if contact:
        jsondata=request.get_json()
        if jsondata:
            if jsondata.get('cname') and jsondata.get('cmail') and jsondata.get('cphone') and jsondata.get('caddress'):
                service.delete_contact(cid)
                return json.dumps({"succuss": "Record Deleted Succussfuly"})
            return json.dumps({"error ": "Mandatory Fields cname,cmail,cphone,caddress are not given"})
        return json.dumps({"Error " : "Empty Data Not Allowed"})
    return json.dumps({"Error"  : f"Contact ID {cid} Not Present"})

@app.route('/auth' ,methods = ['GET'])
def base_auth():
    if request.authorization:
        if request.authorization.username and request.authorization.password:
            username = request.authorization.username
            password = request.authorization.password
            user = User.query.filter_by(username=username).first()
            if user:
                if user.password == password:
                    return json.dumps({"succuss": "User Logged in succussfuly"})
                return ({"Error ": "Password is incorrect"})
            return ({"Error ": f"Username {username} is Not Present"})
        return json.dumps({"Error": "Empty Field "})
    return json.dumps({"Error": "Not a Authorization Request "})


@app.route('/contact/mail/<cnmail>', methods=['GET'])
def contact_bymail(cmail):
    contact = service.get_contact_bymail(cmail)
    contact_dict = {}
    if contact:
        contact = contact.__dict__
        contact_dict = {'cid': contact.get('cid'),
                        'cname': contact.get('cname'),
                        'cphone': contact.get('cphone'),
                        'caddress': contact.get('caddress')}

@app.route('/contact/name/<cname>' ,methods = ['GET'])
def contact_byname(cname):
    contact = service.get_contact_byname(cname)
    contact_dict = {}
    if contact:
        contact = contact.__dict__
        contact_dict = {'cid': contact.get('cid'),
                        'cname': contact.get('cname'),
                        'cphone': contact.get('cphone'),
                        'caddress': contact.get('caddress')}
        return json.dumps(contact_dict)
    return json.dumps({"Error" :f"Contact with {cname} not found"})

@app.route('/contact/')
def show_contacts():
    return jsonify(get_list(klass = Contact,url = '/contact/',
                                      start=request.args.get('start', 1),
                                      limit=request.args.get('limit', 10)))

def serialiaze(contact):
    contacts = contact.query.all()
    contact_list = []
    if contacts:
        for contact in contacts:
            contact = contact.__dict__
            contact_dict = {'cid': contact.get('cid'),
                            'cname': contact.get('cname'),
                            'cphone': contact.get('cphone'),
                            'caddress': contact.get('caddress')}
            contact_list.append(contact_dict)
    return contact_list

def get_list(klass,url, start, limit):
    # check if page exists

    results = serialiaze(klass)
    print(results)
    count = len(results)
    if not results:
        return json.dumps({"Error" : "No data Available"})
    # make response
    dict_page = {}
    dict_page['start'] = start
    dict_page['limit'] = limit
    dict_page['count'] = count
    if start == 1:
        dict_page['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        dict_page['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        dict_page['next'] = ''
    else:
        start_copy = start + limit
        dict_page['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    dict_page['results'] = results[(start - 1):(start - 1 + limit)]
    print(dict_page)
    return dict_page

if __name__ == '__main__':
    app.run(debug=True)