import os
import requests
import bs4
import lxml
from datetime import date


JSONBLOB = os.environ.get('JSONBLOB')

# retriving the json data from jsonblob
def get_json():

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.get(
        JSONBLOB, headers=headers)
    return(response.json())


#pushing the updates to the jsonblob server file
def updating_server_json(updated_json):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    json_data = updated_json
    response = requests.put(
        JSONBLOB, headers=headers, json=json_data)


#if new updates are found the updating the json file which we have retrived from jsonblob
def updating_json(i, soup, notice_json):

    updates = []  # to store the updates

    for j in range(i-1, -1, -1):

        heading = soup.select('#menu2')[0].select('a')[j].getText()
        link = soup.select('#menu2')[0].select('a')[j]['href'].replace(
            "downloads/", "http://www.nitrr.ac.in/downloads/")

        temp = {
            'heading': f'{heading}',
            'link': f'{link}'
        }
        notice_json.insert(0, temp)
        updates.append(temp)
    updating_server_json(notice_json)
    return(updates)


#checks if there are some notices updates or not, if sound the return updates.json
#should be run in regular intervals to check updates
def for_notices():
    notice_json = get_json()
    response = requests.get("http://www.nitrr.ac.in/acad_downloads.php")
    soup = bs4.BeautifulSoup(response.text, "lxml")

    length = len(soup.select('#menu2')[0].select('a'))

    if(soup.select('#menu2')[0].select('a')[0].getText() == notice_json[0]['heading']):
        return []

    else:
        for i in range(length):
            heading = soup.select('#menu2')[0].select('a')[i].getText()
            if(heading == notice_json[0]['heading']):
                new_notices = updating_json(i, soup, notice_json)
                return(new_notices)
