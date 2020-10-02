"""
Task: Get all movies which has the 'substr' in their title, and then sort them by alphabetic order
"""

import urllib.request
import json


def get_json_from_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    json_data = json.loads(html)
    return json_data


def get_all_titles(substr):
    url_base = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={substr}&page="

    data = get_json_from_url(url_base)

    total_pages = data["total_pages"]

    titles = []

    for i in range(1, total_pages + 1):
        url = url_base + str(i)
        data = get_json_from_url(url)
        for movie_object in data["data"]:
            titles.append(movie_object["Title"])
    titles.sort()
    return titles


print(get_all_titles("spiderman"))
