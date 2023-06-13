# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней.
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался.
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep

import os
from selenium.webdriver.common.by import By

from pathlib import Path
from urllib import request

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Wait

sbis_ru = 'https://sbis.ru/'
driver = webdriver.Chrome()
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
try:
    driver.get(sbis_ru)
    sleep(3)
    download_sbis = driver.find_element(By.XPATH, '//a[contains(text(), "Скачать СБИС")]')
    # найти на странице элемент по частичному совпадению текста "Скачать СБИС"
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", download_sbis)
    # автоматически выполнить скрипт
    download_sbis.click()  # нажать кнопку "Скачать СБИС"
    sleep(3)

    btn_plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    btn_plugin.click()  # нажать кнопку "СБИС Плагин"
    sleep(3)

    download_plugin = Wait(driver, 10, ignored_exceptions=ignored_exceptions).until(ec.element_to_be_clickable((
                By.XPATH, '//a[contains(@href, "setup-web.exe")]'
            )))
    # скачать файл с элементом по частичному совпадению нескольких атрибутов: href и setup-web.exe
    url = download_plugin.get_attribute('href')  # получить название атрибута href - url
    file_name = Path(url).name  # вернуть абсолютный путь до файла
    request.urlretrieve(url, file_name)
    assert os.path.exists(file_name), f'Файл {file_name} не загрузился!'
    # проверить что файл скачан на ПК
    file_size = os.path.getsize(file_name) / 1024 ** 2  # рассчитать размера файла
    print(f'Размер файла {file_name}: {round(file_size, 3)} МБ')
    # Вывести на печать размер скачанного файла в мегабайтах, округлить до 3ех знаков
finally:
    driver.quit()
