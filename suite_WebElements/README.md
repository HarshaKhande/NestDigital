# Squish Web Elements - Python Sample Suite

This is a training/sample project for **Squish for Web + Python**.

It includes examples for textboxes, buttons, checkboxes, radio buttons, dropdowns, links, static/dynamic tables, alerts, file upload, mouse actions, keyboard actions, browser tabs/windows, iframes, property verification, dynamic objects, reusable functions, and CSV data-driven testing.

## Import / Open in Squish

1. Extract `Squish_Web_Elements_Python_Project.zip`.
2. Open Command Prompt in `suite_WebElements\demo_site`.
3. Run `python server.py`.
4. Confirm `http://127.0.0.1:8000` opens.
5. Open **Squish IDE -> File -> Open Test Suite**.
6. Select the extracted `suite_WebElements` folder.
7. Run an individual `tst_*` test case.

## Object Map

The script-based Object Map is `shared/scripts/names.py`. It matches the included demo site. If you point the suite at your own application, record/pick your own objects and update these entries.

## Shared Resources

- `shared/scripts/common.py` - reusable functions
- `shared/testdata/users.csv` - login data
- `shared/testdata/upload_sample.txt` - upload test file

## Browser Setup

Configure a supported browser in Squish. If you use Microsoft Edge and Squish reports a missing Edge Driver, install/configure the matching Edge WebDriver first.

## Note

This is a teaching project. A few native keyboard/mouse and popup behaviors can vary by operating system, browser, and Squish version.
