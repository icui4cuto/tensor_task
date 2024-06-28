import os
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class DownloadPageSbis(Base):
    """ Страница загрузки файлов """
    file_path = f"{os.getcwd()}\\sbisplugin-setup-web-standart.exe"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    download = "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']"

    # Getters
    def get_download(self):
        """ Получение WebElement ссылки на файл веб-установщика """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.download)))

    # Actions
    def click_download(self):
        """ Клик по ссылке 'Скачать' """
        self.get_download().click()
        print("Click download")

    def value_file_size(self):
        """ Получение значения размера файла """
        return self.get_download().text

    # Methods
    def downloads(self):
        """ Скачиваем и проверяем файл """
        with allure.step("downloads"):
            Logger.add_start_step(method="downloads")
            if not os.access(self.file_path, os.F_OK):
                self.click_download()
                for s in range(0, 30, 5):
                    if os.access(self.file_path, os.F_OK):
                        break
                    else:
                        time.sleep(s)
            self.assert_file_in_directory(self.file_path)
            self.assert_file_size(self.file_path, self.value_file_size())
            Logger.add_end_step(url=self.driver.current_url, method="downloads")





