from flask import Flask, render_template, request, session
from flask import url_for
from flask_oauth import OAuth

from src.flask.utils.post_by_user import get_post_by_id

OAUTH_DIALOG_URL = 'https://stackexchange.com/oauth/dialog'
CLIENT_ID = '9285'
CLIENT_SECRET = 'k*EAoyC995EOOW*Tv0i3Bg(('
REDIRECT_URI = 'https://stackexchange.com/oauth/login_success'
SCOPE = 'no_expiry'

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'F34TF$($e34D';

oauth = OAuth()
stackExchange = oauth.remote_app('stackexchange',
                                 base_url='https://api.stackexchange.com/2.2',
                                 request_token_url=None,
                                 access_token_url='/oauth/access_token',
                                 authorize_url='https://stackexchange.com/oauth/dialog',
                                 consumer_key=CLIENT_ID,
                                 consumer_secret=CLIENT_SECRET,
                                 request_token_params={'scope': 'no_expiry'})


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/user/posts', methods=['GET'])
def get_user_posts():
    session['user_id'] = request.values["user_id"]
    posts, has_more = get_post_by_id(session['user_id'])
    return render_template('myPosts.html', user_id=session["user_id"], posts=posts, more=has_more)


@app.route('/auth', methods=['GET'])
def get_auth():
    return stackExchange.authorize(callback=url_for('stackExchange_authorized',
                                                    next=request.args.get('next') or request.referrer or None, _external=True))


@app.route('/login/authorized')
@stackExchange.authorized_handler
def stackExchange_authorized(response):
    if response is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    session['access_token'] = (response['access_token'], '')
    me = stackExchange.get('me/posts')
    return render_template('myPosts.html', user_id="By-auth", posts=me, more=me)

@stackExchange.tokengetter
def get_stackExchange_oauth_token():
    return session.get('access_token')


if __name__ == "__main__":
    app.run()
