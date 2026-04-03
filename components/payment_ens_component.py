from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class Payment_ens(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator("#pnlPaymentEns"))

    def get_btnNext(self):
        return ButtonControl(self.page, self.wrapper.locator("#btnNext"))

    def get_btnPay(self):
        return ButtonControl(self.page, self.wrapper.locator("#btnPay"))

    def get_by_text_block(self, text: str):
        return self.wrapper.get_by_text(text)

    def get_fioFl(self):
        return InputControl(self.page, self.wrapper.locator('[name="fioFl"]'))

    def get_innFl(self):
        return InputControl(self.page, self.wrapper.locator('[name="innFl"]'))

    def get_sum(self):
        return InputControl(self.page, self.wrapper.locator('[name="sum"]'))

