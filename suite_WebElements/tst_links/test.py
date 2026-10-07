import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    waitForObject(names.aboutLink).click()
    heading = waitForObject(names.aboutHeading)
    test.compare(str(heading.innerText).strip(), "About Us")
