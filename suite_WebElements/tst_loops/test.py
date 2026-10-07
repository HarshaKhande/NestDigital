import names

def main():

    startBrowser(
        "http://127.0.0.1:8000"
    )

    users = [
        ("admin", "admin123"),
        ("tester", "test123")
    ]

    for username, password in users:

        setText(
            waitForObject(
                names.usernameInput
            ),
            username
        )

        setText(
            waitForObject(
                names.passwordInput
            ),
            password
        )

        clickButton(
            waitForObject(
                names.loginButton
            )
        )

        test.log(
            "Executed test for "
            + username
        )