import allure
import requests

from confest import create_new_user
from static_data.json_data import INVALID_ORDER_DATA
from helpers import generate_header_for_login, generate_list_for_order, generate_body_for_order
from static_data.urls import MAIN_URL, ORDER, GET_INGREDIENTS


class TestOrderCreate:
    @allure.title("Тест создания заказа с ингредиентами")
    def test_order_create_with_auth(self, create_new_user):
        user_data, register_response = create_new_user
        accessToken = register_response.json()["accessToken"]

        # Создание списка для передачи в создание заказа
        ingredients_response = requests.get(MAIN_URL + GET_INGREDIENTS)
        ingredient_list = []
        generate_list_for_order(ingredients_response.json()["data"][0]["_id"], ingredient_list)
        generate_list_for_order(ingredients_response.json()["data"][1]["_id"], ingredient_list)
        ingredients_data = generate_body_for_order(ingredient_list)

        order_create_response = requests.post(MAIN_URL+ORDER, data=ingredients_data, headers=generate_header_for_login(accessToken))
        assert order_create_response.json()["success"] == True
        assert len(order_create_response.json()["order"]["ingredients"]) == len(ingredient_list)

    @allure.title("Тест создания заказа без авторизации")
    def test_order_create_without_auth(self, create_new_user):
        # Создание списка для передачи в создание заказа
        ingredients_response = requests.get(MAIN_URL + GET_INGREDIENTS)
        ingredient_list = []
        generate_list_for_order(ingredients_response.json()["data"][0]["_id"], ingredient_list)
        generate_list_for_order(ingredients_response.json()["data"][1]["_id"], ingredient_list)
        ingredients_data = generate_body_for_order(ingredient_list)

        # Не возвращается список ингредиентов у ордера
        order_create_response = requests.post(MAIN_URL+ORDER, data=ingredients_data)
        assert order_create_response.json()["success"] == True

    @allure.title("Тест создания заказа без ингредиентов")
    def test_order_create_with_auth(self, create_new_user):
        user_data, register_response = create_new_user
        accessToken = register_response.json()["accessToken"]

        # Создание списка для передачи в создание заказа
        ingredient_list = []
        ingredients_data = generate_body_for_order(ingredient_list)

        order_create_response = requests.post(MAIN_URL+ORDER, data=ingredients_data, headers=generate_header_for_login(accessToken))
        assert order_create_response.json()["success"] == False
        assert order_create_response.status_code == 400

    @allure.title("Тест создания заказа с невалидным хешем")
    def test_order_create_with_invalid_hash(self, create_new_user):
        order_create_response = requests.post(MAIN_URL+ORDER, data=INVALID_ORDER_DATA)

        assert order_create_response.status_code == 500
