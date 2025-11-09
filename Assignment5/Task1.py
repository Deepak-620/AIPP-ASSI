import hashlib
import json
import os
from typing import Dict, Tuple

class LoginSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.initialize_storage()
    
    def initialize_storage(self) -> None:
        if not os.path.exists(self.users_file):
            with open(self.users_file, "w") as f:
                json.dump({}, f)
    
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username: str, password: str) -> bool:
        if not username or not password:
            return False
            
        try:
            with open(self.users_file, "r") as f:
                users = json.load(f)
                
            if username in users:
                return False
                
            users[username] = self.hash_password(password)
            
            with open(self.users_file, "w") as f:
                json.dump(users, f)
            return True
            
        except Exception:
            return False
    
    def login(self, username: str, password: str) -> bool:
        try:
            with open(self.users_file, "r") as f:
                users = json.load(f)
                
            if username not in users:
                return False
                
            return users[username] == self.hash_password(password)
            
        except Exception:
            return False
    
    def get_user_input(self) -> Tuple[str, str]:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        return username, password

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            username, password = login_system.get_user_input()
            if login_system.register(username, password):
                print("Registration successful!")
            else:
                print("Registration failed. Username might already exist.")
                
        elif choice == "2":
            username, password = login_system.get_user_input()
            if login_system.login(username, password):
                print("Login successful!")
            else:
                print("Invalid credentials.")
                
        elif choice == "3":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()