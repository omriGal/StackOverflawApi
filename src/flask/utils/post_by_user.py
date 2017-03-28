import requests
import json

STACKOVERFLOW_URL = "http://api.stackexchange.com/2.2/"
POSTS_URL_SUFFIX = "/posts"


def get_post_by_id(user_id):
    full_url = STACKOVERFLOW_URL + "users/" + user_id + POSTS_URL_SUFFIX

    param = {"site": "stackoverflow"}
    response = requests.get(full_url, params=param)
    if response:
        json_response = json.loads(response.text)

        user_posts = []
        for item in json_response["items"]:
            user_posts.append(item["link"])

        if json_response["has_more"]: flag = True
        else: flag = False

        return user_posts, flag
    return None

# def get_post_by_access_token():
#     full_url = STACKOVERFLOW_URL + "me/posts" + POSTS_URL_SUFFIX
#
#     param = {"site": "stackoverflow"}
#     response = requests.get(full_url, params=param)
#     if response:
#         json_response = json.loads(response.text)
#
#         user_posts = []
#         for item in json_response["items"]:
#             user_posts.append(item["link"])
#
#         if json_response["has_more"]: flag = True
#         else: flag = False
#
#         return user_posts, flag
#     return None
