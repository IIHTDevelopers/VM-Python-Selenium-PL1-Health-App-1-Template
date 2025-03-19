import json
import time
import os
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadiologyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Radiology.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.radiology_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.radiology_module = (By.CSS_SELECTOR, 'a[href="#/Radiology"]')
        self.list_request_sub_module = (By.XPATH, '//a[contains(text(),"List Requests")]')
        self.filter_dropdown = (By.XPATH, "//select")
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')
        self.to_date = (By.XPATH, '(//input[@id="date"])[2]')
        self.ok_button = (By.XPATH, '//button[contains(text(),"OK")]')
        self.add_report_button = (By.XPATH, '(//a[contains(text(),"Add Report")])[1]')
        self.close_modal_button = (By.XPATH, 'a[title="Cancel"]')
        self.date_range_dropdown = (By.XPATH, "//span[@data-toggle='dropdown']")
        self.last_3_months_option = (By.XPATH, "//a[text()= 'Last 3 Months']")
        self.date_cells = (By.XPATH, "//div[@role='gridcell' and @col-id='CreatedOn'][1]")

    def verify_data_within_last_three_months(self):
        """
        /**
        * @Test9
        * @description This method verifies that the data displayed in the radiology list request is within the last three months.
        * It navigates to the Radiology module, selects the "Last 3 Months" option from the date range dropdown, and confirms the filter.
        * @expected
        * All retrieved dates should be within the last three months.
        * @return True if all dates are within range, otherwise False.
        */
        """
        pass
        assert False, "TODO: Implement verify_data_within_last_three_months"

    def filter_list_requests_by_date_and_type(self):
        """
        /**
        * @Test14
        * @description This method filters the list of radiology requests based on a specified date range and imaging type.
        * It navigates to the Radiology module, applies the selected filter, enters the 'From' and 'To' dates, and confirms the filter action.
        * The method verifies that the filtered results match the specified imaging type.
        * @return True if the filtered results match the specified imaging type, otherwise False.
        */
        """
        pass
        assert False, "TODO: Implement filter_list_requests_by_date_and_type"
