from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime


def formatDate(date):
    dt_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
    formatedDate = dt_obj.strftime("%m-%d-%Y")
    return formatedDate


def get_flavors():
    url = 'https://www.culvers.com/restaurants/grimes-ia-1st-st'

    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, 'html.parser')

    tag = soup.find("script", id="__NEXT_DATA__")

    html = tag

    data = json.loads(html.string)

    flavors = data["props"]["pageProps"]["page"]["customData"]["restaurantCalendar"]["flavors"]

    flavorsList = []

    for flavor in flavors:
        date = formatDate(flavor["onDate"])
        name = flavor["title"]
        description = flavor["description"]
        image = flavor["image"]["src"]

        newFlavor = {"date": date,
                     "name": name,
                     "description": description,
                     "image": image}
        flavorsList.append(newFlavor)

    return flavorsList
