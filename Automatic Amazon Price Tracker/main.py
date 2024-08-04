import smtplib
import requests
from bs4 import BeautifulSoup

EMAIL = "khazratkulovshokhzod@gmail.com"
PASSWORD = "icpxndxfwfyeoqcd"

URL = "https://www.amazon.com/Sceptre-24-5-inch-DisplayPort-Speakers-C255B-FWT240/dp/B08VM9JN7H/ref=sr_1_10?crid=2EO2ZEOF4J17Q&keywords=monitor&qid=1706729986&sprefix=monitor%2Caps%2C309&sr=8-10&th=1"
headers = {'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
           'User-Agent': "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent"}

response = requests.get(URL, headers=headers)
web_url = response.text

soup = BeautifulSoup(web_url, "lxml")

price = soup.find("span", class_="a-offscreen").get_text()
actual_price = price.split("$")[1]
price_as_float = float(actual_price)

if price_as_float < 200.00:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"subject: Price sale!\n\n Hi there!\nHere is today's hot sale: "
                                f"The product you wanted is lower than you want which is "
                                f"${price_as_float}. Follow the link below!\n{URL}")
