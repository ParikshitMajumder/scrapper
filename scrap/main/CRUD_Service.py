#this is the automated script that will run every day to gather data from the websites.

import mysql.connector
from datetime import datetime

#conn=mysql.connector.connect(database="scalper_data", user='root', password='2wsx@WSX', host='localhost', port= '3306')

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2wsx@WSX",
  database="scalper_data"
)

 


def save_data(name, price,website):
 print("initializing database connection")
 date=datetime.now()
 website_name=website
  

 try:

  cursor=conn.cursor()
  print("Writting data into the database")

  sql = "INSERT INTO scalper_data.main_price_data (Product_name,Price,date,website_name) VALUES (%s,%s,%s,%s)"
  val = (name,price,date,website_name)
  cursor.execute(sql, val)  
  conn.commit()
 
  cursor.execute("select * from scalper_data.main_price_data") 

  print("data recorded ----->",cursor.fetchone())

  #cursor.execute(''' insert into public.main_to_scrapper_data values('test',200,time,'1')''')

  conn.close()
  print("Connection successfully establised and closed.")

 except Exception as e : 
  print("####### Exceptions Happened #######")
  print(e)

