import requests

token = "paste token here"  #Line access tokens
url = 'https://notify-api.line.me/api/notify'


def line_text(message):
    data = {'message': message}
    headers = {'Authorization': 'Bearer ' + token}
    session = requests.Session()
    session_post = session.post(url, headers=headers, data=data)
    print(session_post.text)


def line_pic(message, path_file):
    image_file = {'imageFile': open(path_file, 'rb')}
    data = ({'message': message})
    headers = {'Authorization': 'Bearer ' + token}
    session = requests.Session()
    session_post = session.post(url, headers=headers, files=image_file, data=data)
    print(session_post.text)


line_pic("Alert", "picture.jpg")
