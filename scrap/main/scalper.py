from bs4 import BeautifulSoup
import requests
import CRUD_Service


class scalp_date:

    #For Flipkart 
    def scalp_flipkart(url,name_class_data,price_class_data,website):

        url=url
        website=website
        r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
        htmlcontent=r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')
        name=soup.find(class_=name_class_data).string
        print("Recorded Product Name from Flipkart - ",name)
        
        price1=soup.find(class_=price_class_data).string
        #print("Price - ",price1)
        price=int(price1.strip("₹"))
        print("Recorded Price is -₹",price ,"and converted type to",type(price))
        print("Proceeding with the database call -------")

        try:
            CRUD_Service.save_data(name,price,website)
        except Exception as e :
            print(e)

    def scalp_amazon(url,name_class_data,price_class_data,website):
        pass




# Code tester
# for flipkart
#urll="https://www.flipkart.com/wincial-windows-10-pro-32bit-64bit/p/itm4e58474732d21?pid=OPSG942JMDQKZZK6&lid=LSTOPSG942JMDQKZZK6D36BMR&marketplace=FLIPKART"  
#name="B_NuCI" 
#price="_30jeq3 _16Jk6d"
#website="Flipkart"
#scalp = scalp_date.scalp_flipkart(urll,name,price,website)
    