from typing import TypedDict
from typing_extensions import NotRequired

class User(TypedDict):
    id: int
    name: str
    email: str
    phone: NotRequired[str]


user: User = {
    "id": 123, 
    "name": "deepak sagar", 
    "email": "sagardeepak",
    # "phone": 
}

print(user)
print(user["id"])
print(user["name"])