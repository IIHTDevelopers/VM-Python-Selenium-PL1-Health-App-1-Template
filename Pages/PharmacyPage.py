from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import os
import json

class PharmacyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Pharmacy.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.pharmacy_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.pharmacy_module = (By.CSS_SELECTOR, 'a[href="#/Pharmacy"]')
        self.order_link = (By.XPATH, '//a[contains(text(),"Order")]')
        self.add_new_good_receipt_button = (By.XPATH, "//button[contains(text(),'Add New Good Receipt')]")
        self.good_receipt_modal_title = (By.XPATH, "//span[contains(text(),'Add Good Receipt')]")
        self.print_receipt_button = (By.ID, "saveGr")
        self.add_new_item_button = (By.ID, "btn_AddNew")
        self.item_name_field = (By.XPATH, "//input[@placeholder='Select an Item']")
        self.batch_no_field = (By.ID, "txt_BatchNo")
        self.item_qty_field = (By.ID, "ItemQTy")
        self.rate_field = (By.ID, "GRItemPrice")
        self.save_button = (By.ID, "btn_Save")
        self.supplier_name_field = (By.ID, "SupplierName")
        self.invoice_field = (By.ID, "InvoiceId")
        self.success_message = (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Goods Receipt is Generated and Saved."]')
        self.supplier_name = (By.XPATH, '//input[@placeholder="select supplier"]')
        self.show_details = (By.XPATH, '//button[text()=" Show Details "]')

    def handling_alert_on_radiology(self):
        """
        /**
        * @Test1.1
        * @description This method navigates to the Pharmacy module, verifies the Good Receipt modal,
        * handles alerts during the Good Receipt print process, and ensures the modal is visible
        * before performing further actions.
        * @expected
        * The Good Receipt modal should be displayed, and alerts should be handled successfully.
        */
        """
        pass
        assert False, "TODO: Implement handling_alert_on_radiology"

    def handle_alert(self, alertText):
        """Handles alert popups based on the displayed message."""
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert message: {alert_text}")

            if alertText in alert_text:
                alert.accept()
                print("Alert accepted.")
            else:
                alert.dismiss()
                print("Alert dismissed.")
        except Exception as e:
            raise AssertionError(f"Failed to handle alert: {e}")

    def verify_print_receipt(self):
        """
        /**
        * @Test2
        * @description This method verifies the process of adding a new Good Receipt in the Pharmacy module,
        * filling in item details such as item name, batch number, quantity, rate, supplier name,
        * and a randomly generated invoice number. It concludes by validating the successful printing of the receipt.
        * @expected
        * The Good Receipt should be added successfully, and the receipt should be generated.
        */
        """
        pass
        assert False, "TODO: Implement verify_print_receipt"

    def verify_presence_of_supplier_name(self):
        """
        /**
        * @Test13
        * @description This method verifies the presence of a supplier name in the order section of the Pharmacy module.
        * It navigates through the necessary elements to input the supplier name, triggers the search, and then checks if
        * the supplier name appears in the results grid.
        * @return True if the supplier name is found in the results, otherwise False.
        */
        """
        pass
        assert False, "TODO: Implement verify_presence_of_supplier_name"

