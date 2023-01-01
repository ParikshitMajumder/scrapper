# Step 1 import all the dependencies

from bs4 import BeautifulSoup
import requests


from scrap.main.CRUD_Service import save_data

#url="https://www.flipkart.com/wincial-windows-10-pro-32bit-64bit/p/itm4e58474732d21?pid=OPSG942JMDQKZZK6&cmpid=product.share.pp&_refId=PP.d51682ca-03c3-4c6a-8fb4-bd1a9fbaafc2.OPSG942JMDQKZZK6&_appId=WA"

url="https://www.amazon.in/dp/B08JD36C6H/ref=cm_sw_r_apa_i_N3Y7G0SFXPMJ0KSAZ786_0?th=1"

# Step 2 get the HTML from the Website



r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
htmlcontent=r.content


#print("Content before parsing",htmlcontent)

#step3 parse the HTML

soup = BeautifulSoup(htmlcontent,'html.parser')

print("###################################")
#print("After parsing",soup.prettify)


#step3 HTML Tree traversal

# finding all the tags 

#para=soup.find_all('a')
#print(para)

# finding classes

#print(soup.find(class_='B_NuCI'))
#print(soup.find(class_='_30jeq3 _16Jk6d'))#

#name=soup.find(class_='B_NuCI').string
#s=soup.find(class_='_30jeq3 _16Jk6d')



name = soup.find("span",attrs={"id": 'productTitle'})
name_value = name.string
name_string = name_value.strip().replace(',', '')
print("Product name=",name_string)


price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
print("Product Price=",price)


#s=soup.find(class_='a-price-whole')

price1="₹249.00"
#price1=str(s.string)
price=int(price1[1:4])
print(name)
#print(price)
save_data(name_string,price)


# New Block 