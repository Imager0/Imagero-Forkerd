import os

def create_account(name, env_prefix):
    user = os.environ.get(f'{env_prefix}_USERNAME')
    return {
        "name": name,
        "username": user,
        "password": os.environ.get(f'{env_prefix}_PASSWORD'),
        "dashboard_url": f"https://www.pythonanywhere.com/user/{user}/webapps/"
    }
A = [
    create_account("Slaiz", "PA"),
    create_account("Anker", "ANKER"),
    create_account("Akel", "PA_AKEL"),
    create_account("Imagero", "PA_IMAGERO")
]
