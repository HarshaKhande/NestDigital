import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    male = waitForObject(names.maleRadioButton)
    female = waitForObject(names.femaleRadioButton)
    male.click()
    test.compare(male.checked, True)
    female.click()
    test.compare(female.checked, True)
    test.compare(male.checked, False)
