import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class ContactsPageSbis(Base):
    """ Страница 'Контакты' """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    tensor_banner = "(//a[@title='tensor.ru'])[1]"
    region = "(//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link'])[1]"
    partner_list = "//div[@id='city-id-2']"
    kamchatka_region = "//span[contains(text(), '41 Камчатский край')]"

    # Getters
    def get_tensor_banner(self):
        """ Получение локатора баннера 'Тензор' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.tensor_banner)))

    def get_region(self):
        """ Получение локатора региона """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.region)))

    def get_partner_list(self):
        """ Получение локатора списка партнеров """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.partner_list)))

    def get_kamchatka_region(self):
        """ Получение локатора Камчатского края в списке регионов """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.kamchatka_region)))

    # Actions
    def click_tensor_banner(self):
        """ Клик по баннеру 'Tensor' """
        self.get_tensor_banner().click()
        print("Click tensor banner")

    def click_region_list(self):
        """ Клик по списку регионов """
        self.get_region().click()
        print("Click region list")

    def select_kamchatka_region(self):
        """ Выбор Камчатского края в списке регионов """
        self.get_kamchatka_region().click()
        print("Select region - 'Камчатский край'")

    # Methods
    def open_tensor(self):
        """ Переходим на страницу Tensor.ru"""
        Logger.add_start_step(method="open_tensor")
        self.click_tensor_banner()
        Logger.add_end_step(url=self.driver.current_url, method="open_tensor")

    def check_region(self, region, partner_list, region_id):
        """ Проверка региона и наличия списка партнеров """
        Logger.add_start_step(method="check_region")
        try:
            self.get_current_url()
            print("Selected region:", end=' ')
            time.sleep(2)
            self.assert_word(self.get_region(), region)
            print("Check partner list:", end=' ')
            self.assert_word(self.get_partner_list(), partner_list)
            self.assert_title(region)
            self.assert_region_url(region_id)
        except StaleElementReferenceException:
            self.driver.refresh()

        Logger.add_end_step(url=self.driver.current_url, method="check_region")

    def select_region(self):
        """ Выбор региона """
        Logger.add_start_step(method="select_region")
        self.click_region_list()
        self.select_kamchatka_region()
        Logger.add_end_step(url=self.driver.current_url, method="select_region")