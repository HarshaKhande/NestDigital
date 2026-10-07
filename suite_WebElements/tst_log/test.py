# -*- coding: utf-8 -*-

import names

def main():

    startBrowser("http://127.0.0.1:8000")

    test.log("Test execution started")

    username = waitForObject(
        names.usernameInput
    )

    setText(
        username,
        "admin"
    )

    test.log(
        "Username entered successfully"
    )

    login_button = waitForObject(
        names.loginButton
    )

    if login_button.disabled:

        test.warning(
            "Login button is disabled"
        )

    else:

        test.log(
            "Login button is enabled"
        )

        clickButton(
            login_button
        )

    result = waitForObject(
        names.loginResult
    )

    actual_result = str(
        result.innerText
    ).strip()

    if actual_result == "Success":

        test.log(
            "Login completed successfully"
        )

    else:

        test.fail(
            "Login failed"
        )