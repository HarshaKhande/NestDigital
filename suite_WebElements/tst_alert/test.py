import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    tab = activeBrowserTab()
    clickButton(waitForObject(names.alertButton))
    closeAlert(":dummy")
    test.compare(lastAlertText(tab), "Saved successfully")
    clickButton(waitForObject(names.deleteButton))
    closeConfirm(":dummy", True)
    test.compare(lastConfirmText(tab), "Are you sure?")
