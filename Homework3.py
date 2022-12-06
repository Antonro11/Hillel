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
    return "<p>Hello World!<p>"

@app.route("/students")
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
    students_lst = [('first_name','last_name','email','password','birthday')]
    for i in range(count):
        students_lst.append((faker.first_name(),faker.last_name(),faker.email(),faker.password(),faker.date_of_birth()))
    with open('students.csv', 'w') as file:
        writer = csv.writer(file)
        for row in students_lst:
            writer.writerow(row)
    with open('students.csv', 'r') as file:
        result_str = ''
        for i in file.readlines():
            result_str += i + '</br>'
        return result_str



@app.route("/bitcoin")
@use_kwargs(
    {
    "currency": fields.Str(
        missing='USD',
        validate=validate.Regexp('[A-Z]')
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
    response_currencies = response_symbol.decode(json.detect_encoding(response_symbol))
    currency_info = json.loads(response_currencies)
    for dict_info in currency_info.values():
        for key in dict_info:
            if key['code'] == currency:
                symbol = key['symbol']
    resource_url_rates = 'https://bitpay.com/rates/BTC/' + str(currency)
    headers = {'X-Accept-Version': '2.0.0', 'Content-type': 'application/json'}
    response_rates = requests.get(url=resource_url_rates, headers=headers).content
    response_rates = json.loads(response_rates)

    return str(round(count * (response_rates['data']['rate']), 2)) + symbol + ' = ' + str(count) + 'Bitcoin'




app.run(port=5001,debug=True)
