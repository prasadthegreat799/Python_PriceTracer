from bs4 import BeautifulSoup
import requests
import smtplib

price=input("Enter the price:")

while True:
    page_url="https://www.amazon.in/Boat-Rockerz-400-Bluetooth-Headphones/dp/B01FSYQ01K/ref=sr_1_5?dchild=1&keywords=boat+900+wireless&qid=1597078165&sr=8-5"
    browser_agent={"user-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    product_page=requests.get(page_url,headers=browser_agent).text
    soup=BeautifulSoup(product_page,"html.parser")

    page_title=soup.find(id="productTitle").get_text()
    product_price=soup.find(id="priceblock_ourprice").get_text()[2:7]
    product_price=product_price.replace(',','')
    print(product_price)

    if(int(product_price)<int(price)):
      
      
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
      
        # start TLS for security 
        s.starttls() 
      
        # Authentication 
        s.login("prasadthegreat7999@gmail.com", "111435@one23") 
      
        # message to be sent 
        message = "Hey,prasad now the price of Boat head is deacreases "+ str(product_price)
      
        # sending the mail 
        s.sendmail("prasadthegreat7999@gmail.com", "prasadthegreat7999@gmail.com", message)
        print("mail Send Successfully")
      
        # terminating the session 
        s.quit()
        break
