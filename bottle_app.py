from bottle import default_app, route, post, template

#Import sqlite3 to w0
import sqlite3

gpaDB = sqlite3.connect("gpa.db")
gpaC = gpaDB.cursor()

# Keeping default homepage
@route('/')
def hello_world():
    return 'Hello from Bottle!'

#Landing page and menu for GPA calculations webapp
@route('/gpa')
def gpa_home():
    return template("gpahome.html")

#New user form entry for GPA calculations webapp
@route('/gpa/classinformation')
def class_information():
    return template("gpaclassinformation.html")

#New user results for GPA calculations webapp
@post('/gpa/results')
def gpa_results():
    return template("gparesults.html", c = gpaC, db = gpaDB)

#Returning user login page for GPA calculations webapp
@route('/gpa/login')
def login():
    return template("gpalogin.html")

#Returning user information update page for GPA calculations webapp
@post('/gpa/login/classinformation')
def login_classinformation():
    return template("gpaloginclassinformation.html", c = gpaC)

#Returning user results page for GPA calculatons webapp
@post('/gpa/login/results')
def login_results():
    return template("gpaloginresults.html", c = gpaC, db = gpaDB)

application = default_app()