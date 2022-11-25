from flask import Flask
import random
import csv


app = Flask(__name__)


@app.route("/")
def hello_world():
    return  "<p>Hello World!!!<p>"


@app.route("/hello")
def hello_anton():
    return  "<p>Hello Anton<p>"

@app.route("/password")
def genetare_password():
    len_password = random.randint(10, 20)
    password_lst = []
    result = ''
    while len(password_lst) <= len_password:
        for_mess = random.randint(0, 11)
        if for_mess < 6:
            password_lst.append(chr(random.randint(32, 126)))
        else:
            password_lst.append(str(random.randint(0, 9)))
    random.shuffle(password_lst)
    for i in password_lst:
        result += i
    return result

@app.route("/avarage")
def calculate_average():
    with open('hw.csv') as file:
        reader = csv.reader(file)
        count = 0
        height = []
        weight = []
        for raw in reader:
            if count != 0:
                height.append(float(raw[1]))
                weight.append(float(raw[2]))
            count += 1
        return 'average high is: ' + str(round(sum(height)/len(height),2))+ ' inches, average weight is: ' + str(round(sum(weight)/len(weight),2))+' pounds'




app.run(port=5001,debug=True)
