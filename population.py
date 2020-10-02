"""
Task: Count the countries which has 's' in their name, and has a higher population than 'p'
"""

import urllib.request
import json


def get_json_from_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    json_data = json.loads(html)
    return json_data


def getCountries(s, p):
    url_base = f"https://jsonmock.hackerrank.com/api/countries/search?name={s}&page="

    data = get_json_from_url(url_base)

    total_pages = data["total_pages"]

    score = 0

    for i in range(1, total_pages + 1):
        url = url_base + str(i)
        data = get_json_from_url(url)
        for countries in data["data"]:
            if countries["population"] > p:
                score += 1
    return score


print(getCountries('co', 500))
