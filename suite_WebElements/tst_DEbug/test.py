# -*- coding: utf-8 -*-

import names

def main():

    startApplication("MyApplication")
    
#testSettings.breakOnFailure

    # Stop execution automatically when a verification fails
    testSettings.breakOnFailure = True

    actual = "Admin"
    expected = "User"

    # This fails, so Squish debugger stops here
    test.compare(
        actual,
        expected,
        "Verify username"
    )

    test.log("This executes after continuing from debugger")
    
    
    # break point


    startApplication("MyApplication")

    loginButton = waitForObject(":Login_Button")

    # Pause execution here
    test.breakpoint()

    test.verify(
        loginButton.visible,
        "Verify Login button is visible"
    )

    test.verify(
        loginButton.enabled,
        "Verify Login button is enabled"
    )

    test.compare(
        loginButton.text,
        "Login",
        "Verify Login button text"
    )