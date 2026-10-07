# -*- coding: UTF-8 -*-
"""
Squish Python - Assertions / Verification Examples

Demonstrates:
1. test.verify()
2. test.compare()
3. Object existence verification
4. Textbox value verification
5. Checkbox verification
6. Radio button verification
7. Text contains / not contains
8. Numeric verification
9. Table verification
10. Dynamic table verification
11. Multiple assertions
12. Login result verification
13. Python assert example

Replace names.* with the symbolic names from your Squish Object Map.
"""

BASE_URL = "http://127.0.0.1:8000"


def verify_button_enabled():
    login_button = waitForObject(names.loginButton)
    test.verify(
        login_button.disabled == False,
        "Login button should be enabled"
    )


def verify_button_text():
    button = waitForObject(names.loginButton)
    actual_text = str(button.innerText).strip()
    test.compare(
        actual_text,
        "Login",
        "Verify Login button text"
    )


def verify_object_exists():
    test.verify(
        object.exists(names.loginButton),
        "Login button should exist"
    )


def verify_textbox_value():
    username = waitForObject(names.usernameInput)
    setText(username, "admin")
    test.compare(
        str(username.value),
        "admin",
        "Verify username value"
    )


def verify_checkbox():
    checkbox = waitForObject(names.termsCheckbox)
    if not checkbox.checked:
        checkbox.click()

    test.verify(
        checkbox.checked,
        "Terms checkbox should be selected"
    )

    test.compare(
        checkbox.checked,
        True,
        "Verify checkbox selected state"
    )


def verify_radio_button():
    male_radio = waitForObject(names.maleRadioButton)
    male_radio.click()
    test.compare(
        male_radio.checked,
        True,
        "Male radio button should be selected"
    )


def verify_text_contains():
    result = waitForObject(names.loginResult)
    actual_text = str(result.innerText).strip()
    test.verify(
        "Success" in actual_text,
        "Result should contain Success"
    )


def verify_text_not_contains():
    result = waitForObject(names.loginResult)
    actual_text = str(result.innerText).strip()
    test.verify(
        "Error" not in actual_text,
        "Result should not contain Error"
    )


def verify_numeric_value():
    actual_count = 5
    expected_count = 5

    test.compare(
        actual_count,
        expected_count,
        "Verify record count"
    )

    test.verify(
        actual_count > 0,
        "At least one record should exist"
    )


def verify_table():
    table = waitForObject(names.usersTable)
    rows = table.evaluateXPath(".//tbody/tr")

    test.verify(
        rows.snapshotLength > 0,
        "User table should contain records"
    )

    test.compare(
        rows.snapshotLength,
        2,
        "Verify number of user rows"
    )


def verify_dynamic_table_record():
    employee_name = "Anurag"
    table = waitForObject(names.employeeTable)

    xpath = (
        ".//tr[td[contains(normalize-space(.), '"
        + employee_name
        + "')]]"
    )

    rows = table.evaluateXPath(xpath)

    test.verify(
        rows.snapshotLength > 0,
        "Employee should exist in table"
    )


def multiple_assertions():
    username = waitForObject(names.usernameInput)
    login_button = waitForObject(names.loginButton)

    test.verify(
        object.exists(names.usernameInput),
        "Username field exists"
    )

    test.compare(
        login_button.disabled,
        False,
        "Login button is enabled"
    )

    setText(username, "admin")

    test.compare(
        str(username.value),
        "admin",
        "Username entered correctly"
    )


def verify_login_result():
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

    result = waitForObject(names.loginResult)

    test.compare(
        str(result.innerText).strip(),
        "Success",
        "Login should be successful"
    )


def python_assert_example():
    button = waitForObject(names.loginButton)

    # Valid Python, but Squish test.verify/test.compare are usually preferred
    # because they integrate with Squish Test Results.
    assert button.disabled == False


def main():
    test.log("Starting Squish Assertion Examples")
    startBrowser(BASE_URL)

    test.startSection("Boolean Assertion")
    verify_button_enabled()
    test.endSection()

    test.startSection("Equality Assertion")
    verify_button_text()
    test.endSection()

    test.startSection("Object Existence")
    verify_object_exists()
    test.endSection()

    test.startSection("Textbox Verification")
    verify_textbox_value()
    test.endSection()

    test.startSection("Checkbox Verification")
    verify_checkbox()
    test.endSection()

    test.startSection("Radio Button Verification")
    verify_radio_button()
    test.endSection()

    test.startSection("Numeric Verification")
    verify_numeric_value()
    test.endSection()

    test.startSection("Table Verification")
    verify_table()
    test.endSection()

    test.startSection("Dynamic Table Verification")
    verify_dynamic_table_record()
    test.endSection()

    test.startSection("Multiple Assertions")
    multiple_assertions()
    test.endSection()

    test.startSection("Login Verification")
    verify_login_result()
    test.endSection()

    test.startSection("Text Contains Verification")
    verify_text_contains()
    test.endSection()

    test.startSection("Text Does Not Contain Verification")
    verify_text_not_contains()
    test.endSection()

    # Uncomment to demonstrate a normal Python AssertionError:
    # python_assert_example()

    test.log("Squish Assertion Examples Completed")
