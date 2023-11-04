# app.py

from flask import Flask, render_template, request
# from flask_assets import Bundle, Environment
import logging
import pyorient, pyorient.ogm

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitIdea', methods=['POST'])
def submitIdea():
    idea = {
            'file' : request.files['file'],
            'notes' : request.form['notes'],
            'tagsList' : request.form['taglist']
        }

    #TODO: Create backend to push data to after capture

    # Process the file and text here
    app.logger.info(idea)

    result = 'Form submitted successfully!'

    return result

if __name__ == '__main__':
    app.run(debug=True)
