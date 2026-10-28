# Day 6 -  Python Backend Journey

users = {
    "aditya": {"password": "1234", "role": "admin"},
    "rahul": {"password": "abcd", "role": "user"}
}

def get_user(username):
    return users.get(username, "User not found")

def add_user(username, password, role="user"):
    users[username] = {"password": password, "role": role}
    return f"User {username} added"

def login(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        return f"Login Success - Role: {user['role']}"
    return "Login Failed"

# Testing
print(get_user("aditya"))
print(add_user("amit", "pass123"))
print(login("aditya", "1234"))
print(login("rahul", "wrong"))

print("\nDay 6 - Dictionaries Completed!")
