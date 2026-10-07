import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    records = testData.dataset("users.csv")
    for record in records:
        username = testData.field(record, "Username")
        password = testData.field(record, "Password")
        expected = testData.field(record, "Expected")
        setText(waitForObject(names.usernameInput), username)
        setText(waitForObject(names.passwordInput), password)
        clickButton(waitForObject(names.loginButton))
        result = waitForObject(names.loginResult)
        test.compare(str(result.innerText).strip(), expected)
