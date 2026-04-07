from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class Form_labels(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator("#pnlPaymentEns"))

    def get_li_locator(self, header_text: str):
        return self.page.locator(f"li:has-text('{header_text}')")

    def get_header_locator(self, header_text: str):
        return self.page.locator(f"h2:has-text('{header_text}')")

    def get_kbk(self):
        return InputControl(self.page, self.wrapper.locator('#kbk'))

    def get_kbkGroup(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_1'))

    def get_kbkProg(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_11'))

    def get_region(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_21'))

    def get_fioFl(self):
        return InputControl(self.page, self.wrapper.locator('#fioFl'))

    def get_innFl(self):
        return InputControl(self.page, self.wrapper.locator('#innFl'))

    def get_button_next(self):
        return ButtonControl(self.page, self.page.locator("#btnNext"))

    def get_button_btnPay(self):
        return ButtonControl(self.page, self.wrapper.locator('#btnPay'))