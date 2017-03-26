from flask import Flask, render_template, request, session, redirect

from src.flask.post_by_user import get_post_by_id

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/myPosts', methods=['GET', 'POST'])
def my_posts():
    session['user_id'] = request.form['user_id']
    print session['user_id']
    return get_post_by_id(session['user_id'])


if __name__ == "__main__":    app.run()
