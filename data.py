ALREADY_EXISTS_USER = {
    "email": "r.shchetnikov@yandex.ru",
    "password": "password",
    "name": "Username"
}

USER_WITHOUT_EMAIL = {
    "password": "password",
    "name": "Username"
}

USER_WITHOUT_PASS = {
    "email": "r.shchetnikov@yandex.ru",
    "name": "Username"
}

USER_WITHOUT_NAME = {
    "email": "r.shchetnikov@yandex.ru",
    "password": "password"
}

CHANGED_USER_DATA = {
    "email": "changed_email",
    "name": "changed_name"
}

INVALID_ORDER_DATA = {
    "ingredients": ["123", "321"]
}

ALREADY_EXISTS_USER_ERROR = "User already exists"
CREATE_USER_WITHOUT_FIELD_ERROR = "Email, password and name are required fields"
INCORRECT_LOGIN = "email or password are incorrect"
CHANGE_USER_DATA_ERROR = "You should be authorised"
INVALID_ORDER_DATA_ERROR = "One or more ids provided are incorrect"