import requests


def main():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    # Замените DEMO_KEY ниже своим собственным ключом, если вы его сгенерировали.
    api_key = "aZ28VGAAOqeFzkx3Df9KcwDkuXFw5624VSZCngxT"
    params = {"api_key": api_key, "earth_date": "2020-07-01"}
    response = requests.get(url, params=params)
    if responce.status_code == 200:
        print(response)


main()
