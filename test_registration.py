from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration(link):
    browser = webdriver.Chrome()
    try:
        browser.get(link)

        # Ищем поля по уникальным placeholder-ам
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("test@example.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text

    except Exception as e:
        return f"ОШИБКА: {type(e).__name__}: {e}"
    finally:
        browser.quit()


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

print("ТЕСТ 1:", test_registration(link1))
print("ТЕСТ 2:", test_registration(link2))