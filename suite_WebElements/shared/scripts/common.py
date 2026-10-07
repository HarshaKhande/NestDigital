# -*- coding: utf-8 -*-

BASE_URL = "http://127.0.0.1:8000"

def open_page(path="/"):
    url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
    if isBrowserOpen():
        activeBrowserTab().setUrl(url, 10000)
    else:
        startBrowser(url, 10000)
    test.log("Opened URL: " + url)

def verify_text(object_name, expected_text):
    obj = waitForObject(object_name)
    test.compare(str(obj.innerText).strip(), expected_text)

def enter_text(object_name, text_value):
    setText(waitForObject(object_name), text_value)

def click_object(object_name):
    waitForObject(object_name).click()

def check_checkbox(object_name):
    checkbox = waitForObject(object_name)
    if not checkbox.checked:
        checkbox.click()
    test.compare(checkbox.checked, True)

def uncheck_checkbox(object_name):
    checkbox = waitForObject(object_name)
    if checkbox.checked:
        checkbox.click()
    test.compare(checkbox.checked, False)

def login(username, password):

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