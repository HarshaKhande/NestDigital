import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    dropdown = waitForObject(names.countryDropdown)
    selectOption(dropdown, "India")
    test.log("Selected India by visible text")
    selectOptionByValue(dropdown, "US")
    test.log("Selected United States by value")
