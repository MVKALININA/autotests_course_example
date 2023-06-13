# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    sleep(2)
    btn1_contacts = driver.find_element(By.LINK_TEXT, 'Контакты')
    btn1_contacts.click()   # нажать на кнопку "Контакты"
    sleep(2)

    btn2_logo = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    btn2_logo.click()   # нажать на логотип Тензор

    driver.switch_to.window(driver.window_handles[1])  # перейти на другую вкладку
    sleep(2)

    btn3_power = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    sleep(2)
    assert btn3_power.text.split('\n')[0] == "Сила в людях"  # проверка текста
    actions = ActionChains(driver)  # класс действий
    actions.move_to_element(btn3_power)  # ховер на элемент
    actions.perform()  # вызов действия
    sleep(2)

    btn4_more = driver.find_elements(By.CLASS_NAME, 'tensor_ru-Index__link')[1]
    # ищем второй элемент из списка
    btn4_more.click()  # нажать на "Подробнее"
    assert driver.current_url == about  # проверка текущей вкладки
    sleep(2)

finally:
    driver.quit()
    