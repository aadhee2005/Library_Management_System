users = {
    "aadhi": "aadhi2005",
    "user": "mypassword"
}
def login(username, password):
    if username in users and users[username] == password:
        print(f"Login successful for {username}")
    else:
        print("Invalid username or password")
login("deepan", "password123")
login("user", "wrongpass")