from selenium import webdriver

from pages.sbis.contacts_page_sbis import ContactsPageSbis
from pages.sbis.main_page_sbis import MainPageSbis
from pages.tensor.about_page_tensor import AboutPageTensor
from pages.tensor.main_page_tensor import MainPageTensor


def test_block_and_image(set_up):
    """ В данном тесте осуществляется:
     1. Проверка наличия блока 'Сила в людях' на странице https://tensor.ru/
     2. Правильность перехода по ссылке 'Подробнее' на страницу https://tensor.ru/about
     3. Проверка, имеют ли изображения в блоке 'Работаем' одинаковые параметры 'height' и 'weight' """

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("start-maximized")
    options.add_argument("—disable-popup-blocking")
    driver = webdriver.Chrome(options=options)

    # Переход в раздел 'Контакты'
    mps = MainPageSbis(driver)
    mps.open_main_page()
    mps.open_contacts()

    # Переход на 'tensor.ru'
    cps = ContactsPageSbis(driver)
    cps.open_tensor()

    # Переключаемся на вкладку Tensor.ru
    driver.switch_to.window(driver.window_handles[1])

    # Проверка наличия блока 'Сила в людях' и переход на страницу https://tensor.ru/about
    mpt = MainPageTensor(driver)
    mpt.check_tensor_block()
    mpt.open_about()

    # Проверка, имеют ли изображения в блоке 'Работаем' одинаковые параметры 'height' и 'weight'
    abt = AboutPageTensor(driver)
    abt.check_img_size()
