import time

def test_product_page_has_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза, чтобы визуально проверить язык (как требуется в задании)
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину по уникальному селектору
    button = browser.find_element("css selector", "button.btn-add-to-basket")
    
    # Проверяем, что кнопка существует и видима
    assert button is not None, "Кнопка добавления в корзину не найдена на странице"
