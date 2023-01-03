from bs4 import BeautifulSoup
import requests
from . import CRUD_Service
from django.contrib import messages


class scalp_data:

    #For Flipkart 
    def scalp_flipkart(url,name_class_data,price_class_data,website):

        url=url
        website=website
        r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
        htmlcontent=r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')
        name=soup.find("span",class_=name_class_data)

        print("Recorded Product Name from Flipkart - ",name,"type=",type(name))
        
        price2=soup.find(class_=price_class_data)

        if name  == None:
            return False

        elif price2 == None:
            return False
                #
    
        else : 
            print(".......Proceeding with the database call -------")
            try:
                price1=price2.text
                print("received Price - ",price1)
                price1=price1.replace(',','')
                price=int(price1.replace('₹',''))
                name1=name.text
                print("Final Recorded Product Name from Flipkart - ",name1,"type=",type(name)," Receiced Price =>",price2,"Converted to ",price2)
                CRUD_Service.save_data(name1,price,website)
                return True
            except Exception as e :
                print(e)
                return False
            

        

    def scalp_amazon(url,name_class_data,price_class_data,website):
        pass




# Code tester
# for flipkart
#urll="https://www.flipkart.com/wincial-windows-10-pro-32bit-64bit/p/itm4e58474732d21?pid=OPSG942JMDQKZZK6&lid=LSTOPSG942JMDQKZZK6D36BMR&marketplace=FLIPKART"  
#name="B_NuCI" 
#price="_30jeq3 _16Jk6d"
#website="Flipkart"
#scalp = scalp_data.scalp_flipkart(urll,name,price,website)
    