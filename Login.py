#!/usr/bin/python

from DatabaseConnection import Database
import getpass


def login():
    while True:
        username = input("Please enter your login name: ")
        existence = username_existence(username)
        if not existence:
            print("User doesn't exist!")
        else:
            user_id = database.find_user_id(username)
            password = getpass.getpass("Please enter your password: ")
            match = database.match_password(password, user_id)
            if not match:
                print("Wrong password!")
                return False
            else:
                print("Login successfully")
                return True


def signup():
    name = ""
    exist_name = True
    while exist_name:
        name = input("Please enter your login name: ")
        exist_name = username_existence(name)
        if exist_name:
            print("Username exist already, please try something different!")

    passwd = ""

    valid_passwd = False
    while not valid_passwd:
        passwd = getpass.getpass("Please enter your password: ")
        confirm_passwd = getpass.getpass("Please enter your password again: ")
        valid_passwd = password_validation(passwd, confirm_passwd)
        if not valid_passwd:
            print("Two password don't match!")

    database.signup(name, passwd)
    print("Sign up successfully")


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
