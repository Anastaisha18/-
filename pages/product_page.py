from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        add_btn = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        add_btn.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    def should_be_add_to_basket_message(self, expected_name):
        # Ищем сообщение об успешном добавлении и сравниваем с названием
        success_message = self.browser.find_element(By.CSS_SELECTOR, ".alert-success strong").text
        assert expected_name == success_message, f"Название товара в сообщении не совпадает. Ожидалось: {expected_name}, получено: {success_message}"

    def should_be_correct_basket_price(self, expected_price):
        # Ищем сообщение с ценой и сравниваем
        basket_price = self.browser.find_element(By.CSS_SELECTOR, ".alert-info strong").text
        assert expected_price == basket_price, f"Цена в корзине не совпадает. Ожидалось: {expected_price}, получено: {basket_price}"