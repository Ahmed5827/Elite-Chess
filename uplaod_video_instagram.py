from instagrapi import Client
from instabot import Bot
import json



def upload_insta(path, caption):
    f = open("client_config_insta.json")
    data = json.load(f)
    print(data)
    data = data["insta_credentials"][0]
    username = data["username"]
    password = data["password"]

    cl = Client()
    cl.login(username= username, password= password)
    print("Succesfully loged in!")
    cl.clip_upload(
        path = path,
        caption = caption,
    )
    print("Reel Uploaded")

