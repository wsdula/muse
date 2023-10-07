# app.py

from flask import Flask, render_template, request, jsonify
from flask_assets import Bundle, Environment


app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
js = Bundle("src/*.js", output="dist/main.js")

assets.register("css", css)
assets.register("js", js)
css.build()
js.build()


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/addIdea', methods=['POST'])
def addIdea():
    file = request.files['file']
    text = request.form['notes']

    # Process the file and text here

    result = "Form submitted successfully!"

    return result

if __name__ == "__main__":
    app.run(debug=True)
