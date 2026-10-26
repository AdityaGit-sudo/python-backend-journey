# Day 5 - Functions | Python Backend Journey

def greet(name):
    return f"Hello, {name}! Welcome to Backend"

def add(a, b):
    return a + b

def check_login(username, password):
    if username == "admin" and password == "1234":
        return "Login Success"
    else:
        return "Login Failed"

# Testing the functions
print(greet("Aditya"))
print(f"Sum of 10 + 20 is: {add(10, 20)}")
print(check_login("admin", "1234"))
print(check_login("user", "wrong"))

print("\nDay 5 - Functions Completed!")
