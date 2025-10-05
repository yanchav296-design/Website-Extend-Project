from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('profile'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        game = request.form.get('favorite_game', '').strip()

        # Validation
        if not name or not age or not game:
            error = "Please fill in all required fields"
            return render_template('carsonForm.html', error=error)

        return render_template('chaoForm.html', name=name, age=age, game=game, )

    return render_template('carsonForm.html')


@app.route('/addComments', methods=['GET', 'POST'])
def addComments():
    if request.method == 'POST':
        comment = request.form.get('comments', '').strip()
        if not comment:
            error = "Please enter a comment"
            return render_template('chaoForm.html', error=error)

    return render_template('ericForm.html', comment=comment)
