from flask import Flask, request, redirect
from caesar import rotate_string
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True


form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
                <label for="rot">Rotate By: </label>
                <input name="rot" type="text" value="{0}" />
                <textarea name="text" placeholder="Enter your text here...">{1}</textarea>
                <input type="submit" />
        </form>
    </body>
</html>

"""

@app.route("/", methods = ["POST"])
def encrypt():
    text = request.form["text"]
    rot = request.form["rot"]
    return form.format(rot,rotate_string(text, int(rot))) 

@app.route("/")
def index():
    return form.format(0,"")

app.run()