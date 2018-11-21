#!/usr/bin/python

import mysql.connector


class Database:
    def __init__(self):
        self.database = mysql.connector.connect(
            host="localhost",
            user="boxhezi",
            passwd="password",
            database="test"
        )
        self.cursor = self.database.cursor()

    def __del__(self):
        self.database.close()

    def get_current_db(self):
        cursor = self.cursor
        cursor.execute("select database()")
        tables = cursor.fetchall()

    def signup(self, name, password):
        username_query = "INSERT INTO `username`(`id`, `name`) VALUES (%s, %s);"
        password_query = "INSERT INTO `password`(`id`, `password`, `user_id`) VALUES (%s, %s, %s);"

        user_id = self.generate_id("username")
        passwd_id = self.generate_id("password")
        cursor = self.cursor

        user_tuple = (user_id, name)
        password_tuple = (passwd_id, password, user_id)

        cursor.execute(username_query, user_tuple)
        cursor.execute(password_query, password_tuple)

        self.database.commit()

    def generate_id(self, table_name):
        sql_query = "SELECT * FROM %s ORDER BY id DESC"
        cursor = self.cursor
        cursor.execute(sql_query % table_name)
        id_list = cursor.fetchall()
        if len(id_list) == 0:
            next_id = 1
        else:
            next_id = id_list[0] + 1

        return next_id

    def search_username(self, name):
        cursor = self.cursor
        search_query = "SELECT name FROM username"
        cursor.execute(search_query)

        name_list = cursor.fetchall()

        for i in range(len(name_list)):
            if name == name_list[i][0]:
                return True
            return False

    def find_user_id(self, name):
        cursor = self.cursor
        search_query = "SELECT id FROM username"
        cursor.execute(search_query)

        user_id = cursor.fetchone()[0]

        return user_id

    def match_password(self, entered, user_id):
        cursor = self.cursor
        search_query = "SELECT password FROM password where user_id = %s"
        cursor.execute(search_query % user_id)

        password = cursor.fetchone()[0]
        if password == entered:
            return True
        else:
            return False
