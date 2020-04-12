import requests
import smtplib as smtp
from selenium import webdriver
from bs4 import BeautifulSoup as bs
def send_mail():
	server=smtp.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login("atib.ahmed2022@gmail.com", "8176981385")
	subject="hello "
	body="how r u"
	msg=f"subject : {subject} \n\n{body}"
	server.sendmail("atib.ahmed2022@gmail.com","atib.ahmed@gmail.com", msg)
	server.quit()
	print("MAil sent")
driver=webdriver.Chrome("C:/Users/RIL/Desktop/chromedriver")
url="https://www.amazon.com/Canon-PowerShot-180-Digital-Silver-Accessory/dp/B01B6YDD1G/ref=sxin_0_ac_d_pm?ac_md=4-2-QmV0d2VlbiAkMTAwIGFuZCAkMjAw-ac_d_pm&cv_ct_cx=camera&dchild=1&keywords=camera&pd_rd_i=B01B6YDD1G&pd_rd_r=fd626b6e-1bde-4e02-a584-fd09baf970a5&pd_rd_w=dpwB3&pd_rd_wg=Ka0BM&pf_rd_p=0e223c60-bcf8-4663-98f3-da892fbd4372&pf_rd_r=4MSA0Y5V7T2D548Q2ZGP&psc=1&qid=1586722515&sr=1-3-22d05c05-1231-4126-b7c4-3e7a9c0027d0"
driver.get(url)
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
content = driver.page_source
soup = bs(content,"html.parser")
tittle=soup.find(id="productTitle").get_text()
print(tittle.strip())
price=soup.find(id="productblock_ourprice").get_text()
con_price=float(price[0:5])
if(con_price>100):
	send_mail()

