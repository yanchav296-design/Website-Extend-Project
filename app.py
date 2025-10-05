from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for chosen game
chosen_game = {}

# Temporary storage for comments by game
previous_comments = {
    "Valorant": [],
    "Rainbow Six Siege": [],
    "CS:GO": []
}

@app.route('/')
def index():
    return redirect(url_for('pick_game'))

# ----------------------
# PICK GAME PAGE
# ----------------------
@app.route('/pickGame', methods=['GET', 'POST'])
def pick_game():
    error = None
    if request.method == 'POST':
        selected_game = request.form.get('game_choice', '').strip()
        if not selected_game:
            error = "Please pick a game."
            return render_template('carsonForm.html', error=error)
        chosen_game['game'] = selected_game
        return redirect(url_for('chaoForm'))
    return render_template('carsonForm.html', error=error)

# ----------------------
# SHOW SELECTED GAME
# ----------------------
@app.route('/chaoForm')
def chaoForm():
    current_game = chosen_game.get("game")
    if not current_game:
        return redirect(url_for('pick_game'))
    return render_template(
        'chaoForm.html',
        game=current_game
    )

# ----------------------
# COMMENTS PAGE (ericForm)
# ----------------------
@app.route('/addComments', methods=['GET', 'POST'])
def addComments():
    current_game = chosen_game.get("game")
    if not current_game:
        return redirect(url_for('pick_game'))

    error = None
    name = ""
    comment = ""
    rating = 0

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        comment = request.form.get('comments', '').strip()
        rating = int(request.form.get('rating', 0))

        if not comment:
            error = "Please enter a comment"
        else:
            previous_comments[current_game].append({
                "name": name or "Anonymous",
                "comment": comment,
                "rating": rating
            })
            # Reset form after submission
            name = ""
            comment = ""
            rating = 0

    return render_template(
        'ericForm.html',
        current_game=current_game,
        previous_comments=previous_comments[current_game],
        error=error,
        name=name,
        comment=comment,
        rating=rating
    )

if __name__ == '__main__':
    app.run(debug=True)






