import re

import allure
from playwright.sync_api import Page, expect

from pages.addrno import Addrno_Page
from pages.invalid_inn_fl import Invalidinnfl_Page
from pages.main_page import MainPage
from pages.el_usl_page import EL_USL_Page
from pages.lkfl_page import LKFL_Page
from pages.ops_page import OPS_Page
from pages.payment_fl_page import PaymentFL_Page


@allure.title("Тест 0001: Сервисы и госуслуги. Открытие главной страницы и проверка блока «Личные кабинеты")
def test_open_main_page_and_check_block(page: Page):
    mainpage = MainPage(page)
    el_usl = EL_USL_Page(page)

    with allure.step("Шаг 1: Открыть https://www.nalog.gov.ru/rn02/"):
        mainpage.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: В верхнем меню кликнуть 'Сервисы и госуслуги'"):
        mainpage.get_headermenu().get_by_text("Сервисы и госуслуги").click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('about_fts/el_usl'))
        expect(el_usl.get_block().get_by_text_block("Личные кабинеты")).to_be_visible()
        expect(el_usl.get_block().wrapper).to_have_count(14)

@allure.title("Тест 0002: Вход в личный кабинет для физических лиц")
def test_login_physical_person(page: Page):
    el_usl = EL_USL_Page(page)
    lkfl = LKFL_Page(page)

    with allure.step("Шаг 1: Открыть https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
        el_usl.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис «Личный кабинет для физических лиц»"):
        el_usl.get_block().get_by_text_block('Личный кабинет для физических лиц').click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('lkfl'))

    with allure.step("Шаг 3: Заполнить поля формы тестовыми данными"):
        lkfl.auth_form().get_username().fill('233')
        lkfl.auth_form().get_password().fill('233')
        page.wait_for_timeout(500)
        expect(lkfl.auth_form().get_username().wrapper).to_have_value('233')
        expect(lkfl.auth_form().get_password().wrapper).to_have_value('233')
        page.wait_for_timeout(500)

    with allure.step("Шаг 4: Нажать на кнопку «Войти»"):
        lkfl.auth_form().get_button_by_text('Войти').click()
        page.wait_for_load_state()
        expect(lkfl.auth_form().get_error()).to_have_text(re.compile(r"Указанный Вами ИНН отсутствует в Личном кабинете"))

@allure.title("Тест 0003: Проверка входа через Госуслуги(ЕСИА) Сервиса « Личный кабинет для физических лиц »")
def test_login_gosuslugi(page: Page):
    lkfl = LKFL_Page(page)

    with allure.step("Шаг 1: Открыть  https://lkfl2.nalog.ru/lkfl/"):
        lkfl.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Клик на кнопку «Войти через Госуслуги (ЕСИА)»"):
        lkfl.auth_form().get_button_by_text('Войти через Госуслуги (ЕСИА)').click()
        page.wait_for_url(re.compile('gosuslugi'), timeout=10000)

@allure.title("Тест 0004: Проверка сервиса Уплата налогов и пошлин")
def test_payment_service(page: Page):
    el_usl = EL_USL_Page(page)

    with allure.step("Шаг 1: Открыть https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
        el_usl.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Выбрать сервис 'Уплата налогов и пошлин физических лиц'"):
        el_usl.get_block().get_by_text_block('Уплата налогов и пошлин физических лиц').click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('payment'))

@allure.title("Тест 0005: Пополнение ЕНС физических лиц")
def test_replenish_ENS(page: Page):
    payment = PaymentFL_Page(page)

    with allure.step("Шаг 1: Открыть https://service.nalog.ru/payment/#fl"):
        payment.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис 'Пополнить ЕНС'"):
        payment.get_plate_container().get_by_text_block('Пополнить ЕНС').click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('static'))

    with allure.step("Шаг 3: Кликнуть  чек бокс Я даю согласие на обработку персональных данных"):
        payment.click_unichk()
        page.wait_for_load_state()

    with allure.step("Шаг 4:Кликнуть «Продолжить»"):
        payment.click_btnContinue()
        page.wait_for_load_state()

    with allure.step("Шаг 5: Заполнить поля формы тестовыми данными"):
        payment.get_ens().get_fioFl().fill('Хасанова Гульчачак Валериевна')
        payment.get_ens().get_innFl().fill('026006198150')
        payment.get_ens().get_sum().fill('100')
        page.wait_for_timeout(500)
        expect(payment.get_ens().get_fioFl().wrapper).to_have_value('Хасанова Гульчачак Валериевна')
        expect(payment.get_ens().get_innFl().wrapper).to_have_value('026006198150')
        expect(payment.get_ens().get_sum().wrapper).to_have_value('100')

    with allure.step("Шаг 6: Нажать кнопку 'Далее'"):
        payment.get_ens().get_btnNext().click()
        page.wait_for_timeout(500)
        expected_header = "Сведения о лице, осуществляющем платеж"
        header_locator = payment.get_header_locator(expected_header)
        expect(header_locator).to_be_visible(timeout=5000)

    with allure.step("Шаг 7: Нажать кнопку 'Уплатить'"):
        payment.get_ens().get_btnPay().click()
        page.wait_for_timeout(500)
        expect(page).to_have_url(re.compile('pay'))

