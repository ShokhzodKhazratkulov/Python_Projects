from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PASSWORD = "TDfM$EgeSprVMp8"
EMAIL = "khazratkulovshokhzod11@gmail.com"
PROMISED_DOWN = 100
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'C:\\Users\\khazr\\win64\\121.0.6167.85\\chromedriver.exe'


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.driver = webdriver.Chrome(service=Service(driver_path))

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Find the 'Go' button and click on it
        go_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        )
        go_button.click()

        # Wait for the speed test to complete
        time.sleep(60)

        # Get the download and upload speeds
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print(f"Download Speed: {download_speed}")
        print(f"Upload Speed: {upload_speed}")

    def tweet_at_provider(self):
        # Implement tweeting logic here
        pass


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
    bot.get_internet_speed()
    bot.tweet_at_provider()
