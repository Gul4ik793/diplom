from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class PaymentEdit(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator("#pnlPaymentEdit"))

    def get_btnNext(self):
        return ButtonControl(self.page, self.wrapper.locator("#btnNext"))

    def get_btnPay(self):
        return ButtonControl(self.page, self.wrapper.locator("#btnPay"))

    def get_region(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_1'))

    def get_oktmmf(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_6'))

    def get_kbk(self):
        return InputControl(self.page, self.wrapper.locator('#kbk'))

    def get_kbkGroup(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_11'))

    def get_kbkNoProg(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_16'))

    def get_kbkProg(self):
        return InputControl(self.page, self.wrapper.locator('#uni_select_21'))

    def get_fioFl(self):
        return InputControl(self.page, self.wrapper.locator('#fioFl'))

    def get_innFl(self):
        return InputControl(self.page, self.wrapper.locator('#innFl'))

    def get_sum(self):
        return InputControl(self.page, self.wrapper.locator('#sum'))