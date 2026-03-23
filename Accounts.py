import os

A = [
    {
        "name": "Slaiz",
        "username": os.environ.get('PA_USERNAME'),
        "password": os.environ.get('PA_PASSWORD'),
        "dashboard_url": f"https://www.pythonanywhere.com/user/{PA_USERNAME}/webapps/"
    },
    {
        "name": "Anker",
        "username": os.environ.get('ANKER_USERNAME'),
        "password": os.environ.get('ANKER_PASSWORD'),
        "dashboard_url": f"https://www.pythonanywhere.com/user/{ANKER_USERNAME}/webapps/"
    },
    {
        "name": "Akel",
        "username": os.environ.get('PA_AKEL_USERNAME'),
        "password": os.environ.get('PA_AKEL_PASSWORD'),
        "dashboard_url": f"https://www.pythonanywhere.com/user/{PA_AKEL_USERNAME}/webapps/"
    },
    {
        "name": "Imagero",
        "username": os.environ.get('PA_IMAGERO_USERNAME'),
        "password": os.environ.get('PA_IMAGERO_PASSWORD'),
        "dashboard_url": f"https://www.pythonanywhere.com/user/{PA_IMAGERO_USERNAME}/webapps/"
    }
]
