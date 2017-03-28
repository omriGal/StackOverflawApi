from flask_oauth import OAuth
from flask import Flask, render_template, request, session, redirect

from flask import url_for

from src.flask.post_by_user import get_post_by_id

OAUTH_DIALOG_URL = 'https://stackexchange.com/oauth/dialog'
CLIENT_ID = '9285'
CLIENT_SECRET = 'k*EAoyC995EOOW*Tv0i3Bg(('
REDIRECT_URI = 'https://stackexchange.com/oauth/login_success'
SCOPE = 'no_expiry'

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'F34TF$($e34D';

oauth = OAuth()
stackExchange = oauth.remote_app('stackexchange',
                                 base_url='https://stackexchange.com/',
                                 request_token_url=None,
                                 access_token_url='/oauth/access_token',
                                 authorize_url='https://stackexchange.com/oauth/dialog',
                                 consumer_key=CLIENT_ID,
                                 consumer_secret=CLIENT_SECRET,
                                 request_token_params={'scope': SCOPE})


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
    return stackExchange.authorize(callback=url_for('stackexchange_authorized',
                                                    access_token=request.args or request.referrer or None,
                                                    _external=True))


@app.route('/login/authorized')
@stackExchange.authorized_handler
def stackexchange_authorized(response):
    if response is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['access_token'] = (response['access_token'], '')
    # session['access_token'] = response(['access_token'])
    me = stackExchange.get('me/posts')
    print me
    return 'Logged in as id=%s name=%s redirect=%s' % \
           (me.data['id'], me.data['name'], request.args.get('access_token'))
    # return render_template('myPosts.html', user_id="hi", posts=me, more=me)


if __name__ == "__main__":
    app.run()
