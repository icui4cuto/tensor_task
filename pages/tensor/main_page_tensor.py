from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPageTensor(Base):
    """ Главная страница """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    power_in_people = "//p[contains(text(), 'Сила в людях')]"
    about_link = "//p[@class='tensor_ru-Index__card-text']/a[@href='/about']"

    # Getters
    def get_power_in_people(self):
        """ Получение локатора блока 'Сила в людях' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.power_in_people)))

    def get_about_link(self):
        """ Получение локатора ссылки 'Подробнее' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.about_link)))

    # Actions
    def click_about_link(self):
        """ Клик по ссылке 'Подробнее' """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_about_link())
        self.driver.execute_script("arguments[0].click();", self.get_about_link())
        print("Click about link")

    # Methods
    def check_tensor_block(self):
        """ Проверяем есть ли блок 'Сила в людях' """
        Logger.add_start_step(method="check_tensor_block")
        try:
            self.get_current_url()
            print("Block 'Сила в людях':", end=' ')
            self.assert_word(self.get_power_in_people(), "Сила в людях")
        except StaleElementReferenceException:
            self.driver.refresh()
        Logger.add_end_step(url=self.driver.current_url, method="check_tensor_block")

    def open_about(self):
        """ Переход на страницу 'Подробнее' """
        Logger.add_start_step(method="open_about")
        self.click_about_link()
        self.assert_url("https://tensor.ru/about")
        Logger.add_end_step(url=self.driver.current_url, method="open_about")
