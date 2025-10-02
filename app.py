from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return redirect(url_for('carson'))

@app.route('/carson', methods=[])

def carson():
    return



