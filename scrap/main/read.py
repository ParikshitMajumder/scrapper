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

 
  

try:

  cursor=conn.cursor()
  print("reading data from the database")

  sql = "select * from scalper_data.main_scrapper_data"
 

 
  data=cursor.execute(sql)  
  print(data)

  #cursor.execute(''' insert into public.main_to_scrapper_data values('test',200,time,'1')''')

  conn.close()
  print("Connection successfully establised and closed.")

except Exception as e : 
  print("####### Exceptions Happened #######")
  print(e)

