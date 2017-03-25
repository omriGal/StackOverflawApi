from flask import Flask, render_template

from src.flask.post_by_user import get_post_by_id

app = Flask(__name__ ,template_folder='../templates')

@app.route("/")
def main():
    return render_template('home.html')

@app.route('/myPosts')
def myPosts():
    # return render_template('myPosts.html')
    return get_post_by_id()

if __name__ == "__main__":
    app.run()
