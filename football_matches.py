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

def incrementGoals(total_pages, url_base, home):
  score = 0
  for i in range(1, total_pages+1):
    try:
      url = url_base + str(i)
      data = get_json_from_url(url)
      for goals in data["data"]:
        if home is True:
          score += int(goals["team1goals"])
        else:
          score += int(goals["team2goals"])
    except:
      pass
  return score

def getGoals(team, year, playsAtHome):
  teamNum = "team1"
  atHome = True

  if playsAtHome == "team2":
    teamNum = "team2"
    atHome = False

  url_base = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&{teamNum}={team}&page="

  url = url_base + str(1)
  data = get_json_from_url(url)
  total_pages = data["total_pages"]

  return incrementGoals(total_pages, url_base, atHome)

def get_goals_by_team_in_a_given_year(team, year):
  score1 = getGoals(team, year, "team1")
  score2 = getGoals(team, year, "team2")
  return score1 + score2

print(get_goals_by_team_in_a_given_year("Barcelona", "2011"))
