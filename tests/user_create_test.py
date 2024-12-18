import requests

from data import ALREADY_EXISTS_USER
from helpers import random_user_for_register
from urls import MAIN_URL, REGISTER


class TestUserCreate:

    def test_user_create(self):
        response = requests.post(MAIN_URL+REGISTER, data=random_user_for_register())
        print('sss')
        print(response.json())
        print('sss')