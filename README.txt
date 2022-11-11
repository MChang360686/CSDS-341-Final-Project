README

Matthew Chang mmc175

TO use this code, you must have the following

1) MySQL
2) MySQL Workbench (optional, very convenient though)
3) Ubuntu 20.04 .iso file(Can probably use a newer version's image file)
4) VMWARE Workstation

First, set up a dev server by
1) Installing MySQL and MySQL Workbench
2) Set up a Virtual Machine on VMWare using the Ubuntu .iso file
3) Set up MySQL and SSH on the VM
4) Set both to run on VM on terminal start
5) Tunnel a connection between MySQL Workbench and your VM

Next, after the dev server has been created
1) Use .mwb file for "studentalert.mwb" to run the working DB.  The
theoretically correct DB, "correctedsa.mwb" does NOT have a working DB.
Open this model in your MySQL WB connection
2) Forward engineer the Database
3) Left Click on the schema studentalart, left click tables, and right
click each table and select "Import Wizard".  Use the correspondingly
named .csv file to fill each table with the data we used.  NOTE: you may need
to fill certain tables before others such as University Response and location 
before incident and incident before victim

From Here, we can run the web interface.  Ours takes the form of a webpage
that has links that return the results of various queries that are listed on 
the page itself
1) Open VM
2) Download a copy of zip file and extract all the python and html files in the 
folder listed "CSDS341_Final_Project_Code".
3) Ensure that all the files are in the same directory, AND that the html files are
within a folder labeled "templates"
4) Run the file named "csds341webinterface.py".
5) Open a browser and navigate to localhost 127.0.0.1:5000/
6) You should now be at the index page.  Browse the links as you see fit.

