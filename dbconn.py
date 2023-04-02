# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:25:28 2023

@author: HP
"""
import pymysql as pms
#import mysql.connector

conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="asmr",
                   db="t3")



cursor=conn.cursor()

def getcredentials():
    username =[]
    password=[]
    cursor.execute("SELECT * FROM login ")
    result =cursor.fetchall()
    #print(result)
    for i in result:
        username.append(i[0])
        password.append(i[1])
    #print(username)
    return username , password






















