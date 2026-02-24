from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class ButtonControl(BaseControl):
    def __init__(self, page: Page, wrapper: Locator):
        '''
            Берет кнопки
        '''
        super().__init__(page, wrapper)