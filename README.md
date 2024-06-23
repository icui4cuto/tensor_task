# Тестовое задание Tensor.ru

Выполнение трех тестовых сценариев + подключение логирования + отчеты Allure <!-- описание репозитория -->
<!--Блок информации о репозитории в бейджах-->

<!--Запуск тестов-->

## Установка зависимостей

```pip3 install -r requirements.txt```

## Запуск тестов

Запуск тестов должен производиться из директории /tests

1. Переход в директорию /tests

```cd tests```

2. Запуск одного тестового сценария (например, проверка скачивания файла)

```python -m pytest test_download_file.py -s -v```

3. Запуск всех тестов

```python -m pytest -s -v```

## Создание и просмотр отчетов Allure
1. Для установки Allure необходимо воспользоваться документацией - https://allurereport.org/docs/install-for-windows/

2. Создание отчета

```python -m pytest --alluredir=test_results/ ```

3. Просмотр отчета
   
``` allure serve test_results/ ```
