import allure
import pytest
import requests

from static_data.json_data import USER_WITHOUT_NAME
from helpers import random_user_for_register
from static_data.urls import MAIN_URL, UPDATE_TOKEN, REGISTER


@allure.step("Создание нового пользователя")
@pytest.fixture
def create_new_user():
    user_data = random_user_for_register()
    response = requests.post(MAIN_URL+REGISTER, user_data)

    return user_data, response

@allure.step("Обновление токена пользователя")
@pytest.fixture
def update_user_token():
    response = requests.post(MAIN_URL+UPDATE_TOKEN, data=USER_WITHOUT_NAME)
    print(response.json())