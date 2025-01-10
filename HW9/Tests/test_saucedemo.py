from selenium.webdriver.common.by import By
from pytest import mark

URL1 = 'https://www.saucedemo.com/'
URL2 = 'https://www.saucedemo.com/inventory.html'

@mark.parametrize('driver', ['chrome','firefox'], indirect=True)
@mark.parametrize('username,password',[('visual_user','secret_sauce')])
def test_positive_scenario(driver,username,password):
    driver.get(URL1)
    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    assert driver.current_url == URL2

@mark.parametrize('driver', ['chrome','firefox'], indirect=True)
@mark.parametrize('username,password,text',[('','secret_sauce',"Epic sadface: Username is required"),
                                            ('problem_user','',"Epic sadface: Password is required"),
                                            ('qwerty_user','secret_sauce',"Epic sadface: Username and password do not match any user in this service"),
                                            ('error_user','err_pass',"Epic sadface: Username and password do not match any user in this service"),
                                            ('locked_out_user','secret_sauce',"Epic sadface: Sorry, this user has been locked out.")])
def test_negative_scenario(driver,username,password,text):
    driver.get(URL1)
    username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    assert driver.current_url == URL1
    assert error.text == text