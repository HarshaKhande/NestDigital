import names# -*- coding: utf-8 -*-



def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    checkbox = waitForObject(names.termsCheckbox)
    checkbox.click()
   
  