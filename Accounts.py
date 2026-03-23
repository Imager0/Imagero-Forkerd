import os

ACCOUNTS = [
    {
        "name": "Slaiz",
        "username": os.environ.get('PA_USERNAME'),
        "password": os.environ.get('PA_PASSWORD'),
        "dashboard_url": "https://www.pythonanywhere.com/user/Slaiz/webapps/"
    },
    {
        "name": "Anker",
        "username": os.environ.get('ANKER_USERNAME'),
        "password": os.environ.get('ANKER_PASSWORD'),
        "dashboard_url": "https://www.pythonanywhere.com/user/ankermax/webapps/"
    },
    {
        "name": "Akel",
        "username": os.environ.get('PA_AKEL_USERNAME'),
        "password": os.environ.get('PA_AKEL_PASSWORD'),
        "dashboard_url": "https://www.pythonanywhere.com/user/akel/webapps/"
    },
    {
        "name": "Imagero",
        "username": os.environ.get('PA_IMAGERO_USERNAME'),
        "password": os.environ.get('PA_IMAGERO_PASSWORD'),
        "dashboard_url": "https://www.pythonanywhere.com/user/Imagero/webapps/"
    }
]
