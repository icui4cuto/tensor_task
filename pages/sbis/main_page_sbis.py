

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPageSbis(Base):
    """ Главная страница """
    url = "https://sbis.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    contacts = "(//a[@href='/contacts'])[1]"
    download_link = "//a[@href='/download']"

    # Getters
    def get_contacts(self):
        """ Получение локатора 'Контакты' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.contacts)))

    def get_download_link(self):
        """ Получение локатора 'Скачать локальные версии' """
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.download_link)))

    # Actions
    def select_contacts(self):
        """ Выбор раздела 'Контакты' """
        self.get_contacts().click()
        print("Select contacts")

    def click_download_link(self):
        """ Клик по ссылке 'Скачать локальные версии' """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_download_link())
        self.get_download_link().click()
        print("Click download link")

    # Methods
    def open_main_page(self):
        """ Открываем главную страницу """
        Logger.add_start_step(method="open_main_page")
        self.driver.get(self.url)
        self.driver.maximize_window()
        Logger.add_end_step(url=self.driver.current_url, method="open_main_page")

    def open_contacts(self):
        """ Переходим в раздел 'Контакты' """
        Logger.add_start_step(method="open_contacts")
        self.get_current_url()
        self.select_contacts()
        Logger.add_end_step(url=self.driver.current_url, method="open_contacts")

    def open_download_page(self):
        """ Переходим в раздел 'Скачать' """
        Logger.add_start_step(method="open_download_page")
        self.get_current_url()
        self.click_download_link()
        Logger.add_end_step(url=self.driver.current_url, method="open_download_page")

