import mysql.connector
import os

try :
    conn = mysql.connector.connect(
        user="root",
        password="",
    )
    
except mysql.connector.Error as e:
    print(f"Terjadi error pada program : {e}")

cur = conn.cursor()

def queryInsert():
    pass

def querySelect():
    os.system("cls")
    useDatabase()

def showTable():
    os.system("cls")
    useDatabase()
    cur.execute("SHOW TABLES")
    listTable = ["".join(x) for x in cur]

    print("="*15)
    print("|{:13}|".format("TABEL"))
    print("="*15)
    for i in range(len(listTable)):
        print("|{:^13}|".format(listTable[i]))
    print("="*15)


def selectDatabase():
    os.system("cls")
    cur.execute("SHOW DATABASES")
    listDatabase = ["".join(x) for x in cur]

    print("="*25)
    print("|{:^23}|".format("DATABASE"))
    print("="*25)
    for i in range(len(listDatabase)):
        print("|{:<23}|".format(listDatabase[i]))
    print("="*25)

    choose = input("Pilih database : ")
    cur.execute(f"USE {choose}")
    useDatabase()

def useDatabase():
    print("Database saat ini :", conn.database)

def mainMenu():
    os.system("cls")
    print("="*20)
    print("[1] Pilih database")
    print("[2] Exit")
    print("="*20)

    choose = int(input("Masukkan pilihan : "))
    if choose == 1:
        selectDatabase()
    elif choose == 2:
        exit()
    else :
        input("Input tidak sesuai!\n Tekan enter untuk lanjut!")
        mainMenu()

mainMenu()