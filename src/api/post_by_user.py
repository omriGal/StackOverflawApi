import requests
import json

STACKOVERFLOW_URL = "http://api.stackexchange.com/2.2/users/"
POSTS_URL_SUFFIX = "/posts"

def get_post_by_id():

    user_id = "3729523"
    full_url = STACKOVERFLOW_URL + user_id + POSTS_URL_SUFFIX

    #debug
    print full_url

    param = {"site": "stackoverflow"}
    g = requests.get(full_url, params=param)

    #debug
    print g.url
    print g.status_code
    print g.text

    json_response = json.loads(g.text)

    #debug
    print json_response
    print len(json_response["items"])

    my_response = "<html> " \
                  "<body> "
    for item in json_response["items"]:
        my_response += '<a href="' + item["link"] + '">' + item["link"] + '</a>'
    my_response += "</body> </html>"

    print my_response


get_post_by_id()




