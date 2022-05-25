#!/usr/bin/python3

import requests

hockey = requests.get("https://statsapi.web.nhl.com/api/v1/teams").json()


for i in hockey["teams"]:
    print (i["teamName"])
    print (i["officialSiteUrl"])
    print (i["division"]["name"])
    print (i["venue"]["timeZone"]["tz"])
    print ()
