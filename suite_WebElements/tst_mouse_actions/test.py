import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    mouseClick(names.clickArea)
    snooze(2)
    obj = waitForObject(names.doubleClickArea)

    doubleClick(
        obj,
        5,
        5,
    )

    source_obj = waitForObject(names.dragSource)
    target_obj = waitForObject(names.dropTarget)
    startDrag(source_obj, 5, 5)
    dropOn(target_obj, 5, 5)
    result = waitForObject(names.dropSuccessMessage)
    test.compare(str(result.innerText).strip(), "Dropped")
