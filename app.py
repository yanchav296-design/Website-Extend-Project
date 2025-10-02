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

        return render_template(
            'chaoForm.html',
            name=name,
            age=age,
            game=game,
        )

    return render_template('carsonForm.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        rating = request.form.get('rating', '').strip()
        feedback = request.form.get('feedback', '').strip()

        # Validation
        if not rating:
            errorMsg = "Please provide a rating"
            return render_template('feedbackForm.html', error=errorMsg)

        return render_template(
            'feedbackSuccess.html',
            rating=rating,
            comments=feedback
        )

    return render_template('feedbackForm.html')
