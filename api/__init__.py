import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Authorization': '563492ad6f91700001000001786b9e4bb4bb4b74900164d6c9818e47'
}

def serch_info():
    serch = input('Введіть що саме ви шукаету')
    web_url = f"https://api.pexels.com/v1/search?query={serch}&per_page=1"
    responce = get.web_url

