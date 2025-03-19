import json
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DoctorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Doctor.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.doctor_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.doctors_link = (By.CSS_SELECTOR, 'a[href="#/Doctors"]')
        self.inpatient_department_tab = (By.XPATH, '(//a[@href="#/Doctors/InPatientDepartment"])[2]')
        self.search_bar = (By.XPATH, "(//input[@placeholder='search'])[3]")
        self.order_dropdown = (By.XPATH, "//select")
        self.imaging_action_button = (By.XPATH, '//a[@danphe-grid-action="imaging"]')
        self.search_order_item = (By.XPATH, '//input[@placeholder="search order items"]')
        self.proceed_button = (By.XPATH, '//button[text()=" Proceed "]')
        self.sign_button = (By.XPATH, '//button[text()="Sign"]')
        self.success_message = (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Imaging and lab order add successfully"]')

    def perform_inpatient_imaging_order(self):
        """
        /**
        * @Test8
        * @description This method verifies the process of placing an imaging order for an inpatient.
        * It navigates to the Inpatient Department, searches for a specific patient, selects an imaging action,
        * chooses an order type, specifies the order item, and completes the process by signing the order.
        * @expected
        * The success message should be visible after the imaging order is placed.
        */
        """
        pass
        assert False, "TODO: Implement perform_inpatient_imaging_order"
