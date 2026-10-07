# -*- coding: utf-8 -*-

import names

""" text
value
checked
disabled
visible
enabled
selected """

def main():
    
    startBrowser(
        "http://127.0.0.1:8000"
    )

    login_button = waitForObject(
        names.loginButton
    )

    test.compare(
        str(login_button.innerText).strip(),
        "Login"
    )
    
    
    
#Verify button enabled

    login_button = waitForObject(
    names.loginButton
    )

    test.compare(
        login_button.disabled,
        False
    )

#Checkbox verification

    checkbox = waitForObject(
        names.termsCheckbox
    )

    checkbox.click()

    test.compare(
        checkbox.checked,
    True
    )
    
#Text Verification

    setText(
        waitForObject(names.usernameInput),
        "admin"
    )

    setText(
        waitForObject(names.passwordInput),
        "admin123"
    )

    clickButton(
        waitForObject(names.loginButton)
    )

    result = waitForObject(
        names.loginResult
    )
    
#Contains text verification

    message = str(
        waitForObject(
        names.loginResult
    ).innerText
    )

    test.verify(
    "login successful" in message
    )
    
#Image Verification


    test.imagePresent(
        "logo.png"
    )
    


