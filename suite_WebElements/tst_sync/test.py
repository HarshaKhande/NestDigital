# -*- coding: utf-8 -*-
# synchronization_examples.py

import traceback
import names


# ---------------------------------------------------------
# Reusable helper: capture failure information
# ---------------------------------------------------------
def capture_failure(message):

    test.fail(message)

    test.attachDesktopScreenshot(
        "Screenshot - " + message
    )


# ---------------------------------------------------------
# Reusable helper: wait for object
# ---------------------------------------------------------
def get_object(object_name, timeout=10000):

    try:
        return waitForObject(
            object_name,
            timeout
        )

    except LookupError as e:

        test.fail(
            "Object not found: " + object_name,
            str(e)
        )

        test.attachDesktopScreenshot(
            "Object not found"
        )

        return None


# ---------------------------------------------------------
# Main Test
# ---------------------------------------------------------
def main():

    # -----------------------------------------------------
    # Default timeout for waitForObject()
    # -----------------------------------------------------
    testSettings.waitForObjectTimeout = 15000

    # Capture screenshot automatically on failures
    testSettings.logScreenshotOnFail = True


    try:

        # =================================================
        # 1. WAIT FOR WEB PAGE TO LOAD
        # =================================================

        page_loaded = waitFor(
            lambda: isPageLoaded(),
            15000
        )

        if page_loaded:

            test.pass(
                "Web page loaded successfully"
            )

        else:

            capture_failure(
                "Web page did not load"
            )

            return


        # =================================================
        # 2. WAIT FOR OBJECT TO EXIST
        # =================================================

        username = waitForObjectExists(
            ":Username_Input",
            10000
        )

        test.verify(
            username != None,
            "Username field exists"
        )


        # =================================================
        # 3. WAIT FOR OBJECT TO BE READY
        # =================================================

        username = waitForObject(
            ":Username_Input",
            10000
        )

        password = waitForObject(
            ":Password_Input",
            10000
        )

        loginButton = waitForObject(
            ":Login_Button",
            10000
        )


        # =================================================
        # 4. ENTER DATA
        # =================================================

        type(
            username,
            "admin"
        )

        type(
            password,
            "admin123"
        )


        # =================================================
        # 5. WAIT UNTIL BUTTON IS ENABLED
        # =================================================

        button_enabled = waitFor(
            lambda: loginButton.enabled,
            5000
        )

        if button_enabled:

            test.pass(
                "Login button is enabled"
            )

        else:

            capture_failure(
                "Login button did not become enabled"
            )

            return


        # =================================================
        # 6. CLICK LOGIN
        # =================================================

        mouseClick(
            loginButton
        )


        # =================================================
        # 7. WAIT FOR DASHBOARD
        # =================================================

        dashboard = waitForObject(
            ":Dashboard",
            15000
        )

        test.verify(
            dashboard.visible,
            "Dashboard is visible"
        )


        # =================================================
        # 8. WAIT FOR TEXT / PROPERTY CHANGE
        # =================================================

        statusLabel = waitForObjectExists(
            ":Status_Label",
            10000
        )

        status_completed = waitFor(
            lambda: statusLabel.text == "Completed",
            15000
        )

        if status_completed:

            test.compare(
                statusLabel.text,
                "Completed",
                "Verify status is Completed"
            )

        else:

            capture_failure(
                "Status did not change to Completed"
            )


        # =================================================
        # 9. WAIT UNTIL LOADING SPINNER DISAPPEARS
        # =================================================

        try:

            spinner = waitForObjectExists(
                ":Loading_Spinner",
                5000
            )

            spinner_gone = waitFor(
                lambda: not spinner.visible,
                15000
            )

            test.verify(
                spinner_gone,
                "Loading spinner disappeared"
            )

        except LookupError:

            test.log(
                "Loading spinner was not displayed"
            )


        # =================================================
        # 10. WAIT UNTIL OBJECT NO LONGER EXISTS
        # =================================================

        waitFor(
            lambda: not object.exists(
                ":Loading_Spinner"
            ),
            15000
        )

        test.log(
            "Loading object no longer exists"
        )


        # =================================================
        # 11. WAIT FOR TABLE
        # =================================================

        ordersTable = waitForObject(
            ":Orders_Table",
            10000
        )

        test.verify(
            ordersTable.visible,
            "Orders table is visible"
        )


        # =================================================
        # 12. WAIT FOR TABLE ITEM
        # =================================================

        try:

            item = waitForObjectItem(
                ":Orders_Table",
                "4/2",
                10000
            )

            test.verify(
                item != None,
                "Expected table item is available"
            )

        except LookupError as e:

            test.warning(
                "Table item was not found: "
                + str(e)
            )


        # =================================================
        # 13. EXAMPLE OF SMALL FIXED DELAY
        # =================================================
        # Use snooze() only when absolutely necessary.

        snooze(1)

        test.log(
            "Short fixed delay completed"
        )


        # =================================================
        # 14. FINAL VERIFICATION
        # =================================================

        test.verify(
            dashboard.visible,
            "Final verification - Dashboard visible"
        )

        test.pass(
            "Synchronization test completed successfully"
        )


    # =====================================================
    # HANDLE OBJECT LOOKUP ERRORS
    # =====================================================
    except LookupError as e:

        test.fail(
            "Synchronization / object lookup failed",
            str(e)
        )

        test.attachDesktopScreenshot(
            "Synchronization failure"
        )


    # =====================================================
    # HANDLE OTHER EXCEPTIONS
    # =====================================================
    except Exception as e:

        error_details = traceback.format_exc()

        test.fail(
            "Unexpected exception occurred",
            error_details
        )

        test.attachDesktopScreenshot(
            "Unexpected exception"
        )

