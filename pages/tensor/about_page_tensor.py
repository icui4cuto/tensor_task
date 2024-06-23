import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class AboutPageTensor(Base):
    """ Страница 'О компании' """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    development_sbis_img = "//img[@alt='Разрабатываем систему СБИС']"
    promoting_service_img = "//img[@alt='Продвигаем сервисы']"
    creating_infrastructure_img = "//img[@alt='Создаем инфраструктуру']"
    accompany_clients_img = "//img[@alt='Сопровождаем клиентов']"

    # Getters
    def get_development_sbis_img(self):
        """ Получение WebElement изображения 'Разрабатываем систему СБИС' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.development_sbis_img)))

    def get_promoting_service_img(self):
        """ Получение WebElement изображения 'Продвигаем сервисы' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.promoting_service_img)))

    def get_creating_infrastructure_img(self):
        """ Получение WebElement изображения 'Создаем инфраструктуру' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.creating_infrastructure_img)))

    def get_accompany_clients_img(self):
        """ Получение WebElement изображения 'Сопровождаем клиентов' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.accompany_clients_img)))

    # Methods
    def check_img_size(self):
        """ Проверка, имеют ли изображения в блоке 'Работаем' одинаковые параметры 'height' и 'weight' """
        with allure.step("check_img_size"):
            Logger.add_start_step(method="check_img_size")
            self.get_current_url()
            self.assert_img_size(self.get_development_sbis_img(), self.get_promoting_service_img(),
                                 self.get_creating_infrastructure_img(), self.get_accompany_clients_img())
            Logger.add_end_step(url=self.driver.current_url, method="check_img_size")
