from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class AboutPageTensor(Base):
    """ Главная страница """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    img_1 = "//img[@alt='Разрабатываем систему СБИС']"
    img_2 = "//img[@alt='Продвигаем сервисы']"
    img_3 = "//img[@alt='Создаем инфраструктуру']"
    img_4 = "//img[@alt='Сопровождаем клиентов']"

    # Getters
    def get_img_1(self):
        """ Получение локатора изображения 'Разрабатываем систему СБИС' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.img_1)))

    def get_img_2(self):
        """ Получение локатора изображения 'Продвигаем сервисы' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.img_2)))

    def get_img_3(self):
        """ Получение локатора изображения 'Создаем инфраструктуру' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.img_3)))

    def get_img_4(self):
        """ Получение локатора изображения 'Сопровождаем клиентов' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.img_4)))

    # Methods
    def check_img_size(self):
        """ Проверка, имеют ли изображения в блоке 'Работаем' одинаковые параметры 'height' и 'weight' """
        Logger.add_start_step(method="check_img_size")
        self.get_current_url()
        self.assert_img_size(self.get_img_1(), self.get_img_2(), self.get_img_3(), self.get_img_4())
        Logger.add_end_step(url=self.driver.current_url, method="check_img_size")

