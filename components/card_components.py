from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.input_control import InputControl


class Card(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator(".card-body.p-4"))

    def get_objectAddr(self):
        return InputControl(self.page, self.wrapper.locator('[name="objectAddr"]'))