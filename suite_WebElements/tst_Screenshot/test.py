# -*- coding: utf-8 -*-

import names

#test.attachDesktopScreenshot() captures the complete desktop where the browser AUT is running


def main():

    startApplication("Chrome")

    # Perform web actions here

    test.attachDesktopScreenshot(
        "Screenshot of web application"
    )
    
#For a web application, you can capture a specific element recognized by Squish, such as a:

    loginButton = waitForObject(":Login_Button")

    image = object.grabScreenshot(
        loginButton,
        {"delay": 0}
    )

    test.attachImage(
        image,
        "Login button screenshot"
    )
    
#capture a text field

    username = waitForObject(":Username_Input")

    image = object.grabScreenshot(
        username,
        {"delay": 0}
    )

    test.attachImage(
        image,
        "Username field"
    )
    
#capture screenshot only when test fails

    loginButton = waitForObject(":Login_Button")

    if loginButton.enabled:
        test.pass(
            "Login button is enabled"
    )

    else:

        test.fail(
            "Login button is disabled"
        )

        test.attachDesktopScreenshot(
            "Failure screenshot"
        )
    
    
    