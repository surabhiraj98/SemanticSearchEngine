# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 00:14:55 2020

@author: HP
"""
import dns.resolver
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234"
)

print(mydb)

if(mydb):
    print("Connection Succsessful")
    
else:
    print("Connection Unsuccessful")