import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Authorization': '563492ad6f91700001000001786b9e4bb4bb4b74900164d6c9818e47'
}


def search_info():

    search = input('Введіть що саме ви шукаету:-')  # наприклад opossum or other animals or fish
    page = int(input('Введіть сторінку по якій вести пошук:-'))  # коректно не працюе
    web_url = f"https://api.pexels.com/v1/search?query={search}&per_page={page}"
    responce = requests.get(url=web_url, headers=headers)
    if responce.status_code == 200:
        # res = responce.json()['photos'][0]['url']
        with open('animals_2.json', 'w', encoding='utf-8') as file_json:
            json.dump(responce.json(), file_json, ensure_ascii=False, indent=4)

    with open('animals_2.json', 'r', encoding='utf-8') as file_json:
        text = json.load(file_json)

        for txt in text['photos']:
            print(txt['url'])





search_info()
