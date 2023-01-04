import requests


def notes():
    req = requests.get(url='https://reddit-api.readthedocs.io/en/latest/')
    with open('robots.txt', 'w') as f:
        f.write(req.text)
    # print()



if __name__ == "__main__":
    notes()