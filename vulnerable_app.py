import os
import pickle

# Hardcoded Credentials
API_KEY = "AIzaSyD-1234567890SecretKey"

def execute_user_input(user_command):
    # Command Injection
    os.system(user_command)

def get_user(db, username):
    # SQL Injection
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    db.execute(query)

def load_data(data):
    # Unsafe Deserialization
    return pickle.loads(data)