@allure.title("Тест 0006: Уплата госпошлины")
def test_replenish_payment(page: Page):
    payment = PaymentFL_Page(page)

    with allure.step("Шаг 1: Открыть https://service.nalog.ru/payment/#fl"):
        payment.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис 'Уплата госпошлины'"):
        payment.get_plate_container().get_by_text_block('Уплата госпошлины').click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('static'))

    with allure.step("Шаг 3: Кликнуть  чек бокс Я даю согласие на обработку персональных данных"):
        payment.click_unichk()
        page.wait_for_load_state()

    with allure.step("Шаг 4:Кликнуть «Продолжить»"):
        payment.click_btnContinue()
        page.wait_for_load_state()

    with allure.step("Шаг 5: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля вид платежа"):
        payment.get_form_labels().get_kbkGroup().click()

    with allure.step("Шаг 6: Выбрать Плата за предоставление информации из реестра дисквалифицированных лиц из всплывающего меню"):
        expected_disq = "Плата за предоставление информации из реестра дисквалифицированных лиц"
        header_disq = payment.get_li_locator(expected_disq)
        expect(header_disq).to_be_visible(timeout=5000)

    with allure.step("Шаг 7: Кликнуть Плата за предоставление информации из реестра дисквалифицированных лиц"):
        header_disq.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 8: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Тип платежа"):
        payment.get_form_labels().get_kbkProg().click()

    with allure.step("Шаг 9: Выбрать Платёж из всплывающего меню"):
        expected_payment = "Платёж"
        header_payment = payment.get_li_locator(expected_payment)
        expect(header_payment).to_be_visible(timeout=5000)

    with allure.step("Шаг 10: Кликнуть Платёж"):
        header_payment.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 11: нажать кнопку « Далее»"):
        payment.get_form_labels().get_button_next().click()
        page.wait_for_load_state()
        expected_step_PAYEE = "ОКТМО получателя платежа"
        header_step_PAYEE = payment.get_header_locator(expected_step_PAYEE)
        expect(header_step_PAYEE).to_be_visible(timeout=5000)
        page.wait_for_timeout(1000)

    with allure.step("Шаг 12: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Регион"):
        payment.get_form_labels().get_region().click()
        page.wait_for_timeout(500)

    with allure.step("Шаг 13: Выбрать 02 из всплывающего меню"):
        expected_region = "02 - БАШКОРТОСТАН РЕСП"
        header_region = payment.get_form_labels().get_li_locator(expected_region)
        expect(header_region).to_be_visible(timeout=5000)

    with allure.step("Шаг 14: Кликнуть 02 - БАШКОРТОСТАН РЕСП"):
        header_region.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 15: нажать кнопку « Далее»"):
        payment.get_form_labels().get_button_next().click()
        page.wait_for_load_state()
        expected_step_PAYER = "Сведения о лице, осуществляющем платеж"
        header_step_PAYER = payment.get_header_locator(expected_step_PAYER)
        expect(header_step_PAYER).to_be_visible(timeout=5000)
        page.wait_for_timeout(1000)

    with allure.step("Шаг 16: Заполнить форму данными"):
        payment.get_form_labels().get_fioFl().fill('Хасанова Гульчачак Валериевна')
        payment.get_form_labels().get_innFl().fill('026006198150')
        page.wait_for_timeout(1000)
        expect(payment.get_form_labels().get_fioFl().wrapper).to_have_value('Хасанова Гульчачак Валериевна')
        expect(payment.get_form_labels().get_innFl().wrapper).to_have_value('026006198150')

    with allure.step("Шаг 17: нажать кнопку « Далее»"):
        payment.get_form_labels().get_button_next().click()
        page.wait_for_load_state()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 18: нажать кнопку « Уплатить»"):
        payment.get_form_labels().get_button_btnPay().click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('pay'))

