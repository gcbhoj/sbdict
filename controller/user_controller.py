from config.dbconfig import connect_db

class CreateUserController:

    def __init__(self):
        self.db = connect_db()
        self.users_collection = self.db.users

    def create_user(self):

        result = self.users_collection.insert_one({
            "username": "bhoj",
            "email": "bhoj@example.com"
        })

        return {
            "success": True,
            "message": "User created successfully",
            "id": str(result.inserted_id)
        }, 201