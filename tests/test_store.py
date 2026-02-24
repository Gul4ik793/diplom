import re

import allure
from playwright.sync_api import Page, expect

from pages.main_page import MainPage
from pages.el_usl_page import EL_USL_Page
from pages.lkfl_page import LKFL_Page


@allure.title("Тестирование сайта https://www.demoblaze.com/")
@allure.description("Тестирование сайта https://www.demoblaze.com/")
def test_stor_page(page: Page):
    mainpage = MainPage(page)
    el_usl = EL_USL_Page(page)
    lkfl = LKFL_Page(page)

    with allure.step("Открытие главной страницы сайта"):
        mainpage.open()
        page.wait_for_timeout(1000)

    with allure.step("Кликнуть Сервисы и госуслуги"):
        page.wait_for_timeout(1000)
        mainpage.get_headermenu().click_by_text_text("Сервисы и госуслуги")
        page.wait_for_timeout(1000)

    with allure.step("Проверка: url страницы содержит 'about_fts/el_usl'"):
        expect(page).to_have_url(re.compile('about_fts/el_usl'))

    with allure.step("Прверка: На странице присутствует блок «Личные кабинеты»."):
        page.wait_for_timeout(1000)
        block_name = el_usl.get_block().get_by_text_block("Личные кабинеты")
        page.wait_for_timeout(1000)
        expect(block_name).to_be_visible()

    with allure.step("Проверка: На странице отображается 14 блоков с сервисами"):
        const_block = el_usl.get_block().wrapper
        expect(const_block).to_have_count(14)

    with allure.step("Кликнуть на сервис «Личный кабинет для физических лиц» "):
        el_usl.get_block().click_by_text('Личный кабинет для физических лиц')
        page.wait_for_timeout(1000)

    with allure.step("Проверка: url страницы содержит 'lkfl'"):
        expect(page).to_have_url(re.compile('lkfl'))

    with allure.step("Ввести значение «abc» на поле ввода  Логин (Ваш ИНН)"):
        lkfl.auth_form().fill_username('233')

    with allure.step("Ввести значение «abc» на поле ввода  Пароль"):
        lkfl.auth_form().fill_password('233')
        page.wait_for_timeout(3000)

    #
    # with allure.step("Внизу страницы кликнуть на кнопку пагинатора «Next»"):
    #     stor_page.get_pagination().click_by_text('Next')
    #     page.wait_for_timeout(1000)
    #
    # with allure.step("Прверка: На странице присутствует товар с наименованием «MacBook air»"):
    #     macbookair = stor_page.get_tbodyid().get_by_text_tbodyid('MacBook air')
    #     expect(macbookair).to_be_visible()
    #
    # with allure.step("Кликнуть на товар с наименованием «MacBook air»"):
    #     page.wait_for_timeout(1000)
    #     stor_page.get_tbodyid().click_by_text('MacBook air')
    #
    # with allure.step("Проверка: URL страницы включает prod.html?idp_ = 11"):
    #     expect(page).to_have_url(re.compile('prod.html\\?idp_=11'))
    #
    # with allure.step("Проверка: На странице присутствует заголовок «MacBook air»"):
    #     expect(page.locator("h2")).to_have_text('MacBook air')
    #
    # with allure.step("Записать цену товара в переменную macPrice"):
    #     macPrice = page.locator("h3").inner_text()
    #
    # with allure.step("Нажать на кнопку «Add to cart»"):
    #     page.wait_for_timeout(1000)
    #     product_page.get_tbodyid().click_by_text("Add to cart")
    #     page.wait_for_timeout(1000)
    #
    # with allure.step("В верхнем меню кликнуть по пункту «Cart» "):
    #     stor_page.get_narvbarx().click_by_text('Cart')
    #     page.wait_for_timeout(2000)
    #
    # with allure.step("Проверка: URL страницы включает cart"):
    #     expect(page).to_have_url(re.compile('cart'))
    #
    # with allure.step("Проверка: Присутствует название товара «MacBook air»"):
    #      product_name_locator = cart_page.get_cart().get_nameproduct().wrapper
    #      expect(product_name_locator).to_contain_text('MacBook air')
    #
    # # with allure.step("Проверка: Цена всего заказа равна значению из переменной macPrice "):
    # #     page.wait_for_timeout(2000)
    # #     print(page.locator("h3").inner_text())
    # #     print(macPrice)
    # #     expect(page.locator("h3")).to_contain_text(str(macPrice))
    #
    # with allure.step("Кликнуть по кнопке «Price Order» "):
    #     cart_page.get_cart().click_cart()
    #     page.wait_for_timeout(2000)
    #
    # with allure.step("Проверка: На странице присутствует форма оформления заказа "):
    #     page.wait_for_timeout(2000)
    #     expect(page.locator("#orderModalLabel")).to_be_visible()
    #
    # with allure.step("Заполнить поля формы тестовыми данными"):
    #     cart_page.get_formprice().get_form_name().fill('Вася')
    #     cart_page.get_formprice().get_form_city().fill('Уфа')
    #     cart_page.get_formprice().get_form_card().fill('1234 5678')
    #     page.wait_for_timeout(3000)
    #
    # with allure.step("Кликнуть по кнопке «Purchase» "):
    #     cart_page.get_formprice().click_by_text('Purchase')
    #     page.wait_for_timeout(2000)
    #
    # with allure.step('На странице присутствует сообщение «Thank you for your purchase!»'):
    #     locator = page.get_by_role("heading", name="Thank you for your purchase!")
    #     expect(locator).to_be_visible()
    #
    # with allure.step('Кликнуть по кнопке «ОК» в окне об успешном заказе'):
    #     cart_page.get_confirm().click_ok('ОК')
    #
    # with allure.step("Проверка: URL страницы включает index"):
    #     expect(page).to_have_url(re.compile('index'))