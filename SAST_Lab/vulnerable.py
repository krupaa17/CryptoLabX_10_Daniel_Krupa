import sqlite3
import random
import pickle


def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)

    return cursor.fetchall()


def generate_code():
    return random.randint(100000, 999999)


def load_data(data):
    return pickle.loads(data)


def save_password(password):
    with open("password.txt", "w") as file:
        file.write(password)


def main():
    username = input("Enter username: ")

    users = get_user(username)

    code = generate_code()

    print("Users:", users)
    print("Verification code:", code)

    save_password("mySecretPassword")


if __name__ == "__main__":
    main()
