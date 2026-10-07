# -*- coding: utf-8 -*-
from objectmaphelper import *

usernameInput = {"tagName": "INPUT", "id": "usernameInput", "type": "text"}
passwordInput = {"tagName": "INPUT", "id": "passwordInput", "type": "password"}
keyboardInput = {"tagName": "INPUT", "id": "keyboardInput", "type": "text"}
saveButton = {"tagName": "BUTTON", "id": "saveButton"}
successMessage = {"tagName": "DIV", "id": "successMessage"}
loginButton = {"tagName": "BUTTON", "id": "loginButton"}
loginResult = {"tagName": "DIV", "id": "loginResult"}
termsCheckbox = {"tagName": "INPUT", "id": "termsCheckbox", "type": "checkbox"}
maleRadioButton = {"tagName": "INPUT", "id": "maleRadioButton", "type": "radio"}
femaleRadioButton = {"tagName": "INPUT", "id": "femaleRadioButton", "type": "radio"}
countryDropdown = {"tagName": "SELECT", "id": "countryDropdown"}
aboutLink = {"tagName": "A", "id": "aboutLink"}
aboutHeading = {"tagName": "H2", "id": "aboutHeading"}
usersTable = {"tagName": "TABLE", "id": "usersTable"}
employeeTable = {"tagName": "TABLE", "id": "employeeTable"}
alertButton = {"tagName": "BUTTON", "id": "alertButton"}
deleteButton = {"tagName": "BUTTON", "id": "deleteButton"}
chooseFileButton = {"tagName": "INPUT", "id": "chooseFileButton", "type": "file"}
uploadButton = {"tagName": "BUTTON", "id": "uploadButton"}
uploadSuccessMessage = {"tagName": "DIV", "id": "uploadSuccessMessage"}
clickArea = {"tagName": "BUTTON", "id": "clickArea"}
doubleClickArea = {"tagName": "DIV", "id": "doubleClickArea"}
dragSource = {"tagName": "DIV", "id": "dragSource"}
dropTarget = {"tagName": "DIV", "id": "dropTarget"}
dropSuccessMessage = {"tagName": "DIV", "id": "dropSuccessMessage"}
openChildWindowButton = {"tagName": "BUTTON", "id": "openChildWindowButton"}
childPageHeading = {"tagName": "H1", "id": "childPageHeading"}
cardNumberInput = {"tagName": "INPUT", "id": "cardNumberInput", "type": "text"}
expiryInput = {"tagName": "INPUT", "id": "expiryInput", "type": "text"}
payButton = {"tagName": "BUTTON", "id": "payButton"}
paymentResult = {"tagName": "DIV", "id": "paymentResult"}
dynamicOrderButton = {"tagName": "BUTTON", "id": Wildcard("order_*")}

# encoding: UTF-8



orangeHRM_BrowserTab = {"title": "OrangeHRM", "type": "BrowserTab"}
orangeHRM_username_text1 = {"container": orangeHRM_BrowserTab, "name": "username", "tagName": "INPUT", "type": "text", "visible": True}
orangeHRM_password_password = {"container": orangeHRM_BrowserTab, "name": "password", "tagName": "INPUT", "type": "password", "visible": True}
orangeHRM_Login_submit = {"container": orangeHRM_BrowserTab, "simplifiedInnerText": "Login", "tagName": "BUTTON", "type": "submit", "visible": True}


