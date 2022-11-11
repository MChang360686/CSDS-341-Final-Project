#!/usr/env/bin/python3

from flask import Flask, redirect, url_for, render_template
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
    
# Grab all entries in the itemstaken table
def getAllItemstaken():
  global case
  case = 1
  try:
    query = ("""SELECT * FROM studentalert.itemstaken""")
    result = executeQuery(query)
    return result
  except Error as e:
    print("Error: {e}")

# Grab all entries in the location table
def getAllLocations():
  global case
  case = 1
  try:
    query = ("""SELECT * FROM studentalert.location""")
    result = executeQuery(query)
    return result
  except Error as e:
    print("Error: {e}")

# Grab all entries in the perpetrator table
def getAllPerpetrators():
  global case
  case = 1
  try:
    query = ("""SELECT * FROM studentalert.perpetrator""")
    result = executeQuery(query)
    return result
  except Error as e:
    print("Error: {e}")

# Grab all entries in the university response table
def getAllUniResp():
  global case
  case = 1
  try:
    query = ("""SELECT * FROM studentalert.universityresponse""")
    result = executeQuery(query)
    return result
  except Error as e:
    print("Error: {e}")

# Grab all entries in the victim table
def getAllVictims():
  global case
  case = 1
  try:
    query = ("""SELECT * FROM studentalert.victim""")
    result = executeQuery(query)
    return result
  except Error as e:
    print("Error at {e}")
    
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
    
# return indexes of all incidents that are carjackings
def getCarjackings():
  global case
  case = 2
  name = 'vehicle'
  try:
    query = ("""SELECT incidentid FROM studentalert.incident, studentalert.victim, studentalert.itemstaken WHERE itemstaken.name = %s AND itemstaken.victim_idvictim = victim.idvictim AND victim.incident_incidentid = incident.incidentid""", (name,))
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')
    
# return number of incidents that are carjackings
def getNumCarjackings():
  global case
  case = 2
  crime = 'vehicle'
  try:
    query = ("""SELECT COUNT(name) FROM studentalert.itemstaken WHERE name = %s""", (crime,))
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')
    
# Sample query 1, get number of incidents by Date
def inciDate():
  global case
  case = 1
  try:
    query = ("""SELECT COUNT(date), date FROM studentalert.incident GROUP BY date""")
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')


# Sample query 2, get the number of all incidents by location
def inciByLoc():
  global case
  case = 1
  try:
    query = ("""SELECT COUNT(location_idlocation) FROM studentalert.incident, studentalert.location WHERE idlocation = location_idlocation GROUP BY location_idlocation""")
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')
    
# "Harder" query that is meant to be more complicated than the others
# Returns the incidents that are carjackings
def inciCarjack():
  global case
  case = 1
  try:
    query = ("""SELECT COUNT(location_idlocation) FROM studentalert.incident, studentalert.location WHERE idlocation = location_idlocation GROUP BY location_idlocation""")
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')

# Another harder query
# Returns all incidents listed as Armed Robberies on Euclid
def armedEuclid():
  global case
  case = 1
  try:
    query = ("""SELECT incidentid, incident.description, incident.date, incident.time FROM incident, location WHERE incident.armed = 1 AND incident.location_idlocation = location.idlocation AND incidentid IN (SELECT incidentid FROM incident WHERE location_idlocation = 6)""")
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')
    
# Also deals with Euclid, but Euclid is quite important for students
# Returns all carjackings and armed incidents that the university had a response of 1 to that occured on Euclid
def carjackingOne():
  global case
  case = 1
  try:
    query = ("""SELECT idvictim, victim.description FROM incident, victim WHERE incidentid = incident_incidentid AND universityresponse_iduniversityresponse = 1 AND location_idlocation = 6 AND incident.description LIKE ("%Armed%")""")
    result = executeQuery(query)
    return result
  except Error as e:
    print('Error: {e}')


app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")
  
@app.route("/incident")
def all():
  queryResult = getAllIncidents()
  return render_template("incidents.html", data=queryResult)
  
@app.route("/itemstaken")
def items():
  queryResult = getAllItemstaken()
  return render_template("itemstaken.html", data=queryResult)
  
@app.route("/location")
def locations():
  queryResult = getAllLocations()
  return render_template("location.html", data=queryResult)
  
@app.route("/perpetrator")
def perp():
  queryResult = getAllPerpetrators()
  return render_template("perpetrator.html", data=queryResult)
  
@app.route("/universityresponse")
def uniresp():
  queryResult = getAllUniResp()
  return render_template("universityresponse.html", data=queryResult)
  
@app.route("/victim")
def victims():
  queryResult = getAllVictims()
  return render_template("victim.html", data=queryResult)
  
@app.route("/armed")
def arm():
  # runs a query to pull all entries where
  # studentalert.incident armed = 1
  queryResult = getAllArmed()
  return render_template("armed.html", data=queryResult)
  
@app.route("/carjackings")
def carjackings():
  queryResult = getCarjackings()
  return render_template("carjackings.html", data=queryResult)
  
@app.route("/numcarjackings")
def numcarjackings():
  queryResult = getNumCarjackings()
  return render_template("numcarjackings.html", data=queryResult)
  
@app.route("/incidentsbydate")
def incidentsByDate():
  queryResult = inciDate()
  return render_template("incidentsbydate.html", data=queryResult)
  
@app.route("/incidentsbylocation")
def incidentsByLocation():
  queryResult = inciByLoc()
  return render_template("incidentsbylocation.html", data=queryResult)
  
@app.route("/armedeuclid")
def armedIncidentOnEuclid():
  queryResult = armedEuclid()
  return render_template("armedEuclid.html", data=queryResult)

@app.route("/carjackingone")
def carjackingResponseOne():
  queryResult = carjackingOne()
  return render_template("carjackingOne.html", data=queryResult)


if __name__ == "__main__":
  app.run()
  
  
