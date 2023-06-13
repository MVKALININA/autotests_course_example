# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    sleep(1)
    user_login, user_password = 'skaner', 'skaner123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(3)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)

    btn1_contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    btn1_contacts.click()  # Нажать кнопку "Контакты" в аккордеоне
    sleep(3)

    btn2_contacts = driver.find_element(By.CSS_SELECTOR, '[class="NavigationPanels-SubMenu__head  NavigationPanels-SubMenu__head_default ws-flex-shrink-0"]')
    btn2_contacts.click()  # нажать кнопку "Контакты" в выпадающем меню
    sleep(2)

    btn_message = driver.find_element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]')
    btn_message.click()  # + сообщение
    sleep(3)
    btn1_person = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2023-06-13"]')
    person = "Сканер Святослав"
    btn1_person.send_keys(person, Keys.ENTER)  # ввели адресата, появилось автодополнение
    sleep(3)

    btn2_person = driver.find_element(By.CSS_SELECTOR, '[class="person-BaseInfo ws-flexbox ws-align-items-baseline person-BaseInfo__textAlignment_fontsize-2xl controls_Person_theme-default person-Info__withActivity"]')
    btn2_person.click()  # выбрать адресата, открылось поле сообщения
    sleep(3)

    btn_arial_message = driver.find_element(By.CSS_SELECTOR, '[class="textEditor_Viewer__Paragraph"]')
    btn_arial_message.click()
    sleep(2)

    text = "Мой первый и последний автотест"
    btn_arial_message.send_keys(text, Keys.ENTER)  # ввести текст сообщения
    sleep(2)

    btn_send_to_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    btn_send_to_message.click()  # Нажать кнопку отправки сообщения
    sleep(2)
    # Проверка, что сообщение появилось в реестре:
    message = driver.find_element(By.CSS_SELECTOR, '[class="msg-entity-text msg-entity_font_croppless richEditor_richContentRender_fontSize-m_theme-default controls_RichEditor_theme-default richEditor_richContentRender_theme-default richEditor_richContentRender richEditor_richContentRender_lineHeight-s richEditor_richContentRender_colorPalette-first richEditor_richContentRender_readOnly msg-dialogs-item__message-text msg-entity-text_normalized controls-List_DragNDrop__notDraggable ws-flex-shrink-1 msg-entity-expander__content ws-flex-grow-1 ws-flex-shrink-1"]')
    assert message.text == "Мой первый и последний автотест"

    btn_read_message = driver.find_element(By.CSS_SELECTOR,'[class="controls-ListView__itemContent  controls-ListView__item_default-topPadding_s controls-ListView__item_default-bottomPadding_s controls-ListView__item-rightPadding_null controls-ListView__itemContent_withCheckboxes controls-ListView__itemContent_withCheckboxes_default "]')
    btn_read_message.click()  # открыть сообщение
    sleep(2)

    btn_delete_message = driver.find_element(By.CSS_SELECTOR,'[data-qa="remove"]')
    btn_delete_message.click()  # удалить сообщение
    sleep(3)

    message_delete = driver.find_element(By.CSS_SELECTOR, '[class="msg-dialogs-detail msg-dialogs-layout__detail-content ws-flex-shrink-1 controls-MasterDetail_detailsContent  controls-MasterDetail_details-bg-contrast controls-MasterDetail_details-newDesign tlr"]')
    assert message_delete.text != "Мой первый и последний автотест"  # проверить что сообщения нет в реестре
finally:
    driver.quit()
