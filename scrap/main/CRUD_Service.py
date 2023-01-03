#this is the automated script that will run every day to gather data from the websites.

import mysql.connector
from datetime import datetime

#conn=mysql.connector.connect(database="scalper_data", user='root', password='2wsx@WSX', host='localhost', port= '3306')

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2wsx@WSX",
  database="scrapper_data"
)

 


def save_data(name, price,website):
 print("initializing database connection")
 date=datetime.now()
 website_name=website
  

 try:
  

  cursor=conn.cursor()
  print("Writting data into the database Total 3 steps")
  print("Step1 : Writing name into Product name table")
  #creating name table 
  name_sql= "INSERT INTO scrapper_data.main_product_name (Name) VALUES (%s)"
  value=(name,)
  cursor.execute(name_sql,value)  
  conn.commit()
  cursor.reset()
  print("Step2 : previous operation successfull, reading name from Product name table",name)
  cursor.execute("select id from scrapper_data.main_product_name where Name='"+name+"'") 
  record=cursor.fetchone()
  for i in record : 
    name_id=record[0]

    print("id is------>",record[0],"and type is -->",type(record[0]))
  
  print("Step3 : previous operation successfull, writting into main_price_data table")
  cursor.reset()
  sql = "INSERT INTO scrapper_data.main_price_data (name_id,Price,date,website_name) VALUES (%s,%s,%s,%s)"
  val = (name_id,price,date,website_name)
  cursor.execute(sql, val)  
  conn.commit()
 
  cursor.execute("select * from scrapper_data.main_price_data") 

  print("data recorded into main_price_data ----->",cursor.fetchone())

  #cursor.execute(''' insert into public.main_to_scrapper_data values('test',200,time,'1')''')

  conn.close()
  print("Connection successfully establised and closed.")

 except Exception as e : 
  print("####### Exceptions Happened #######")
  print(e)

