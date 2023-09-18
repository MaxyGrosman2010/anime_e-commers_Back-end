
def user_schema(user) -> dict:
    return {"id": str(user["_id"]), "name": user["name"], "surname": user["surname"],
    "username": user["name"], "age": user["age"], "email": user["email"]}

def userdb_schema(user_db) -> dict:
    return {"id": str(user_db["_id"]), "name": user_db["name"], "surname": user_db["surname"],
    "username": user_db["name"], "age": user_db["age"], "email": user_db["email"],
    "password": user_db["password"], "disable": user_db["disable"]}