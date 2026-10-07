import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    tab = activeBrowserTab()
    test.verify(hasFrameContext(tab, "paymentFrame"), "paymentFrame is available")
    setFrameContext(tab, "paymentFrame")
    setText(waitForObject(names.cardNumberInput), "4111111111111111")
    setText(waitForObject(names.expiryInput), "12/30")
    clickButton(waitForObject(names.payButton))
    result = waitForObject(names.paymentResult)
    test.compare(str(result.innerText).strip(), "Payment submitted")
