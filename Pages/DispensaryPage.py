import os
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DispensaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.download_path = os.path.join(os.getcwd(), "downloads")

        self.dispensary_link = (By.XPATH, '//a[@href="#/Dispensary"]')
        self.reports_tab = (By.XPATH, '//a[contains(text(),"Reports")]')
        self.user_collection_report = (By.XPATH, '//i[text()="User Collection"]')
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')
        self.show_report_button = (By.XPATH, '//span[text()="Show Report"]')
        self.export_button = (By.XPATH, '//button[@title="Export To Excel"]')

    def verify_export_user_collection_report(self):
        """
        /**
        * @Test10
        * @description This method verifies the export functionality for the User Collection Report.
        * @expected The exported file should download with the name `PharmacyUserwiseCollectionReport_2025`.
        * @return True if the expected file is downloaded, otherwise False.
        */
        """
        pass
        assert False, "TODO: Implement verify_export_user_collection_report"


