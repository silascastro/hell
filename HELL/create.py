from os import system

class create:
    def __init__(self):
        self.create_files()
    def create_files(self):
        ques = input('\n\033[0;33m[1] Basic app\n > A Simple website with one file\n[2] Basic app with Blueprint\n > A Simple website with blueprint\n\033[0;35mType it:\033[m')
        if ques == "1":
            self.one_file()
        elif ques == "2":
            self.blueprint()
    def blueprint(self):
        system('mkdir app/')
        system('mkdir app/home')
        f = open('app/home/views.py', 'w')
        f.write("""from . import home\nfrom flask import render_template

@home.route('/')
def homepage():
    return render_template('home.html')
# Hell
""")  
        f.close()
        system('mkdir app/templates')
        f = open('app/templates/home.html', 'w')
        f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hell</title>
</head>
<body>
    <h1>Hell</h1>
</body>
</html>       
""")

        f = open('app/home/__init__.py', 'w')
        f.write("""from flask import Blueprint\n
home = Blueprint('home', __name__)

from . import views

# Hell
""")  
        f.close()

        f = open('app/run.py', 'w')
        f.write("""from flask import Flask\nfrom home import home\n
app = Flask(__name__)
app.register_blueprint(home)

app.run(debug=True)

# Hell
""")  
        f.close()

    def one_file(self):
        system('mkdir app')
        f = open('app/main.py', 'w')
        f.write("""from flask import Flask\n
app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Hell</h1>'

app.run(debug=True)

# Hell
""")  
        f.close()