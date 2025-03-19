from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

class MedicalRecordsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

         # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "MedicalRecord.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.medical_record_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")
        
        self.medical_records_link = (By.CSS_SELECTOR, 'a[href="#/Medical-records"]')
        self.mr_outpatient_list = (By.XPATH, '(//a[@href="#/Medical-records/OutpatientList"])[2]')
        self.ok_button = (By.XPATH, '//button[@class="btn green btn-success"]')
        self.search_bar = (By.ID, "quickFilterInput")
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')
        self.doctor_filter = (By.XPATH, '//input[@placeholder="Doctor Name"]')

    def keyword_matching(self):
        """
        /**
        * @Test3
        * @description This method verifies patient records in the Dispensary module by applying a date filter
        * and searching for a specific patient by gender. It validates the search results by checking if the
        * gender appears in the filtered records.
        * @expected
        * The search results should display only records matching the specified gender.
        */
        """
        pass
        assert False, "TODO: Implement keyword_matching"

    def presence_of_doctor_filter(self):
        """
        /**
        * @Test4
        * @description This method verifies the presence of the doctor filter functionality in the medical records module.
        * It applies the filter by selecting a specific doctor and a date range, and validates that the search results
        * correctly display records associated with the selected doctor.
        * @expected
        * The search results should display only records associated with the selected doctor.
        */
        """
        pass
        assert False, "TODO: Implement presence_of_doctor_filter"