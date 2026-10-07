# -*- coding: utf-8 -*-

import names



def main():

    startBrowser(
        "http://127.0.0.1:8000"
    )
    
    snooze(3)

    login_button = waitForObject(
        names.loginButton
    )

    if login_button.disabled == False:

        test.log(
            "Login button is enabled"
        )

        clickButton(
            login_button
        )

    else:

        test.fail(
            "Login button is disabled"
        )