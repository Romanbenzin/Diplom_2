import allure
import requests

from confest import create_new_user
from helpers import generate_list_for_order, generate_body_for_order, generate_header_for_login
from static_data.error_data import USER_NOT_AUTH_ERROR
from static_data.urls import MAIN_URL, ORDER, GET_INGREDIENTS


class TestGetOrder:
    @allure.title("Тест получения заказов пользователя")
    def test_get_order(self, create_new_user):
        user_data, register_response = create_new_user

        accessToken = register_response.json()["accessToken"]

        # Создание списка для передачи в создание заказа
        ingredients_response = requests.get(MAIN_URL + GET_INGREDIENTS)
        ingredient_list = []
        generate_list_for_order(ingredients_response.json()["data"][0]["_id"], ingredient_list)
        generate_list_for_order(ingredients_response.json()["data"][1]["_id"], ingredient_list)
        ingredients_data = generate_body_for_order(ingredient_list)

        auth_header = generate_header_for_login(accessToken)
        order_create_response = requests.post(MAIN_URL+ORDER, data=ingredients_data, headers=auth_header)
        order_response = requests.get(MAIN_URL+ORDER, headers=auth_header)

        assert order_response.status_code == 200
        assert order_response.json()["success"] == True
        assert order_create_response.json()["order"]["_id"] == order_response.json()["orders"][0]["_id"]

    @allure.title("Тест получения заказов пользователя без авторизации")
    def test_get_order_without_auth(self):
        order_response = requests.get(MAIN_URL+ORDER)

        assert order_response.status_code == 401
        assert order_response.json()["success"] == False
        assert order_response.json()["message"] == USER_NOT_AUTH_ERROR
