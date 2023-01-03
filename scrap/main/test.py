from bs4 import BeautifulSoup
import requests
import CRUD_Service




    #For Flipkart 
def scalp_flipkart(url,name_class_data,price_class_data,website):

        url=url
        website=website
        r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
        htmlcontent=r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')
        #name=soup.find(class_="B_NuCI").string
        #name=str(soup.find("span",class_="B_NuCI").text)
        name=soup.find("span",class_=name_class_data)
    
        #print("Recorded Product Name from Flipkart - ",name,"type=",type(name))
        price2=soup.find(class_=price_class_data)
        #price1=price2.text
        #print("receiverd Price - ",price1)
        #price1=price1.replace(',','')
        #price=int(price1.replace('₹',''))
        print("Recorded Price is -₹",price2 ,"and converted type to",type(price2))
        if name  == None:
            return False

        elif price2 == None:
            return False
                #
    
        else : 
            print("Proceeding with the database call -------")
            try:
                price1=price2.text
                print("receiverd Price - ",price1)
                price1=price1.replace(',','')
                price=int(price1.replace('₹',''))
                name1=name.text
                print("Final Recorded Product Name from Flipkart - ",name1,"type=",type(name)," Receiced Price =>",price2,"Converted to ",price2)
                CRUD_Service.save_data(name1,price,website)
                return True
            except Exception as e :
                print(e)
                return False

            
        """
        price1=soup.find(class_=price_class_data).string
        print("receiverd Price - ",price1)
        price1=price1.replace(',','')
        price=int(price1.replace('₹',''))
        print("Recorded Price is -₹",price ,"and converted type to",type(price))
        print("Proceeding with the database call -------")
        """
        #try:
        #    CRUD_Service.save_data(name,price,website)
        #except Exception as e :
        #    print(e)

def scalp_amazon(url,name_class_data,price_class_data,website):
        pass


#

# Code tester
# for flipkart
urll="https://www.flipkart.com/razer-blackwidow-v3-pro-wireless-mechanical-gaming-keyboard-yellow-switch-wired-usb/p/itm9d81411acc21d?pid=ACCG59YHCYSWVGFT&lid=LSTACCG59YHCYSWVGFTK5QJRS&marketplace=FLIPKART&q=mechanical+keyboard&store=4rr%2Fkm5&srno=s_1_9&otracker=search&otracker1=search&fm=Search&iid=93ea8ebf-ebd1-44ab-936c-6822b81733d6.ACCG59YHCYSWVGFT.SEARCH&ppt=sp&ppn=sp&qH=a792c83875887481"
name="B_NuCI" 
price="_30jeq3 _16Jk6d"
website="Flipkart"
scalp = scalp_flipkart(urll,name,price,website)
print(scalp,type(scalp))
    