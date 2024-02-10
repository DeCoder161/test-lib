import requests


def f(url: str):
    r = requests.get(url)
    print(r)
