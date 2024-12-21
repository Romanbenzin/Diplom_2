import allure
import requests

from confest import create_new_user
from static_data.error_data import USER_NOT_AUTH_ERROR
from helpers import generate_header_for_login, generate_changed_data, generate_json_for_test_change
from static_data.urls import MAIN_URL, GET_USER_DATA, PATCH_USER_DATA


class TestUserDataChange:
    @allure.title("Тест смены пользовательских данных")
    def test_change_user_data_with_auth(self, create_new_user):
        user_data, register_response = create_new_user
        accessToken = register_response.json()["accessToken"]
        auth_token = generate_header_for_login(accessToken)

        changed_data = generate_changed_data()
        requests.patch(MAIN_URL+PATCH_USER_DATA, headers=auth_token, data=changed_data)

        user_data_response_after_change = requests.get(MAIN_URL + GET_USER_DATA, headers=auth_token).json()

        data_after_change = generate_json_for_test_change(user_data_response_after_change["success"], user_data_response_after_change["user"]["email"], user_data_response_after_change["user"]["name"])
        data_before_change = generate_json_for_test_change(True, changed_data["email"], changed_data["name"])

        assert data_after_change == data_before_change

    @allure.title("Тест смены пользовательских данных без авторизации")
    def test_change_user_data_without_auth(self, create_new_user):

        changed_data = generate_changed_data()
        response_after_change_data = requests.patch(MAIN_URL + PATCH_USER_DATA, data=changed_data).json()

        assert response_after_change_data["success"] == False
        assert response_after_change_data["message"] == USER_NOT_AUTH_ERROR
