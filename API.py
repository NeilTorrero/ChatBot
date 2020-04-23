import requests

BASE_URL = 'http://www.dnd5eapi.co'

def getInfoAPI(type, name):
    url = BASE_URL + '/api/' + type + '/' + name + '/'
    response = requests.get(url)
    data = response.json()
    print(data)
    print(data['name'])
    print(data['level'])
    print(data['range'])
    print(data['desc'])
    return data
