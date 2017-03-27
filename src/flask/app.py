from flask import Flask, render_template, request, session, redirect
from pprint import pprint

from requests_oauthlib import OAuth2Session

from src.flask.post_by_user import get_post_by_id

OAUTH_DIALOG_URL = 'https://stackexchange.com/oauth/dialog'
CLIENT_ID = '9285'
CLIENT_SECRET = 'k*EAoyC995EOOW*Tv0i3Bg(('
REDIRECT_URI = 'https://stackexchange.com/oauth/login_success'
SCOPE = 'no_expiry'

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'F34TF$($e34D';


@app.route("/")
def home():
    return render_template('home.html')


# @app.route('/myPosts', methods=['GET', 'POST'])
# def my_posts():
#     session['user_id'] = request.form['user_id']
#     if request.form['action'] == 'Get my posts with auth':
#         oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
#         # todo: dubug
#         pprint(vars(oauth))
#         authorization_url, state = oauth.authorization_url(OAUTH_DIALOG_URL)
#         # todo: debug
#         print(authorization_url)
#     return get_post_by_id(session['user_id'])

# @app.route('/users/<user_id>/posts', methods=['GET'])

@app.route('/user/posts', methods=['GET'])
def get_user_posts():
    session['user_id'] = request.values["user_id"]
    posts, has_more = get_post_by_id(session['user_id'])
    return render_template('myPosts.html', user_id=session["user_id"], posts=posts, more=has_more)


@app.route('/user/post/auth', methods=['GET'])
def get_user_posts_with_auth():
    # oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    # authorization_url, state = oauth.authorization_url(OAUTH_DIALOG_URL)
    # request
    # posts = get_post_by_id(session['user_id'])
    # return render_template('my_posts.html', session['user_id'], posts)
    print "hi!!"


# users/:userId/posts

# myPosts

if __name__ == "__main__":
    app.run()
