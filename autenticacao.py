import json
import os
import bcrypt

class UserManager:
    def __init__(self, filename='usuarios.json'):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_users(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file)

    def create_user(self, username, password):
        if username in self.users:
            raise ValueError("Usuário já existe")
        
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.users[username] = hashed.decode()
        self.save_users()

    def authenticate_user(self, username, password):
        if username in self.users:
            hashed = self.users[username].encode()
            return bcrypt.checkpw(password.encode(), hashed)
        return False