@allure.title("Тест 0007: Уплата по реквизитам")
def test_replenish_noENS(page: Page):
    payment = PaymentFL_Page(page)

    with allure.step("Шаг 1: Открыть https://service.nalog.ru/payment/#fl"):
        payment.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис 'Уплата по реквизитам'"):
        payment.get_plate_container().get_by_text_block('Уплата по реквизитам').click()
        expect(page).to_have_url(re.compile('static'))

    with allure.step("Шаг 3: Кликнуть  чек бокс Я даю согласие на обработку персональных данных"):
        payment.click_unichk()
        page.wait_for_load_state()

    with allure.step("Шаг 4:Кликнуть «Продолжить»"):
        payment.click_btnContinue()
        page.wait_for_load_state()

    with allure.step("Шаг 5: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Регион"):
        payment.get_paymentedit().get_region().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 6: Выбрать 02 - БАШКОРТОСТАН РЕСП из всплывающего меню"):
        expected_region = "02 - БАШКОРТОСТАН РЕСП"
        header_region = payment.get_paymentedit().get_li_locator(expected_region)
        expect(header_region).to_be_visible(timeout=5000)

    with allure.step("Шаг 7: Кликнуть 02 - БАШКОРТОСТАН РЕСП"):
        header_region.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 8: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Код ОКТМО"):
        payment.get_paymentedit().get_oktmmf().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 9: Выбрать 80701000 - город Уфа из всплывающего меню"):
        expected_oktmmf = "80701000 - город Уфа"
        header_oktmmf = payment.get_paymentedit().get_li_locator(expected_oktmmf)
        expect(header_oktmmf).to_be_visible(timeout=5000)

    with allure.step("Шаг 10: Кликнуть 80701000 - город Уфа"):
        header_oktmmf.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 11: нажать кнопку « Далее»"):
        payment.get_paymentedit().get_btnNext().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 12: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Вид платежа"):
        payment.get_paymentedit().get_kbkGroup().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 13: Выбрать Налоги, сборы и регулярные платежи за пользование  из всплывающего меню"):
        expected_kbkGroup = "Налоги, сборы и регулярные платежи за пользование "
        header_kbkGroup = payment.get_paymentedit().get_li_locator(expected_kbkGroup)
        expect(header_kbkGroup).to_be_visible(timeout=5000)

    with allure.step("Шаг 14: Кликнуть Налоги, сборы и регулярные платежи за пользование"):
        header_kbkGroup.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 15: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Наименование платежа:"):
        payment.get_paymentedit().get_kbkNoProg().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 16: Выбрать Сбор за пользование объектами животного мира из всплывающего меню"):
        expected_kbkNoProg = "Сбор за пользование объектами животного мира"
        header_kbkNoProg = payment.get_paymentedit().get_li_locator(expected_kbkNoProg)
        expect(header_kbkNoProg).to_be_visible(timeout=5000)

    with allure.step("Шаг 17: Кликнуть Сбор за пользование объектами животного мира"):
        header_kbkNoProg.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 18: Нажать кнопку Dropdown arrow (стрелка раскрывающегося меню) поля Тип платежа:"):
        payment.get_paymentedit().get_kbkProg().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 19: Выбрать Платёж из всплывающего меню"):
        expected_payment = "Платёж"
        header_payment = payment.get_paymentedit().get_li_locator(expected_payment)
        expect(header_payment).to_be_visible(timeout=5000)

    with allure.step("Шаг 20: Кликнуть Платёж"):
        header_payment.click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 21: нажать кнопку « Далее»"):
        payment.get_form_labels().get_button_next().click()
        page.wait_for_load_state()

    with allure.step("Шаг 22: Заполнить форму данными"):
        payment.get_paymentedit().get_fioFl().fill('Хасанова Гульчачак Валериевна')
        payment.get_paymentedit().get_innFl().fill('026006198150')
        payment.get_paymentedit().get_sum().fill('100')
        expect(payment.get_paymentedit().get_fioFl().wrapper).to_have_value('Хасанова Гульчачак Валериевна')
        expect(payment.get_paymentedit().get_innFl().wrapper).to_have_value('026006198150')
        expect(payment.get_paymentedit().get_sum().wrapper).to_have_value('100')

    with allure.step("Шаг 23: нажать кнопку « Далее»"):
        payment.get_paymentedit().get_btnNext().click()
        page.wait_for_timeout(1000)

    with allure.step("Шаг 24: нажать кнопку « Уплатить»"):
        payment.get_paymentedit().get_btnPay().click()
        page.wait_for_timeout(1000)
        expect(page).to_have_url(re.compile('pay'))

