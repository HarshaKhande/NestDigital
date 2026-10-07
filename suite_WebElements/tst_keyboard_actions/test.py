import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    field = waitForObject(names.keyboardInput)
    typeText(field, "Squish Automation")
    test.compare(str(field.value), "Squish Automation")
    nativeMouseClick(field, MouseButton.LeftButton)
    nativeType("<Ctrl+a>")
    nativeType("Updated Text")
    nativeType("<Return>")
