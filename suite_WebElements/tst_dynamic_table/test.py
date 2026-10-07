import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    table = waitForObject(names.employeeTable)
    employee_name = "Anurag"
    xpath = ".//tr[td[contains(normalize-space(.), '" + employee_name + "')]]"
    rows = table.evaluateXPath(xpath)
    test.verify(rows.snapshotLength > 0, "Employee found")
    if rows.snapshotLength > 0:
        row = rows.snapshotItem(0)
        test.log("Found row: " + str(row.innerText))
        buttons = row.evaluateXPath(".//button")
        if buttons.snapshotLength > 0:
            buttons.snapshotItem(0).click()
