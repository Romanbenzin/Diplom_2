import requests

from confest import create_new_user
from data import INCORRECT_LOGIN
from helpers import generate_data_for_login, generate_incorrect_data_for_login
from urls import MAIN_URL, LOGIN


class TestUserCreate:
    def test_login_user(self, create_new_user):
        user_data, register_response = create_new_user
        accessToken = register_response.json()["accessToken"]

        login_data = generate_data_for_login(user_data["email"], user_data["password"])
        login_response = requests.post(MAIN_URL+LOGIN, data=login_data)

        assert login_response.json()["success"] == True
        assert login_response.json()["accessToken"] == accessToken
        assert login_response.json()["user"]["email"] == user_data["email"]
        assert login_response.json()["user"]["name"] == user_data["name"]

    def test_incorrect_login_data(self):
        login_data = generate_incorrect_data_for_login()

        incorrect_login = requests.post(MAIN_URL+LOGIN, data=login_data)

        assert incorrect_login.json()["success"] == False
        assert incorrect_login.json()["message"] == INCORRECT_LOGIN
