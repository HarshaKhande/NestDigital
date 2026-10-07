# -*- coding: utf-8 -*-
import names

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    username = waitForObject(names.usernameInput)
    setText(username, "Anurag")
    test.compare(str(username.value), "Anurag")
  
