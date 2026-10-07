# -*- coding: utf-8 -*-
import names

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    button = waitForObject(names.saveButton)
    test.compare(str(button.innerText).strip(), "Save")
    clickButton(button)
    snooze(2)
    message = waitForObject(names.successMessage)
    test.compare(str(message.innerText).strip(), "Saved successfully")
