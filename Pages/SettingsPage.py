from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "Settings.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.settings_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.settings = {
            "settingsLink": (By.XPATH, '//a[@href="#/Settings"]'),
            "radiologySubmodule": (By.XPATH, '//a[@href="#/Settings/RadiologyManage" and contains(text(),"Radiology")]'),
            "addImagingTypeButton": (By.XPATH, '//a[text()="Add Imaging Type"]'),
            "imagingItemNameField": (By.ID, 'ImagingTypeName'),
            "addButton": (By.ID, 'Add'),
            "searchBar": (By.ID, 'quickFilterInput'),
            "dynamicTemplates": (By.XPATH, '(//a[@href="#/Settings/DynamicTemplates"])[2]'),
            "addTemplateButton": (By.XPATH, '//a[@id="id_btn_template_newTemplate"]'),
            "templateName": (By.XPATH, '//input[@placeholder="template name"]'),
            "templateType": (By.ID, 'TemplateTypeId'),
            "templateCode": (By.XPATH, '//input[@placeholder="enter template code"]'),
            "iframeLocator": (By.CSS_SELECTOR, 'iframe[title="Rich Text Editor, editor1"]'),
            "textField": (By.CSS_SELECTOR, 'html[dir="ltr"] body'),
            "typeOption": (By.XPATH, '//span[text()="Discharge Summary"]')
        }

    def verify_dynamic_templates(self):
        """
        /**
        * @Test5
        * @description This method verifies the creation of dynamic templates in the Settings module.
        * It navigates to the Dynamic Templates submodule, fills out the template details including
        * template type, name, code, and text field, and ensures the template is added successfully.
        * @expected
        * The template should be created successfully and appear in the templates list.
        */
        """
        pass
        assert False, "TODO: Implement verify_dynamic_templates"

