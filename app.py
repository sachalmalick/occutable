import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
	return "hi"

@app.route("/pg2")
def pagethree():
    return ''''''

def listify(filename):
    tmp = 0
    L=[]
    lfile = open(filename, 'r').readlines()
    for row in lfile:
        sl = row.replace('"', '').replace('\n', '').split(",",2)
        L.append(sl[0])
        L.append(sl[1])
        L.append(sl[2])
    return L

def listoflist(filename):
    tmp = 0
    L=[]
    lfile = open(filename, 'r').readlines()
    for row in lfile:
        sl = row.replace('"', '').replace('\n', '').split(",",2)
        L.append(sl)
    return L

def percentlist(filename):
    L=[]
    tmp = 0
    origlist = listoflist('occupations.csv')
    for row in origlist:
        num = int(10 * float(row[1]))# get percentage
        start = tmp
        tmp = num + start
        L.append([start, tmp, row[0]])
    return L

def dicify(filename):
    tmp = 0
    d={}
    occu = listoflist('occupations.csv')
    for row in occu:
        d[row[0]] = [row[1],row[2]]
    return d

def chooser():
    rand = int(random.random() * 1000)
    L = percentlist('occupations.csv')
    for row in L:
        if rand > row[0] and rand < row[1]:
            return row[2]


@app.route("/occupations")
def pagetwo():
    return render_template("sample.html",chosen = chooser(),occu = dicify("occupations.csv") )

if __name__=="__main__":
    app.run(debug = True)

