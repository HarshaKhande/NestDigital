# -*- coding: utf-8 -*-

import names

#Use test.compare() when you want to compare an actual value with an expected value.

def main():

    # Simple number comparison
    actual = 10
    expected = 10

    test.compare(actual, expected, "Verify number is correct")


    # String comparison
    actual_name = "Admin"
    expected_name = "Admin"

    test.compare(
        actual_name,
        expected_name,
        "Verify username is Admin"
    )


    # Boolean comparison
    actual_status = True
    expected_status = True

    test.compare(
        actual_status,
        expected_status,
        "Verify status is True"
    )
    
#test.verify() when you already have a Boolean condition that should evaluate to True

    age = 25

    test.verify(
        age >= 18,
        "Verify user is an adult"
    )
    
    
    startApplication("MyApplication")

    loginButton = waitForObject(":Login_Button")

    test.verify(
        loginButton != None,
        "Verify Login button exists"
    )

