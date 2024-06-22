import os
from selenium import webdriver

from pages.sbis.download_page_sbis import DownloadPageSbis
from pages.sbis.main_page_sbis import MainPageSbis


def test_download_file(set_up):
    """ В данном тесте осуществляется:
     1. Скачивание файла веб-установщика
     2. Наличие файла в директории с тестом
     3. Проверка, совпадает ли размер файла с размером указанным на сайте """

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.getcwd(), "download.directory_upgrade": True,
             'safebrowsing.enabled': True}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("—disable-popup-blocking")
    driver = webdriver.Chrome(options=options)

    # Открываем главную страницу
    mps = MainPageSbis(driver)
    mps.open_main_page()

    # Переходим на страницу загрузок
    mps.open_download_page()

    # Скачиваем файл, проверяем нахождение его в директории и размер
    dps = DownloadPageSbis(driver)
    dps.downloads()
