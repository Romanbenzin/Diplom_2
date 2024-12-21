import allure
import pytest
import requests

from static_data.json_data import ALREADY_EXISTS_USER, USER_WITHOUT_EMAIL, USER_WITHOUT_PASS, USER_WITHOUT_NAME
from static_data.error_data import ALREADY_EXISTS_USER_ERROR, CREATE_USER_WITHOUT_FIELD_ERROR
from helpers import random_user_for_register
from static_data.urls import MAIN_URL, REGISTER


class TestUserCreate:
    @allure.title("Тест создания уникального пользователя")
    def test_user_create(self):
        user_data = random_user_for_register()
        response = requests.post(MAIN_URL+REGISTER, data=user_data)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == user_data["email"]
        assert response.json()["user"]["name"] == user_data["name"]

    @allure.title("Тест создания пользователя, который уже зарегистрирован")
    def test_already_exists_user(self):
        response = requests.post(MAIN_URL+REGISTER, data=ALREADY_EXISTS_USER)

        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == ALREADY_EXISTS_USER_ERROR

    @allure.title("Тест создания пользователя, без заполнения одного из обязательных полей")
    @pytest.mark.parametrize("user_data", [USER_WITHOUT_EMAIL, USER_WITHOUT_PASS, USER_WITHOUT_NAME])
    def test_user_create_without_field(self, user_data):
        response = requests.post(MAIN_URL+REGISTER, data=user_data)

        assert response.status_code == 403
        assert response.json()["success"] == False
        assert response.json()["message"] == CREATE_USER_WITHOUT_FIELD_ERROR
