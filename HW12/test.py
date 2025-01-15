import os.path
import time
import allure
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

DOMAIN = "https://the-internet.herokuapp.com"


@allure.suite("Selenium_advanced")
@allure.sub_suite("Clicks")
class TestClicks:
    @allure.title("Normal_click")
    def test_click(self, driver):
        url = f"{DOMAIN}/checkboxes"
        driver.get(url)
        checkbox = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
        checkbox.click()
        assert checkbox.is_selected()

    @allure.title("JS_click")
    def test_js_click(self, driver):
        url = f"{DOMAIN}/hovers"
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*/a[@href="/users/1"]')
        driver.execute_script("arguments[0].click()", element)
        assert driver.title != "The Internet"

    @allure.title("Mouse_click")
    def test_mouse_click(self, driver):
        url = f"{DOMAIN}/context_menu"
        driver.get(url)
        box = driver.find_element(By.XPATH, '//*[@id="hot-spot"]')
        action: ActionChains = ActionChains(driver)
        action.context_click(box).perform()
        alert = driver.switch_to.alert
        assert alert.text == "You selected a context menu"
        alert.accept()

    @allure.title("Keyboard_click")
    def test_keyboard_click(self, driver):
        url = f"{DOMAIN}/key_presses"
        driver.get(url)
        action: ActionChains = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You entered: ENTER"


@allure.suite("Selenium_advanced")
@allure.sub_suite("Text")
class TestText:
    @allure.title("Text_input")
    def test_add_text(self, driver):
        url = f"{DOMAIN}/inputs"
        driver.get(url)
        field = driver.find_element(By.XPATH, '//*[@type="number"]')
        field.send_keys("123")
        assert field.get_attribute("value") == "123"

    @allure.title("Clear_text")
    def test_clear_text(self, driver):
        url = f"{DOMAIN}/inputs"
        driver.get(url)
        field = driver.find_element(By.XPATH, '//*[@type="number"]')
        field.send_keys("123")
        field.clear()
        assert field.get_attribute("value") == ""


@allure.suite("Selenium_advanced")
@allure.sub_suite("Alert")
class TestAlert:
    @allure.title("Simple_alert")
    def test_accept_simple_alert(self, driver):
        url = f"{DOMAIN}/javascript_alerts"
        driver.get(url)
        button = driver.find_element(By.XPATH, "//*[1]/button")
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Alert"
        alert.accept()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You successfully clicked an alert"

    @allure.title("Confirmation_alert_accept")
    def test_accept_confirm_alert(self, driver):
        url = f"{DOMAIN}/javascript_alerts"
        driver.get(url)
        button = driver.find_element(By.XPATH, "//*[2]/button")
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Confirm"
        alert.accept()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You clicked: Ok"

    @allure.title("Confirmation_alert_dismiss")
    def test_dismiss_confirm_alert(self, driver):
        url = f"{DOMAIN}/javascript_alerts"
        driver.get(url)
        button = driver.find_element(By.XPATH, "//*[2]/button")
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Confirm"
        alert.dismiss()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You clicked: Cancel"

    @allure.title("Prompt_alert_accept")
    def test_accept_prompt_alert(self, driver):
        url = f"{DOMAIN}/javascript_alerts"
        driver.get(url)
        button = driver.find_element(By.XPATH, "//*[3]/button")
        button.click()
        alert = driver.switch_to.alert
        alert.send_keys("test")
        alert.accept()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You entered: test"

    @allure.title("Prompt_alert_dismiss")
    def test_dismiss_prompt_alert(self, driver):
        url = f"{DOMAIN}/javascript_alerts"
        driver.get(url)
        button = driver.find_element(By.XPATH, "//*[3]/button")
        button.click()
        alert = driver.switch_to.alert
        alert.send_keys("test")
        alert.dismiss()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You entered: null"


@allure.suite("Selenium_advanced")
@allure.sub_suite("Tabs")
@allure.title("Tabs")
def test_switch_to_new_tab(driver):
    url = f"{DOMAIN}/windows"
    driver.get(url)
    assert driver.title == "The Internet"
    link = driver.find_element(By.XPATH, '//a[@href="/windows/new"]')
    link.click()
    main_window = driver.current_window_handle
    new_window = [window for window in driver.window_handles if window != main_window][
        0
    ]
    driver.switch_to.window(new_window)
    time.sleep(1)
    assert driver.title == "New Window"


@allure.suite("Selenium_advanced")
@allure.sub_suite("iFrame")
@allure.title("iFrame")
def test_switch_to_frame(driver):
    url = f"{DOMAIN}/iframe"
    driver.get(url)
    frame = driver.find_element(By.XPATH, "//iframe")
    driver.switch_to.frame(frame)
    content = driver.find_element(By.XPATH, "//p")
    assert content.text == "Your content goes here."
    driver.switch_to.default_content()


@allure.suite("Selenium_advanced")
@allure.sub_suite("Files")
class TestFiles:
    @allure.title("File_upload")
    def test_upload_file(self, driver):
        url = f"{DOMAIN}/upload"
        driver.get(url)
        file_upload = driver.find_element(By.XPATH, '//*[@id="file-upload"]')
        file_path = os.path.abspath("/test/upload.txt")
        file_upload.send_keys(file_path)
        file_submit = driver.find_element(By.XPATH, '//*[@id="file-submit"]')
        file_submit.click()
        message = driver.find_element(By.XPATH, "//*/h3")
        file_name = driver.find_element(By.XPATH, '//*[@id="uploaded-files"]')
        assert message.text == "File Uploaded!"
        assert file_name.text == "upload.txt"

    @allure.title("File_download")
    def test_download_file(self, driver):
        url = f"{DOMAIN}/download"
        driver.get(url)
        driver.implicitly_wait(5)
        download_link = driver.find_element(
            By.XPATH, '//*/a[contains(@href,"upload.txt")]'
        )
        download_link.click()
        download_dir = os.path.abspath("/test/downloads")
        expected_file = os.path.join(download_dir, "upload.txt")
        assert os.path.exists(expected_file)
