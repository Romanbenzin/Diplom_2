import allure
import pytest
import requests

from helpers import random_user_for_register
from static_data.urls import MAIN_URL, REGISTER


@allure.step("Создание нового пользователя")
@pytest.fixture
def create_new_user():
    user_data = random_user_for_register()
    response = requests.post(MAIN_URL+REGISTER, user_data)

    return user_data, response
