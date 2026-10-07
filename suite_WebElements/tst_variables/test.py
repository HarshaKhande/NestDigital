# -*- coding: utf-8 -*-

import names

# -*- coding: utf-8 -*-
def main():

    # String
    username = "admin"

    # Integer
    retry_count = 3

    # Float
    wait_time = 2.5

    # Boolean
    login_expected = True

    # List
    users = ["admin", "tester", "manager"]

    # Tuple
    credentials = ("admin", "admin123")

    # Dictionary
    user_data = {
        "username": "admin",
        "password": "admin123"
    }

    test.log("Username: " + username)
    test.log("Retry Count: " + str(retry_count))
    test.log("Wait Time: " + str(wait_time))
    test.log("Login Expected: " + str(login_expected))
