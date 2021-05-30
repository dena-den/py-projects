import requests
import json

client_id = '6bda0d7ba90bb70eaeac'
client_secret = '14f48ab5ee7a1960eb22db7a6e9e8d42'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
dict = {}
with open('dataset_24476_4.txt') as f:
    for line in f:
        line = line.strip()
        #line='4e2ed576477cc70001006f99'
        r = requests.get("https://api.artsy.net/api/artists/{}".format(line), headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        dict[j['sortable_name']] = j['birthday']
    a = sorted(dict.items(), key=lambda x: (x[1], x[0]))
    print(a)
    for i in range(len(a)):
        print(a[i][0])