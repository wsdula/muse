# app.py

from flask import Flask, render_template, request, jsonify
# from flask_assets import Bundle, Environment
import logging

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

tagsList = []

@app.route('/')
def index():
    tagsList = []
    return render_template('index.html')

@app.route('/tags', methods=['POST','DELETE'])
def tags():
    if request.method == 'DELETE':
        tagText = request.form['tag']
        app.logger.info(tagText)

        tagsList.remove(tagText)
        logtext = tagText + " has been removed from list: " + str(tagsList)
        app.logger.info(logtext)
        result = ''
    else:
        #Take in a tag, trim it, then push it back in it's respective html element
        tagText = request.form['hashtags'].strip().lower()
        result = '''<div id=tag class="m-2 w-auto font-medium text-sm pointer-events-auto bg-[#242424] text-white p-2.5 text-center rounded-3xl cursor-pointer hover:bg-gray-600" hx-delete="/tags" hx-target="this" hx-on::after-request="this.remove()">'''+tagText+'</div>'

        tagsList.append(str(tagText))
        logtext = tagText + " has been added to list: " + str(tagsList)
        app.logger.info(logtext)

    return result


@app.route('/submitIdea', methods=['POST'])
def submitIdea():
    # file = request.files['file']
    # text = request.form['notes']

    a = jsonify(request.form['hashtags'])

    # Process the file and text here

    result = 'Form submitted successfully!'

    return a

if __name__ == '__main__':
    app.run(debug=True)
