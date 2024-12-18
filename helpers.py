import random

def random_user_for_register():
    random_number = random.randint(10000000, 99999999)
    random_email = f"r.shchetnikov:{random_number}@yandex.ru"
    random_pass = f"password:{random_number}"
    random_username = f"Username:{random_number}"

    user_data = {
        "email": random_email,
        "password": random_pass,
        "name": random_username
    }

    return user_data

def generate_data_for_login(email, password):
    login_data = {
        "email": email,
        "password": password
    }

    return login_data

def generate_incorrect_data_for_login():
    random_number = random.randint(100000000, 999999999)
    login_data = {
        "email": f"bimbimbim:{random_number}",
        "password": f"bambambam:{random_number}"
    }

    return login_data
