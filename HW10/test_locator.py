import time
from selenium.webdriver.common.by import By


URL = 'https://www.wildberries.by/'

def test_xpath(driver):
    driver.get(URL)
    time.sleep(3)
    country = driver.find_element(By.XPATH, '//header//span[contains(@class, "currency")]')
    burger = driver.find_element(By.XPATH, '//header//button[contains(@class, "burger")]')
    search_field = driver.find_element(By.XPATH, '//header//input[contains(@type, "search")]')
    logo = driver.find_element(By.XPATH, '//header//a[contains(@class, "logo")]')
    basket = driver.find_element(By.XPATH, '//header//div[contains(@class, "basket")]')

    assert country.is_displayed(), "Country selector is not visible"
    assert burger.is_displayed(), "Burger menu is not visible"
    assert search_field.is_displayed(), "Search field is not visible"
    assert logo.is_displayed(), "Logo is not visible"
    assert basket.is_displayed(), "Basket icon is not visible"

def test_css(driver):
    driver.get(URL)
    time.sleep(3)
    country = driver.find_element(By.CSS_SELECTOR, '.simple-menu__currency')
    burger = driver.find_element(By.CSS_SELECTOR, '.header__nav-element button')
    search_field = driver.find_element(By.CSS_SELECTOR, '#searchInput')
    logo = driver.find_element(By.CSS_SELECTOR, '.header__nav-element a img')
    basket = driver.find_element(By.CSS_SELECTOR, '.j-item-basket a')

    assert country.is_displayed(), "Country selector is not visible"
    assert burger.is_displayed(), "Burger menu is not visible"
    assert search_field.is_displayed(), "Search field is not visible"
    assert logo.is_displayed(), "Logo is not visible"
    assert basket.is_displayed(), "Basket icon is not visible"