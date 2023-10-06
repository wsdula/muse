# app.py

from flask import Flask, render_template, request
from flask_assets import Bundle, Environment

from todos import todos

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
def homepage():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_todo():
    search_term = request.form.get("search")

    if not len(search_term):
        return render_template("todo.html", todos=[])

    res_todos = []
    for todo in todos:
        if search_term in todo["title"]:
            res_todos.append(todo)

    return render_template("todo.html", todos=res_todos)

if __name__ == "__main__":
    app.run(debug=True)
