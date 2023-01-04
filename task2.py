import json, requests



def comment_json():
    req = requests.get(url='https://api.pushshift.io/reddit/comment/search/')
    with open('pushshift.json', 'w') as file:
        json.dump(req.json(), file)


if __name__ == "__main__":
    comment_json()
