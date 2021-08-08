import json

import requests


def search_info():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Authorization': '563492ad6f91700001000001786b9e4bb4bb4b74900164d6c9818e47'
    }
    search = input('Введіть що саме ви шукаету:-') # наприклад opossum or other animals or fish
    page = int(input('Введіть сторінку по якій вести пошук:-'))  # коректно не працюе
    web_url = f"https://api.pexels.com/v1/search?query={search}&per_page={page}"
    responce = requests.get(web_url, headers=headers)
    if responce.status_code == 200:
        res = responce.json()['photos'][0]['url']
        with open('animals_1.json', 'w', encoding='utf-8') as file_json:
            json.dump(res, file_json, ensure_ascii=False, indent=4)




search_info()
