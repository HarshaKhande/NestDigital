import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    main_tab = activeBrowserTab()
    clickButton(waitForObject(names.openChildWindowButton))
    child_tab = waitForObject("{type='BrowserTab' title='Child Window'}")
    activateBrowserTab(child_tab)
    test.compare(str(activeBrowserTab().title), "Child Window")
    heading = waitForObject(names.childPageHeading)
    test.compare(str(heading.innerText).strip(), "Child Window")
    child_tab.close()
    activateBrowserTab(main_tab)
