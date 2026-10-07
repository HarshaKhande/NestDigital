# -*- coding: utf-8 -*-

import names


def main():

    startApplication("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username = waitForObject(names.orangeHRM_username_text1)
    password = waitForObject(names.orangeHRM_password_password)

    type(username, "admin")
    type(password, "admin123")

    clickButton(
        waitForObject(names.orangeHRM_Login_submit)
    )

  