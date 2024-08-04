import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

GOOGLE_FORM = "https://forms.gle/YZK9WomaVBTnczUX6"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=ZILLOW_URL).text

soup = BeautifulSoup(response, "html.parser")

all_links = []
all_tags_a = soup.find_all(name="a")
for anchor in all_tags_a:
    all_links.append(anchor.get("href"))
# print(all_links)

all_prices = []
all_price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
for price in all_price:
    s = price.getText()
    num = s.strip("$").strip("+/mo").replace(",", "")
    num = num.strip("+ 1bd")
    all_prices.append(num)
# print(all_prices)

all_addresses = []
addresses = soup.find_all(name="address")
for address in addresses:
    all_addresses.append(address.getText().strip("\n").strip(" ").replace(",", ""))
# print(all_addresses)

#Using selenium to fill the google form and getting excel sheet data

driver = webdriver.Chrome()
driver.get(url=GOOGLE_FORM)

for n in range(len(all_addresses)):
    first_question = driver.find_element(By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_question = driver.find_element(By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_question = driver.find_element(By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    time.sleep(1)
    first_question.send_keys(all_addresses[n])
    second_question.send_keys(all_prices[n])
    third_question.send_keys(all_links[n])
    submit.click()
    time.sleep(1)
    another_submit = driver.find_element(By.CSS_SELECTOR, value='.Uc2NEf a')
    another_submit.click()

# responses = driver.find_element(By.XPATH, '//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div')
# responses.click()
# sheet_data = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
# sheet_data.click()
