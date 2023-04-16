import mysql.connector
import pandas as pd
import os
from collections import namedtuple

try :
    conn = mysql.connector.connect(
        user="root",
        password="",
        database="resto" #Ubah nama database disini dan sesuaikan nama tabelnya
    )
except mysql.connector.Error as e:
    print(f"Terjadi error pada program : {e}")

cur = conn.cursor()
def showMenu():
    cur.execute("SELECT * FROM menu")
    for menu in cur:
        print(list(menu))

def showPembelian():
    cur.execute("SELECT * FROM pembelian")
    for pembelian in cur:
        print(list(pembelian))

def mainMenu():
    status = "y"
    while status != "n":
        os.system("cls")
        print("[1] Lihat Data Menu Resto")
        print("[2] Lihat Data Pembelian")
        pilihMenu = int(input("Pilih menu : "))
        if pilihMenu == 1:
            showMenu()
        elif pilihMenu == 2:
            showPembelian()
        
        status = input("Lanjut?[Y/N] : ").lower()

mainMenu()