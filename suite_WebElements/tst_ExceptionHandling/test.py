# -*- coding: utf-8 -*-

import names

def main():
    
    startBrowser(
        "http://127.0.0.1:8000"
    )
    
    snooze(3)


    try:

        login_button = waitForObject(
            names.loginButton,
            5000
        )

        clickButton(
            login_button
        )

        test.log(
            "Login button clicked"
        )

    except Exception as error:

        test.fail(
            "Unable to click login button"
        )

        test.log(
            str(error)
        )
