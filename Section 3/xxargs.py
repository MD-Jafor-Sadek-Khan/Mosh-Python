"""xxargs"""


def save_user(**user):
    """Saves details of a user"""
    print(user)
    print(user["name"])
    


save_user(id=1, name="rahat")
