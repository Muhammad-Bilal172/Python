import requests
from bs4 import BeautifulSoup
import smtplib

myEmail = "bilalashiq190@gmail.com"
password = "clft bcub xrkh rsma"

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=header)

content = BeautifulSoup(response.text, "html.parser")

priceTag = content.find(name="span", class_="a-price-whole")

price = priceTag.getText()[0:-1]

if int(price) < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail, password=password)

        connection.sendmail(from_addr=myEmail, 
                            to_addrs="bilalashiq110@gmail.com", 
                            msg=f"The Price is less than 100 dollars please buy it from the original amazon website"
                            )
