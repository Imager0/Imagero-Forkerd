import os

def create_acc(name, prefix):
    # .strip() уберет случайные пробелы, которые могли попасть в Secrets
    user = (os.environ.get(f'{prefix}_USERNAME') or "").strip()
    pw = (os.environ.get(f'{prefix}_PASSWORD') or "").strip()
    return {
        "name": name,
        "username": user,
        "password": pw
    }

A = [
    create_acc("Slaiz", "PA"),
    create_acc("Anker", "ANKER"),
    create_acc("Akel", "PA_AKEL"),
    create_acc("Imagero", "PA_IMAGERO")
]
