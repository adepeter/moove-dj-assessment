import requests


def get_country(country_name):
    response = requests.get('https://restcountries.com/v2/name/%(country)s?fullText=true' % {'country': country_name})
    return isinstance(response.json(), list)
