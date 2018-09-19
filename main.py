from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

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
        <form action="/rotate" method="post">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value="0"/>
            <textarea name="text">{0}</textarea>
            <input type="submit" />
            
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/rotate", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    text_rot = rotate_string(text, rot)
    return form.format(text_rot)

app.run()