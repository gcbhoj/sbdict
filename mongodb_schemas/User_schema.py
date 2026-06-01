from config.dbconfig import connect_db

db = connect_db()

user_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["username", "email"],
        "properties": {
            "username": {
                "bsonType": "string",
                "description": "Must be a string and is required"
            },
            "email": {
                "bsonType": "string",
                "pattern": "^.+@.+$",
                "description": "Must be a valid email string"
            }
        }
    }
}

if "users" not in db.list_collection_names():
    db.create_collection(
        "users",
        validator=user_validator
    )