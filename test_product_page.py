import pytest
from pages.product_page import ProductPage

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # Если баг на 7-й ссылке, она должна быть помечена как xfail, как в подсказке:
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    # 1. Получаем название и цену ДО добавления в корзину
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # 2. Добавляем в корзину (и решаем капчу)
    page.add_to_basket()

    # 3. Проверяем, что в сообщении правильное название и цена
    page.should_be_add_to_basket_message(product_name)
    page.should_be_correct_basket_price(product_price)