from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def home(request, id):
    response = requests.get("https://en.wikipedia.org/wiki/"+id)

    # scrape webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    country_name = soup.select_one('.firstHeading')
    country_info = country_name.find_next('span')
    country = country_info.get_text()

    capital_name = soup.select_one('.infobox-data')
    capital_info = capital_name.find_next('a')
    capital = capital_info.get_text()

    largest_city = soup.select_one('.plainlist')
    largest_info = largest_city.find_next('a')
    large = largest_info.get_text()

    official_lang = soup.select_one('.hlist')
    lang_info = official_lang.find_next('a')
    language = lang_info.get_text()

    return render(request, "country.html", {'country': country, 'capital': capital, 'large': large, 'language': language, })
