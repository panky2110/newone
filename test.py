
from flask import Flask, request, jsonify
app = Flask(__name__)

from flask import json
from contact_book.controller import *

def test_add():
    response = app.test_client().post(
        '/add',
        data=json.dumps({'cid': 1, 'cname': 'pankaj','cphpne':'86678765','cmail':'pankaj@gmail.com','caddress':'pune'}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['added'] == 'sucessfully'