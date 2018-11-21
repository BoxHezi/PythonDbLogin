#!/usr/bin/python

from DatabaseConnection import Database


def login():
    username = input("Please enter your login name: ")
    existence = username_existence(username)
    if not existence:
        print("User name doesn't exist!")
    else:
        user_id = database.find_user_id(username)
        password = input("Please enter your password: ")
        match = database.match_password(password, user_id)
        if not match:
            print("Wrong password!")
            return False
        else:
            return True


def signup():
    name = input("Please enter your login name: ")
    passwd = ""

    valid_passwd = False
    while not valid_passwd:
        passwd = input("Please enter your password: ")
        confirm_passwd = input("Please enter your password again: ")
        valid_passwd = password_validation(passwd, confirm_passwd)
        if not valid_passwd:
            print("Two password don't match!")

    database.signup(name, passwd)


def username_existence(name):
    return database.search_username(name)


def password_validation(pass1, pass2):
    if pass1 != pass2:
        return False
    return True


def menu():
    print("Options:\n1. Login\n2. Signup")
    user_option = input("Please select an option: ")
    user_option = int(user_option)

    if user_option == 1:
        login()
    else:
        signup()


database = Database()
menu()
