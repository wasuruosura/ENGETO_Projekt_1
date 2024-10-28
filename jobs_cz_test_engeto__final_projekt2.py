# Václav Osladil
# Tests performing exactly the way code is written in Playwright inspector Step over (F10) function
# Tests 3, 4 are compromised in Playwright inspector Resume (F8) function, job search page does not filter city
# Test 4, it was observed that the job detail page redirects from the jobs.cz website
# to the employer's company website
# Im not able to solve this behavior in Resume (F8) function without further experience

from playwright.sync_api import sync_playwright


def test_homepage_loads_successfully():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.jobs.cz")

        # Verify page title
        title = page.title()
        assert title == ("Jobs.cz – skvělá šance na skvělý job – nabídka práce, volná pracovní místa, "
                         "brigády i vzdělávání a rozvoj")

        # Verify search bar "job" is visible
        search_bar_job = page.locator(
            "#hp-search-box > form > div.SearchField.SearchField--grouped.SearchField--inverted."
            "SearchField--large.InterestSearch > div > div > div.SearchField__valueContainer."
            "SearchField__valueContainer--isMulti.SearchField__value-container."
            "SearchField__value-container--is-multi.css-1hwfws3 > div.SearchField__placeholder."
            "SearchField__placeholder.css-1wa3eu0-placeholder")
        assert search_bar_job.is_visible()

        # Verify search bar "city" is visible
        search_bar_city = page.locator(
            "#hp-search-box > form > div.SearchField.SearchField--grouped.SearchField--inverted."
            "SearchField--large.LocalitySearch > div > div > div.SearchField__valueContainer."
            "SearchField__valueContainer--isMulti.SearchField__value-container."
            "SearchField__value-container--is-multi.css-1hwfws3")
        assert search_bar_city.is_visible()

        # Verify navigation menu Nabídky práce / Job Offers ("profession") is visible
        nav_menu_profession = page.locator(
            "body > section > header > nav:nth-child(3) > ul > li:nth-child(1) > a")
        assert nav_menu_profession.is_visible()

        # Verify navigation menu Brigády ("brigady") is visible
        # (this menu button is not available in en version of website)
        nav_menu_brigady = page.locator(
            "body > section > header > nav:nth-child(3) > ul > li:nth-child(2) > a")
        assert nav_menu_brigady.is_visible()

        # Verify navigation menu Inspirace ("poradna") is visible
        # (this menu button is not available in en version of website)
        nav_menu_poradna = page.locator(
            "body > section > header > nav:nth-child(3) > ul > li:nth-child(3) > a")
        assert nav_menu_poradna.is_visible()

        # Verify navigation menu Zaměstnavatelé ("spolecnosti") is visible
        # (this menu button is not available in en version of website)
        nav_menu_spolecnosti = page.locator(
            "body > section > header > nav:nth-child(3) > ul > li:nth-child(4) > a")
        assert nav_menu_spolecnosti.is_visible()

        # Verify navigation menu Vytvořit si životopis / Create your CV ("zivotopis") is visible
        nav_menu_zivotopis = page.locator(
            "body > section > header > nav:nth-child(3) > ul > li:nth-child(5) > div > a")
        assert nav_menu_zivotopis.is_visible()

        # Verify navigation menu Přihlásit / Log in ("login) is visible
        nav_menu_login = page.locator(
            "body > section > header > nav.HeaderDesktopActions.HeaderDesktopActions--end > a."
            "Button.Button--primary.Button--medium")
        assert nav_menu_login.is_visible()

        # Verify navigation menu Pro firmy / Looking for Employees ("firmy") is visible
        nav_menu_firmy = page.locator(
            "body > section > header > nav.HeaderDesktopActions.HeaderDesktopActions--end > a."
            "Button.Button--inverted.Button--medium")
        assert nav_menu_firmy.is_visible()

        # Verify footer is visible
        footer = page.locator(
            "body > footer > div > div.Footer__copyright")
        assert footer.is_visible()

        browser.close()


from playwright.sync_api import sync_playwright


def test_navigation_to_for_jobs_menus():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.jobs.cz")

        # Navigate to "Looking For Employers" section
        for_employers_link = page.locator(
            "body > section > header > nav.HeaderDesktopActions.HeaderDesktopActions--end > a."
            "Button.Button--inverted.Button--medium")
        for_employers_link.click()

        # Retrieve and verify the section header text
        section_header = page.locator("body > section > div > div > h1").inner_text()
        assert section_header == "Inzerujte na Jobs.cz"

        # Navigate to "Create your CV" section
        create_cv_link = page.locator(
            "body > section > header > nav:nth-child(3) > ul > li:nth-child(5) > div > a")
        create_cv_link.click()

        # Retrieve and verify the section header text
        section_header = page.locator("body > main > section.UserCvLandingPageHero > div.Container."
                                      "Container--cassiopeia > div > h1").inner_text()
        assert section_header == "Skvělý životopis otevírá dveře"

        browser.close()


from playwright.sync_api import sync_playwright


