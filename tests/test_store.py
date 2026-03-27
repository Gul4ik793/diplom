import re

import allure
from playwright.sync_api import Page, expect

from pages.addrno import Addrno_Page
from pages.main_page import MainPage
from pages.el_usl_page import EL_USL_Page
from pages.lkfl_page import LKFL_Page
from pages.ops_page import OPS_Page
from pages.payment_fl_page import PaymentFL_Page


@allure.title("Тестирование сайта https://www.nalog.gov.ru/rn02/")
@allure.description("Тестирование сайта https://www.nalog.gov.ru/rn02/")
def test_stor_page(page: Page):
    mainpage = MainPage(page)
    el_usl = EL_USL_Page(page)
    lkfl = LKFL_Page(page)
    payment = PaymentFL_Page(page)
    ops = OPS_Page(page)
    addrno =Addrno_Page(page)

    with allure.step("Тест 0001: 'Сервисы и госуслуги'"):
        with allure.step("Шаг 1:Открыть  https://www.nalog.gov.ru/rn02/"):
            mainpage.open()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 2:В верхнем меню кликнуть  'Сервисы и госуслуги'" ):
            page.wait_for_timeout(1000)
            mainpage.get_headermenu().click_by_text_text("Сервисы и госуслуги")
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит «about_fts/el_usl»"):
            expect(page).to_have_url(re.compile('about_fts/el_usl'))

        with allure.step("Проверка: На странице присутствует блок «Личные кабинеты»"):
            page.wait_for_timeout(1000)
            block_name = el_usl.get_block().get_by_text_block("Личные кабинеты")
            page.wait_for_timeout(1000)
            expect(block_name).to_be_visible()

        with allure.step("Проверка: На странице отображается 14 блоков с сервисами"):
            const_block = el_usl.get_block().wrapper
            expect(const_block).to_have_count(14)

    with allure.step("Тест 0002: Сервис 'Личный кабинет для физических лиц'"):
        with allure.step("Шаг 1:Кликнуть на сервис «Личный кабинет для физических лиц»"):
            el_usl.get_block().click_by_text('Личный кабинет для физических лиц')
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  'lkfl'"):
            expect(page).to_have_url(re.compile('lkfl'))

        with allure.step("Шаг.2.Заполнить поля формы тестовыми данными "):
            lkfl.auth_form().fill_username('233')
            lkfl.auth_form().fill_password('233')
            page.wait_for_timeout(3000)

        with allure.step("Проверка: поля формы заполнены тестовыми данными"):
            username_input = lkfl.auth_form().get_username().wrapper
            password_input = lkfl.auth_form().get_password().wrapper
            expect(username_input).to_have_value('233')
            expect(password_input).to_have_value('233')

        with allure.step("Шаг 2: Нажать на кнопку «Войти»"):
            lkfl.auth_form().click_by_text('Войти')
            page.wait_for_timeout(3000)

        with allure.step("Проверка: На странице содержится сообщение об ошибке: ‘Указанный Вами ИНН отсутствует в Личном кабинете’"):
            expect(page.locator('[data-qa="auth-error-msg"]')).to_have_text(re.compile(r"Указанный Вами ИНН отсутствует в Личном кабинете"))

    with allure.step("Тест 0003: Проверка входа через Госуслуги(ЕСИА) Сервиса « Личный кабинет для физических лиц »"):
        with allure.step("Шаг 1:Кликнуть на кнопку «Войти через Госуслуги (ЕСИА)»"):
            lkfl.auth_form().click_by_text('Войти через Госуслуги (ЕСИА)')
            page.wait_for_timeout(3000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  'gosuslugi'"):
            expect(page).to_have_url(re.compile('gosuslugi'))

    with allure.step("Тест 0004: Сервис Уплата налогов и пошлин"):
        with allure.step("Шаг 1:Открыть  https://www.nalog.gov.ru/rn02/"):
            mainpage.open()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 2:В верхнем меню кликнуть  'Сервисы и госуслуги'" ):
            page.wait_for_timeout(1000)
            mainpage.get_headermenu().click_by_text_text("Сервисы и госуслуги")
            page.wait_for_timeout(1000)

        with allure.step("Шаг 3:Кликнуть на сервис «Уплата налогов и пошлин физических лиц»"):
            el_usl.get_block().click_by_text('Уплата налогов и пошлин физических лиц')
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  'payment'"):
            expect(page).to_have_url(re.compile('payment'))

    with allure.step("Тест 0005: Пополнение ЕНС физических лиц"):
        with allure.step("Шаг 1:Открыть  https://service.nalog.ru/payment/ens.html?payer=fl"):
            payment.open()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 2:Кликнуть на сервис «Пополнить ЕНС»"):
            payment.get_plate_container().click_by_text('Пополнить ЕНС')
            page.wait_for_timeout(3000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  'static'"):
            expect(page).to_have_url(re.compile('static'))

        with allure.step("Шаг 3:Кликнуть  чек бокс Я даю согласие на обработку персональных данных"):
            page.wait_for_timeout(1000)
            payment.click_unichk()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 4:Кликнуть «Продолжить»"):
            payment.click_button()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 5.Заполнить поля формы тестовыми данными "):
            payment.get_ens().fill_fioFl('Хасанова Гульчачак Валериевна')
            payment.get_ens().fill_innFl('026006198150')
            payment.get_ens().fill_sum('100')
            page.wait_for_timeout(1000)

        with allure.step("Проверка: поля формы заполнены тестовыми данными"):
            fioFl_input = payment.get_ens().get_fioFl().wrapper
            innFl_input = payment.get_ens().get_innFl().wrapper
            sum_input = payment.get_ens().get_sum().wrapper
            expect(fioFl_input).to_have_value('Хасанова Гульчачак Валериевна')
            expect(innFl_input).to_have_value('026006198150')
            expect(sum_input).to_have_value('100')
            page.wait_for_timeout(3000)

        with allure.step("Шаг 6. Нажать далее"):
            payment.get_ens().click_by_btnNext()
            page.wait_for_timeout(1000)

        with allure.step("Проверка: На странице присутствует заголовок «Сведения о лице, осуществляющем платеж»"):
            locator = page.locator("h2:has-text('Сведения о лице, осуществляющем платеж')")
            expect(locator).to_be_visible()
            expect(locator).to_have_text(re.compile("Сведения о лице, осуществляющем платеж"))

        with allure.step("Шаг 7. Нажать уплатить"):
            payment.get_ens().click_by_btnPay()
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  «pay»"):
            expect(page).to_have_url(re.compile('pay'))

    with allure.step("Тест 0006: Калькулятор расчёта страховых взносов"):
        with allure.step("Шаг 1:Открыть  https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
            el_usl.open()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 2:Кликнуть на сервис « Калькулятор расчёта страховых взносов »"):
            el_usl.get_block().click_by_text(' Калькулятор расчёта страховых взносов ')
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  «ops»"):
            expect(page).to_have_url(re.compile('ops'))

        with allure.step("Проверка: На странице присутствует заголовок «Калькулятор расчета страховых взносов»"):
            locator = page.locator("h1:has-text('Калькулятор расчета страховых взносов')")
            expect(locator).to_be_visible()
            expect(locator).to_have_text(re.compile("Калькулятор расчета страховых взносов"))

        with allure.step("Шаг 2.Заполнить поле «Расчетный период:» значением: 2025 "):
            ops.get_contentform().click_ddlYear()
            ops.get_ddlYear().fill("2025")
            ops.get_ddlYear().press("Enter")

        with allure.step("Шаг 3.Нажать кнопку «Рассчитать» "):
            ops.get_contentform().click_by_blue_button()
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  «https://www.nalog.gov.ru/rn02/service/ops/?y=2025&df=01.01.2025&dt=31.12.2025&v=&c=false&lp=false&nt=false»"):
            expect(page).to_have_url("https://www.nalog.gov.ru/rn02/service/ops/?y=2025&df=01.01.2025&dt=31.12.2025&v=&c=false&lp=false&nt=false")

    with allure.step("Тест 0007: Сервис Адрес и платежные реквизиты вашей инспекции"):
        with allure.step("Шаг 1:Открыть  https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
            el_usl.open()
            page.wait_for_timeout(1000)

        with allure.step("Шаг 2:Кликнуть на сервис «  Адрес и платежные реквизиты вашей инспекции »"):
            el_usl.get_block().click_by_text('Адрес и платежные реквизиты вашей инспекции')
            page.wait_for_timeout(1000)

        with allure.step("Проверка: Страница обновилась, url страницы содержит :  «addrno.do»"):
            expect(page).to_have_url(re.compile('addrno.do'))

        with allure.step("Проверка: На странице присутствует заголовок «Определение реквизитов ИФНС, органа государственной регистрации ЮЛ/ИП, обслуживающих данный адреc»"):
            locator = page.locator("h2:has-text('Определение реквизитов ИФНС, органа государственной регистрации ЮЛ/ИП, обслуживающих данный адрес')")
            expect(locator).to_be_visible()
            expect(locator).to_have_text(re.compile("Определение реквизитов ИФНС, органа государственной регистрации ЮЛ/ИП, обслуживающих данный адрес"))

        with allure.step("Шаг 3: Заполнить поле «Выберите код ИФНС» значением «уфа коммунистическая д. 59» и выбрать первый элемент из всплывающего меню"):
            addrno.get_card().fill_objectAddr("уфа коммунистическая д. 59")

        with allure.step("Шаг 4: Dыбрать первый элемент из всплывающего меню"):
            page.wait_for_selector("[data-object-id='44929801']")
            page.locator('[data-object-id="44929801"]').click()
            page.wait_for_timeout(10000)

        with allure.step("Проверка: На странице присутствует заголовок «Реквизиты ИФНС»"):
            locator = page.locator("h4:has-text('Реквизиты ИФНС')")
            expect(locator).to_be_visible()
            expect(locator).to_have_text(re.compile("Реквизиты ИФНС"))