from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PASSWORD = "TDfM$EgeSprVMp8"
EMAIL = "@jony104570"
PROMISED_DOWN = 100
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'C:\\Users\\khazr\\win64\\121.0.6167.85\\chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.driver = webdriver.Chrome(options=driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        ads = self.driver.find_element(By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")
        time.sleep(3)
        ads.click()
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        self.download = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div'
                                                                 '[2]/div''[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                                 '/div[1]/div/'
                                                            'div[2]/span').text
        self.upload = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                               '/div[3]'
                                                          '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'
                                                          '/span').text


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        fill = self.driver.find_element(By.CSS_SELECTOR, value="#react-root input")
        fill.send_keys(EMAIL)
        fill.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div'
                                                            '/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label'
                                                            '/div/div[2]/div[1]/input')

        password.send_keys(PASSWORD)
        print(password.text)
        tweet_post = self.driver.find_element(By.CLASS_NAME, value="public-DraftStyleDefault-block "
                                                                   "public-DraftStyleDefault-ltr")
        tweet = (f"Hey Provider! My internet speed is {self.download}/down{self.upload}/up when i paid for "
                 f"{PROMISED_DOWN}/down{PROMISED_UP}/up! Shame on YOU!")
        tweet_post.send_keys(tweet)
        post_button = self.driver.find_element(By.LINK_TEXT, value="Post")
        time.sleep(2)
        post_button.click()
        time.sleep(2)
        self.driver.quit()




bot = InternetSpeedTwitterBot(chrome_options)

bot.get_internet_speed()
bot.tweet_at_provider()
