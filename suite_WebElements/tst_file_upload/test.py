import names# -*- coding: utf-8 -*-

def main():
    source(findFile("scripts", "common.py"))
    open_page("/")
    snooze(3)
    file_path = findFile("C://Users//Anurag Patil//Documents//CorporateTraining//Iskill//Nest Digital//Squish_Web_Elements_Python_Project//suite_WebElements//shared//testdata","upload_sample.txt")
    test.log("Uploading: " + file_path)
    clickButton(waitForObject(names.chooseFileButton))
    chooseFile(file_path)
    clickButton(waitForObject(names.uploadButton))
    message = waitForObject(names.uploadSuccessMessage)
    test.compare(str(message.innerText).strip(), "Upload successful")
