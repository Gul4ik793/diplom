from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class InputControl(BaseControl):
    '''
    Берет кнопки ввода
    '''
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def fill(self, text):
        self.wrapper.fill(text)

    def press(self, text):
        self.wrapper.press(text)