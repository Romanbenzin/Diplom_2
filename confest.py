import allure
import pytest
import requests

from helpers import random_user_for_register, generate_header_for_login
from static_data.urls import MAIN_URL, REGISTER, DELETE


@allure.step("Создание нового пользователя")
@pytest.fixture
def create_new_user():
    user_data = random_user_for_register()
    response = requests.post(MAIN_URL+REGISTER, user_data)

    yield user_data, response

    accessToken = response.json()["accessToken"]
    delete_user = requests.delete(MAIN_URL+DELETE, headers=generate_header_for_login(accessToken))
    print(delete_user.json())
