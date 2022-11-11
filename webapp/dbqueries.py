#!/usr/bin/python3

import mysql.connector
from mysql.connector import Error

connected = False
mydb = None
cursor = None
case = 0

def connectDB():
  global connected
  global mydb
  try:
    mydb = mysql.connector.connect(
      host='127.0.0.1',
      user='root',
      passwd='password',
      database='studentalert',
      port='3306',
      allow_local_infile = True
      )
    print("Connection Successful")
    connected = True
  except mysql.connector.Error as e:
    print(f"Error: {e}, connection unsuccessful")
  return mydb
 
  
def closeDB():
  global connected
  global cursor
  global mydb
  connected = False
  cursor.close()
  #mydb.close()
  mydb = None
  pass


def executeQuery(query):
  global connected
  global mydb
  global cursor
  global case
  
  if(case == 1):
    if(mydb == None and connected == False):
      connection = connectDB()
      cursor = connection.cursor()
      result = None
      try:
        cursor.execute(query)
        result = cursor.fetchall()
        closeDB()
        return result
      except Error as err:
        print(f"Error: {err}")
    else:
      print(mydb)
      print(connected)
  elif(case == 2):
    if(mydb == None and connected == False):
      connection = connectDB()
      cursor = connection.cursor()
      result = None
      try:
        cursor.execute(*query)
        result = cursor.fetchall()
        closeDB()
        return result
      except Error as err:
        print(f"Error: {err}")
    else:
      print(mydb)
      print(connected)
  elif(case == 3):
    if(mydb == None and connected == False):
      connection = connectDB()
      cursor = connection.cursor()
      result = None
      try:
        cursor.execute(*query)
        connection.commit()
        closeDB()
      except Error as err:
        print(f"Error: {err}")
    else:
      print(mydb)
      print(connected)
  closeDB()
  pass
  
  
# Grab all entries in the incident table
def getAllIncidents():
  global case
  case = 1
  try:
    query = ("""SELECT * FROM studentalert.incident""")
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')
    
# Grab all entries in incident where armed = 1
def getAllArmed():
  global case
  case = 2
  # 0 = unarmed, 1 = armed
  arm = 1
  try:
    query = ("""SELECT * FROM studentalert.incident WHERE armed = %s""", (arm,))
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')
    
# Functional queries
#print(getAllIncidents())
#print(getAllArmed())


  
  

