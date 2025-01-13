from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
import time
import pyperclip

class NaverLoginService:
    def __init__(self):
        self.driver = None

    def open_web_mode(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager(driver_version="131.0.6778.205").install()
            ),
            options=Options()
        )
        self.driver.set_page_load_timeout(10)

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def login(self):
        self.driver.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fmail.naver.com%2F")
        time.sleep(2)

        test_id = "ID"
        test_passwd = "Passwd"

        id_input = self.driver.find_element(By.ID, "id")
        id_input.click()
        pyperclip.copy(test_id)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)

        pw_input = self.driver.find_element(By.ID, "pw")
        pw_input.click()
        pyperclip.copy(test_passwd)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)

        self.driver.find_element(By.ID, "log.login").click()

if __name__ == "__main__":
    naver_service = NaverLoginService()
    naver_service.open_web_mode()
    naver_service.login()
    time.sleep(5)
    naver_service.close_browser()
