import requests, lxml, os
from bs4 import BeautifulSoup

AMAZON_PRODUCT_URL = "https://www.amazon.ca/Practical-Programming-Introduction-Computer-Science/dp/1680502689/ref=sr_1_6?crid=10XGTI9MLB5GB&keywords=programming+book&qid=1685490298&s=books&sprefix=programming+boo%2Cstripbooks%2C199&sr=1-6"
TARGET_PRICE = 50
USER_AGRENT = os.environ.get("USER_AGENT_HEADER")
ACCEPT_LANGUAGE = os.environ.get("ACCEPT_LANGUAGE_HEADER")
headers = {
    "User-Agent": USER_AGRENT,
    "Accept-Language": ACCEPT_LANGUAGE,
    "Accept-Identity": "identity",
}
response = requests.get(url=AMAZON_PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price_html_tag = soup.select_one(selector="span#price")
price = float(price_html_tag.text.split("$")[1])

if price <= TARGET_PRICE:
    import smtplib
    MY_EMAIL = os.environ.get("MY_EMAIL")
    MY_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
    title_html_tag = soup.select_one(selector="span#productTitle")
    product_title = title_html_tag.text.strip()
    subtitle_html_tag = soup.select_one(selector="span#productSubtitle")
    product_subtitle = subtitle_html_tag.text.strip().split(" ")[0]
    SMTP_HOST = os.environ.get("SMTP_HOST")
    with smtplib.SMTP(host=SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        message = f"""\
Subject: Amazon Price Alert

{product_title} - {product_subtitle} is now below ${TARGET_PRICE: .2f}.\n
{AMAZON_PRODUCT_URL}"""
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
