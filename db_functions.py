from config import server_host, server_port
import requests


def server_connect(link='/'):
    return f"{server_host}:{server_port}{link}"


def categories_all():
    return requests.get(server_connect('/categories')).json()


def find_category(name):
    return requests.get(server_connect(f'/category/{name}')).json()[0][0]


def register_user(user_id):
    return requests.get(server_connect(f'/register/{user_id}')).json()


def subscribe(user_id, category_id):
    return requests.get(server_connect(f'/sub/{user_id}/{category_id}')).json()


def unsubscribe(user_id, category_id):
    return requests.get(server_connect(f'/unsub/{user_id}/{category_id}')).json()


def user_subscribes(user_id):
    return requests.get(server_connect(f'/subs/{user_id}')).json()


def fetch_news(category):
    return requests.get(server_connect(f'/get_news/{category}')).json()
