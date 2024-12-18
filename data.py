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

ALREADY_EXISTS_USER_ERROR = "User already exists"
CREATE_USER_WITHOUT_FIELD_ERROR = "Email, password and name are required fields"
INCORRECT_LOGIN = "email or password are incorrect"