from playwright.sync_api import Page

from components.payment_ens_component import Payment_ens
from components.platecontaine_component import Platecontaine
from controls.button_control import ButtonControl
from pages.base_page import BasePage


class PaymentFL_Page(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://service.nalog.ru/payment/#fl")

    def get_plate_container(self):
        return Platecontaine(self.page)

    def get_ens(self):
        return Payment_ens(self.page)

    def click_unichk(self):
        ButtonControl(self.page, self.page.locator("#unichk_0")).click()

    def click_button(self):
        ButtonControl(self.page, self.page.locator("#btnContinue")).click()