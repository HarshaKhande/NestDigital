import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    username = waitForObject(names.usernameInput)
    setText(username, "admin")
    test.compare(str(username.value), "admin")
    login_button = waitForObject(names.loginButton)
    test.compare(str(login_button.innerText).strip(), "Login")
    test.compare(login_button.disabled, False)
    test.verify(object.exists(names.loginButton))
