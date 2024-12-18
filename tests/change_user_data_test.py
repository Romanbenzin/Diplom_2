import requests

from confest import create_new_user
from data import CHANGE_USER_DATA_ERROR
from helpers import generate_header_for_login, generate_changed_data
from urls import MAIN_URL, GET_USER_DATA, PATCH_USER_DATA


class TestUserDataChange:
    def test_change_user_data_with_auth(self, create_new_user):
        user_data, register_response = create_new_user
        accessToken = register_response.json()["accessToken"]
        auth_token = generate_header_for_login(accessToken)
        user_data_response_before_change = requests.get(MAIN_URL+GET_USER_DATA, headers=auth_token)

        changed_data = generate_changed_data()
        requests.patch(MAIN_URL+PATCH_USER_DATA, headers=auth_token, data=changed_data)

        user_data_response_after_change = requests.get(MAIN_URL + GET_USER_DATA, headers=auth_token)

        assert user_data_response_after_change.json()["success"] == True
        assert user_data_response_after_change.json()["user"]["email"] == changed_data["email"]
        assert user_data_response_after_change.json()["user"]["email"] != user_data_response_before_change.json()["user"]["email"]
        assert user_data_response_after_change.json()["user"]["name"] == changed_data["name"]
        assert user_data_response_after_change.json()["user"]["name"] != user_data_response_before_change.json()["user"]["name"]

    def test_change_user_data_without_auth(self, create_new_user):
        user_data, register_response = create_new_user
        accessToken = register_response.json()["accessToken"]
        auth_token = generate_header_for_login(accessToken)
        user_data_response_before_change = requests.get(MAIN_URL + GET_USER_DATA, headers=auth_token)

        changed_data = generate_changed_data()
        response_after_change_data = requests.patch(MAIN_URL + PATCH_USER_DATA, data=changed_data)

        user_data_response_after_change = requests.get(MAIN_URL + GET_USER_DATA, headers=auth_token)

        assert response_after_change_data.json()["success"] == False
        assert response_after_change_data.json()["message"] == CHANGE_USER_DATA_ERROR
        assert user_data_response_after_change.json()["user"]["email"] != changed_data["email"]
        assert user_data_response_after_change.json()["user"]["email"] == user_data_response_before_change.json()["user"]["email"]
        assert user_data_response_after_change.json()["user"]["name"] != changed_data["name"]
        assert user_data_response_after_change.json()["user"]["name"] == user_data_response_before_change.json()["user"]["name"]