def test_job_search():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            page.goto("https://www.jobs.cz/")

            # Locate the search input field "job"
            search_input = page.locator(
                "#hp-search-box > form > div.SearchField.SearchField--grouped.SearchField--inverted."
                "SearchField--large.InterestSearch > div > div > div.SearchField__valueContainer."
                "SearchField__valueContainer--isMulti.SearchField__value-container."
                "SearchField__value-container--is-multi.css-1hwfws3 > div.SearchField__placeholder."
                "SearchField__placeholder.css-1wa3eu0-placeholder")

            search_input.click()

            # Type text into the search field using keyboard events
            page.keyboard.type("Tester")  # Replace with your desired search query

            # Press Enter to submit the search
            page.keyboard.press("Enter")

            # Locate the search input field "city"
            search_input = page.locator(
                "#hp-search-box > form > div.SearchField.SearchField--grouped."
                "SearchField--inverted.SearchField--large.LocalitySearch > div > div > div."
                "SearchField__valueContainer.SearchField__valueContainer--isMulti."
                "SearchField__value-container.SearchField__value-container--is-multi.css-1hwfws3")

            search_input.click()

            # Type text into the search field using keyboard events
            page.keyboard.type("Praha")  # Replace with your desired search query

            # Press Enter to submit the search
            page.keyboard.press("Enter")

            # Submit the search form
            submit_button = page.locator("#hp-search-box > form > button")

            if submit_button.is_visible():
                submit_button.click()
            else:
                print("Submit button is not visible; check the form state.")

            # Optionally, wait for search results or verify expected elements on the search page
            page.wait_for_load_state("networkidle")

            # Verify that search results container is present
            search_results_container = page.locator("#search-result-container")
            assert search_results_container.is_visible(), "Search results container is not visible"

        finally:
            browser.close()

        # Run the test function
        if __name__ == "__main__":
            test_job_search()


from playwright.sync_api import sync_playwright


def test_job_detail_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.jobs.cz")

        # Locate the search input field "job"
        search_input = page.locator(
            "#hp-search-box > form > div.SearchField.SearchField--grouped.SearchField--inverted."
            "SearchField--large.InterestSearch > div > div > div.SearchField__valueContainer."
            "SearchField__valueContainer--isMulti.SearchField__value-container."
            "SearchField__value-container--is-multi.css-1hwfws3 > div."
            "SearchField__placeholder.SearchField__placeholder.css-1wa3eu0-placeholder")

        search_input.click()

        # Type text into the search field using keyboard events
        page.keyboard.type("Tester")  # Replace with your desired search query

        # Press Enter to submit the search
        page.keyboard.press("Enter")

        # Locate the search input field "city"
        search_input = page.locator(
            "#hp-search-box > form > div.SearchField.SearchField--grouped."
            "SearchField--inverted.SearchField--large.LocalitySearch > div > div > div."
            "SearchField__valueContainer.SearchField__valueContainer--isMulti."
            "SearchField__value-container.SearchField__value-container--is-multi.css-1hwfws3")

        search_input.click()

        # Type text into the search field using keyboard events
        page.keyboard.type("Praha")  # Replace with your desired search query

        # Press Enter to submit the search
        page.keyboard.press("Enter")

        # Submit the search form
        submit_button = page.locator("#hp-search-box > form > button")

        if submit_button.is_visible():
            submit_button.click()
        else:
            print("Submit button is not visible; check the form state.")

        # Optionally, wait for search results or verify expected elements on the search page
        page.wait_for_load_state("networkidle")

        # Click on the first job result
        first_job_result = page.locator(
            "#search-result-container > div.Stack.Stack--hasIntermediateDividers."
            "Stack--hasStartDivider > article:nth-child(1) > header > h2 > a").nth(
            0)

        # Extract the text from the first job result
        first_job_result_text = first_job_result.inner_text()

        # Click on the first job result
        first_job_result.click()

        # Verify the job detail page is loaded
        job_detail_title = page.locator("h1").inner_text()

        # Perform the assertion
        assert first_job_result_text in job_detail_title

        browser.close()


import pytest
from playwright.sync_api import sync_playwright


def test_invalid_login():
    with (sync_playwright() as p):
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.jobs.cz")

        # Click on the login button
        page.click("body > section > header > nav.HeaderDesktopActions.HeaderDesktopActions--end > a."
                   "Button.Button--primary.Button--medium")

        page.fill("#loginName", "invalid_user@example.com")

        page.fill("#password", 'invalid_password')

        # Click on the login button
        page.click("#jobs_login > button")

        # Wait for the error message to appear and assert its presence
        error_message_selector = "#jobs_login > div.Alert.Alert--danger.mb-600"
        page.wait_for_selector(error_message_selector)

        # Assert that the error message is displayed on the page
        error_message = page.text_content(error_message_selector)
        assert error_message is not None and "Nesprávné přihlašovací údaje" in error_message, f"Expected 'Nesprávné přihlašovací údaje', but got '{error_message}'"

        browser.close()


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
