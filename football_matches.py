"""
Task: Calculate the sum of the goals, that 'team' scores in a given 'year' 
"""

import urllib.request
import json


def get_json_from_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    json_data = json.loads(html)
    return json_data


def get_score_by_team_in_a_given_year(team, year):
    url_base = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page="

    url = url_base + str(1)
    data = get_json_from_url(url)

    total_pages = data["total_pages"]

    score = 0

    for i in range(total_pages):
        url = url_base + str(i)
        data = get_json_from_url(url)
        for goals in data["data"]:
            score += int(goals["team1goals"])
    return score


print(get_score_by_team_in_a_given_year("Barcelona", "2011"))
