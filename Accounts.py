import os

def create_acc(name, prefix):
    return {
        "name": name,
        "username": os.environ.get(f'{prefix}_USERNAME'),
        "password": os.environ.get(f'{prefix}_PASSWORD'),
    }

A = [
    create_acc("Slaiz", "PA"),
    create_acc("Anker", "ANKER"),
    create_acc("Akel", "PA_AKEL"),
    create_acc("Imagero", "PA_IMAGERO")
]
