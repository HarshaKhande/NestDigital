import names

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    table = waitForObject(names.usersTable)
    cells = table.evaluateXPath(".//tbody/tr[1]/td")
    test.verify(cells.snapshotLength > 0, "Table contains cells")
    for index in range(cells.snapshotLength):
        cell = cells.snapshotItem(index)
        test.log("Column " + str(index) + ": " + str(cell.innerText))