@allure.title("Тест 0008: Калькулятор расчёта страховых взносов")
def test_calculator_strakh_vznosov(page: Page):
    el_usl = EL_USL_Page(page)
    ops = OPS_Page(page)

    with allure.step("Шаг 1: Открыть страницу  https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
        el_usl.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис « Калькулятор расчёта страховых взносов »"):
        el_usl.get_block().get_by_text_block(' Калькулятор расчёта страховых взносов ').click()

    with allure.step("Проверка: Страница обновилась, url страницы содержит :  «ops»"):
        expect(page).to_have_url(re.compile('ops'))
        expected_calc = "Калькулятор расчета страховых взносов"
        header_calc = ops.get_header_locator(expected_calc)
        expect(header_calc).to_be_visible(timeout=5000)

    with allure.step("Шаг 3: Заполнить поле «Расчетный период:» значением: 2025"):
        ops.get_contentform().get_ddlYear().click()
        ops.get_ddlYear().fill("2025")
        ops.get_ddlYear().press("Enter")
        page.wait_for_timeout(500)

    with allure.step("Шаг 4: Нажать кнопку «Рассчитать»"):
        ops.get_contentform().get_blue_button().click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('y=2025'))

@allure.title("Тест 0009: Сервис Адрес и платежные реквизиты вашей инспекции")
def test_address_requisites(page: Page):
    el_usl = EL_USL_Page(page)
    addrno = Addrno_Page(page)

    with allure.step("Шаг 1: Открыть  https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
        el_usl.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис «  Адрес и платежные реквизиты вашей инспекции »"):
        el_usl.get_block().get_by_text_block('Адрес и платежные реквизиты вашей инспекции').click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('addrno.do'))
        expected_addrno = "Определение реквизитов ИФНС, органа государственной регистрации ЮЛ/ИП, обслуживающих данный адрес"
        header_addrno = addrno.get_card().get_h2_locator(expected_addrno)
        expect(header_addrno).to_be_visible(timeout=5000)
        expect(header_addrno).to_have_text(re.compile("Определение реквизитов ИФНС, органа государственной регистрации ЮЛ/ИП, обслуживающих данный адрес"))

    with allure.step("Шаг 3: Заполнить поле «Выберите код ИФНС» значением «уфа коммунистическая д. 59» и выбрать первый элемент из всплывающего меню"):
        addrno.get_card().get_objectAddr().fill("уфа коммунистическая д. 59")

    with allure.step("Шаг 4: Выбрать первый элемент из всплывающего меню"):
        addrno.get_card().get_u3fieldoptions().click()
        page.wait_for_load_state()
        expected_Ifns = "Реквизиты ИФНС"
        header_Ifns = addrno.get_card().get_h4_locator(expected_Ifns)
        expect(header_Ifns).to_be_attached(timeout=5000)
        expect(header_Ifns).to_have_text(re.compile("Реквизиты ИФНС"))

@allure.title("Тест 0010: Сервис Сведения о недействительных ИНН физических лиц")
def test_verification_Invalidinnfl(page: Page):
    el_usl = EL_USL_Page(page)
    invalidinnfl = Invalidinnfl_Page(page)

    with allure.step("Шаг 1: Открыть  https://www.nalog.gov.ru/rn02/about_fts/el_usl/"):
        el_usl.open()
        page.wait_for_load_state()

    with allure.step("Шаг 2: Кликнуть на сервис «  Сведения о недействительных ИНН физических лиц »"):
        el_usl.get_block().get_by_text_block('Сведения о недействительных ИНН физических лиц').click()
        page.wait_for_load_state()
        expect(page).to_have_url(re.compile('invalid-inn-fl'))

    with allure.step("Шаг 3: Кликнуть в поле ИНН"):
        invalidinnfl.get_inn().click()

    with allure.step("Шаг 4: В поле ИНН вести значение 026006198150"):
        invalidinnfl.get_inn().fill("026006198150")
        expect(invalidinnfl.get_inn().wrapper).to_have_value('026006198150')

    with allure.step("Шаг 5: нажать кнопку « Выполнить проверку ИНН»"):
        invalidinnfl.get_btn_with_icon_search().click()
        page.wait_for_load_state()
        expect(invalidinnfl.det_Result()).to_have_text(re.compile(r"Информация не найдена"))

