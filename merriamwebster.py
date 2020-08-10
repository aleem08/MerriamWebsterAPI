import requests, urllib.request, json

word = input("Word:")

url = 'https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=b1bbdd97-858c-412d-9520-8037b000cf6d'
response = requests.get(url)
jsonStruct = response.json()
definition = jsonStruct[0]['def'][0]['sseq'][0][0][1]['dt'][0][1][4:]

print(definition)