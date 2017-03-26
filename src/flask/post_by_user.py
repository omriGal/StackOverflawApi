import requests
import json

SUFFIX_RESPONSE_POST = "</ul></body> </html>"

PREFIX_RESPONSE_POST = "<html> " \
                       "<body> " \
                       "<h1>Stack Overflow posts by user_id:</h1>" \
                       "<ul style='list-style-type:circle'>"

STACKOVERFLOW_URL = "http://api.stackexchange.com/2.2/users/"
POSTS_URL_SUFFIX = "/posts"


def get_post_by_id(user_id):

    full_url = STACKOVERFLOW_URL + user_id + POSTS_URL_SUFFIX

    # debug
    print full_url

    param = {"site": "stackoverflow"}
    g = requests.get(full_url, params=param)

    # debug
    print g.url
    print g.status_code
    print g.text

    json_response = json.loads(g.text)

    # debug
    print json_response
    print len(json_response["items"])

    user_name = json_response["items"][0]['owner']['display_name']
    my_response = PREFIX_RESPONSE_POST
    my_response += '<h2> Links to ' + user_name + ' posts </h2>'

    for item in json_response["items"]:
        my_response += '<li><a href="' + item["link"] + '">' + item["link"] + '</a></li> <br>'

        #debug
        print my_response

    if json_response["has_more"]: my_response += '<h3> User has more posts</h3>'
    my_response += SUFFIX_RESPONSE_POST

    return my_response


