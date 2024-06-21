import os


class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """ Метод возвращает текущий url """
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    def assert_word(self, word, result):
        """ Проверка значения текста"""
        value_word = word.text
        assert value_word == result
        print("Check - Ok!")

    def assert_url(self, result):
        """ Проверка url """
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url!")

    def assert_region_url(self, region_id):
        """ Проверка id региона в url """
        get_id_region_in_url = self.driver.current_url
        assert get_id_region_in_url.find(region_id)
        print("Region ID in url: Check - Ok!")

    def assert_title(self, result):
        """ Проверка заголовка страницы """
        get_title = self.driver.title
        title_modified = (get_title.split(" — "))[1]
        assert title_modified.split()[0] == result.split()[0]
        print("Title: Check - Ok!")

    def assert_img_size(self, *args):
        """ Проверка размеров изображений """
        element_height, element_width = [], []

        for element in args:
            element_height.append(element.get_attribute("height"))
            element_width.append(element.get_attribute("width"))

        assert len(set(element_height)) == 1 and len(set(element_width)) == 1
        print("The size of all elements are equal!")

    def assert_file_in_directory(self, file_path):
        """ Проверка наличия файла в директории """
        assert os.access(file_path, os.F_OK)
        print("File in directory!")

    def assert_file_size(self, file_path, file_size):
        """ Проверка размера файла """
        file_size = float((file_size.split())[2])
        assert round((os.path.getsize(file_path)/1048576), 2) == file_size
        print("File is correct size!")
