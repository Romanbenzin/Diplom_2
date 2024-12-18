import random

def random_user_for_register():
    random_number = random.randint(10000000, 99999999)
    random_email = f"r.shchetnikov:{random_number}@yandex.ru"
    random_pass = f"password:{random_number}"
    random_username = f"Username:{random_number}"

    return {
    "email": random_email,
    "password": random_pass,
    "name": random_username
}