import mysql.connector
import os

try :
    conn = mysql.connector.connect(
        user="root",
        password="",
    )
    
except mysql.connector.Error as e:
    print(f"Terjadi error pada program : {e}")
    os.system("C:\\xampp\\xampp-control.exe")

cur = conn.cursor()

def queryInsert():
    pass

def showTable():
    os.system("cls")
    useDatabase()
    cur.execute("SHOW TABLES")
    listTable = ["".join(x) for x in cur]

    print("="*40)
    print("|{:38}|".format("TABEL"))
    print("="*40)
    for i in range(len(listTable)):
        print("|{:^38}|".format(listTable[i]))
    print("="*40)

def querySelect():
    showTable()
    choose1 = input("Pilih table : ")
    cur.execute(f"SELECT * FROM {choose1}")
    conTable = [list(x) for x in cur]

    for i in range(len(conTable)):
        print(conTable[i])

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
    
    showTable()

    print("="*20)
    print("[1] Pilih table")
    print("[2] Exit")
    print("="*20)

    choose1 = int(input("Masukkan pilihan : "))
    if choose1 == 1:
        querySelect()
    elif choose1 == 2:
        exit()
    else :
        input("Input tidak sesuai!\n Tekan enter untuk lanjut!")

    querySelect()


mainMenu()