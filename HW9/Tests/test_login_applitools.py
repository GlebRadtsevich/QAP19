from selenium.webdriver.common.by import By
from pytest import mark


URL1 = 'https://demo.applitools.com/index.html'
URL2 = 'https://demo.applitools.com/app.html'


@mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
@mark.parametrize('username,password', [('admin', 'admin')])
def test_login(driver, username, password):
    driver.get(URL1)
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'log-in')

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    assert driver.current_url == URL2
    assert driver.title == 'ACME demo app'
