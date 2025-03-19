from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import os
import time

class SubStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "SubStore.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.substore_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")
        
        self.ward_supply_link = (By.CSS_SELECTOR, 'a[href="#/WardSupply"]')
        self.substore = (By.XPATH, '//i[text()="Accounts"]')
        self.inventory_requisition_tab = (By.XPATH, '//a[text()="Inventory Requisition"]')
        self.create_requisition_button = (By.XPATH, '//span[text()="Create Requisition"]')
        self.target_inventory_dropdown = (By.XPATH, '//input[@id="activeInventory"]')
        self.item_name_field = (By.XPATH, '//input[@placeholder="Item Name"]')
        self.request_button = (By.XPATH, '//input[@value="Request"]')
        self.success_message = (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Requisition is Generated and Saved"]')
        self.account_btn = (By.XPATH, '//span[contains(@class, "report-name")]/i[contains(text(), "Accounts")]')
        self.print_button = (By.XPATH, '//button[@id="printButton"]')
        self.consumption_link = (By.XPATH, '(//a[@href="#/WardSupply/Inventory/Consumption"])')
        self.new_consumption_btn = (By.XPATH, '//span[contains(@class, "glyphicon") and contains(@class, "glyphicon-plus")]')
        self.input_item_name = (By.ID, "itemName0")
        self.save_btn = (By.ID, "save")
        self.success_message1 = (By.XPATH, '//p[contains(text()," Success ")]/../p[text()="Consumption completed"]')
        self.report_link = (By.XPATH, '(//a[@href="#/WardSupply/Inventory/Reports"])')
        self.consumption_report = (By.XPATH, '//span[contains(@class, "report-name")]/i[contains(text(), "Consumption Report")]')
        self.sub_category = (By.XPATH, '//select[@id="selectedCategoryName"]')
        self.show_report = (By.XPATH, '//button[contains(text(),"Show Report")]')
        self.issue_field = (By.XPATH, "//input[@placeholder='Issue No']")
        self.from_date = (By.XPATH, '(//input[@id="date"])[1]')

    def create_inventory_requisition(self):
        """
        /**
        * @Test6
        * @description This method verifies the creation of an inventory requisition in the Ward Supply module.
        * It navigates to the Substore section, selects a target inventory, adds an item, and submits the requisition.
        * The method ensures the requisition is successfully created by verifying the success message.
        * @expected
        * The inventory requisition should be successfully created and a success message should be displayed.
        */
        """
        pass
        assert False, "TODO: Implement create_inventory_requisition"

    def creating_consumption_section(self):
        """
        /**
        * @Test11
        * @description This method creates a new consumption section. It navigates through the Ward Supply module,
        * accesses the account and consumption sections, and opens the "New Consumption" form.
        * The function enters the item name, submits the form, and verifies the successful creation of the consumption
        * section by asserting that a success message becomes visible.
        * @return True if the consumption section is successfully created, otherwise False.
        */
        """
        pass
        assert False, "TODO: Implement creating_consumption_section"

    def creating_report_section(self):
        """
        /**
        * @Test12
        * @description This method creates a new report section in the Ward Supply module. It navigates through
        * the report section and selects the specified item name from the subcategory dropdown. After generating
        * the report, the function verifies if the selected item name is displayed in the report grid.
        * @return True if the item name is found in the report, otherwise False.
        */
        """
        pass
        assert False, "TODO: Implement creating_report_section"

