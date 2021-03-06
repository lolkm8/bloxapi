import json
import asyncio
import requests
# from .utils import User




class User:
    def __init__(self, username: str, id: int):
        self.username = username
        self.id = id

    async def get_status(self):
        response = requests.get(url=f'https://users.roblox.com/v1/users/{self.id}/status')
        json = response.json()
        return json["status"]

    async def get_description(self):
        response = requests.get(url=f'https://users.roblox.com/v1/users/{self.id}')
        json = response.json()
        return json["description"]

    async def get_friends(self):
        response = requests.get(url=f'https://friends.roblox.com/v1/users/{self.id}/friends')
        json = response.json()
        friends = []
        for friend in json["data"]:
            friends.append(User(friend["name"], friend["id"]))
        return friends

    async def get_join_date(self):
        response = requests.get(url=f'https://users.roblox.com/v1/users/{self.id}')
        json = response.json()
        return json["created"].split('T')[0]





# >>> User.id
# 2 Display past usernames << dmsDMS LOOKIN dmsDMS
# >>> TODO
# 3 Display item ID's of what they're currently wearing
# >>> TODO
# 4 Display when they joined
# >>> TODO
# 5 Display when they were last online
# >>> Not doing
# 6 Indicate RAP <<< GIVE MORE LIKE THIS
# >>> TODO
