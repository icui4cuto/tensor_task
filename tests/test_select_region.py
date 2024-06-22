from selenium import webdriver

from pages.sbis.contacts_page_sbis import ContactsPageSbis
from pages.sbis.main_page_sbis import MainPageSbis


def test_select_region(set_up):
    """ В данном тесте осуществляется:
     1. Проверка правильности выбора нашего региона "Нижегородская область" и список партнеров
     2. Проверка возможности выбора другого региона "Камчатский край"
     3. Проверка, содержит ли url и title страницы информацию о выбранном регионе """

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("—disable-popup-blocking")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    # Переход в раздел 'Контакты'
    mps = MainPageSbis(driver)
    mps.open_main_page()
    mps.open_contacts()

    # Проверяем, что наш регион определился правильно (Нижегородская обл.) и есть список партнеров
    cps = ContactsPageSbis(driver)
    cps.check_region("Нижегородская обл.", "Нижний Новгород", "52")

    # Выбираем регион "Камчатский край" и проверяем, что подставился нужный регион и список партнеров
    cps.select_region()
    cps.check_region("Камчатский край", "Петропавловск-Камчатский", "41")

