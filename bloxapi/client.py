import json
import asyncio
import requests
from.user import User

class Client:
    """
    Client tingz
    """

    def __init__(self, cookie=None):
        self.cookie = cookie


    async def get_user_by_username(self, username: str):
        response = requests.get(url=f'https://api.roblox.com/users/get-by-username?username={username}')
        json = response.json()
        if response.status_code != 200 or not json.get('Id'):
            return None
        else:
            return User(json["Username"], json["Id"])

    async def get_user_by_id(self, id: int):
        response = requests.get(url=f'https://api.roblox.com/users/{id}')
        json = response.json()
        if response.status_code != 200 or not json.get('Username'):
            return None
        else:
            return User(json["Username"], json["Id"])
