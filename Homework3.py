from flask import Flask,request
import csv
from faker import Faker
import requests
import json
from  webargs import fields,validate
from webargs.flaskparser import use_args,use_kwargs


app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello World!!!<p>"


@app.route("/hello")
def hello_anton():
    return "<p>Hello Anton<p>"

@app.route("/range")
@use_kwargs(
    {
    "count":fields.Int(
        missing=10,
        validate=[validate.Range(min=1,max=1000)]
        )
    },
    location='query'
)
def generate_students(count):
    faker = Faker()
    with open('students.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('first_name','last_name','email','password','birthday'))
    for i in range(count):
        with open('students.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow((faker.first_name(),faker.last_name(),faker.email(),faker.password(),faker.date_of_birth()))

    with open('students.csv', 'r') as file:
        a = ''
        for i in file.readlines():
            a+=i
            a+= '</br>'
        return a


@app.route("/bitcoin")
@use_kwargs(
    {
    "currency": fields.Str(
        missing='USD'
        ),
    "count":fields.Int(
        missing=1,
        validate=[validate.Range(min=1,max=1000)]
    )
    },
    location='query'
)
def get_bitcoin_value(currency,count):
    resource_url = 'https://test.bitpay.com/currencies'
    headers = {'X-Accept-Version': '2.0.0', 'Content-type': 'application/json'}
    response_symbol = requests.get(url=resource_url, headers=headers).content
    a = response_symbol.decode(json.detect_encoding(response_symbol))
    data_symbol = json.loads(a)
    for i in data_symbol.values():
        for y in i:
            if y['code'] == currency.upper():
                symbol = y['symbol']
    repsonse = requests.get('https://bitpay.com/api/rates')
    data = repsonse.json()
    for i in data:
        if currency.upper() in i.values():
            return str(i['rate']*count) + str(symbol) + ' = '+str(count) +'bitcoin'
    return 'Wrong format'



app.run(port=5001,debug=True)
