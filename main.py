import mysql.connector
import os

try:
    conn = mysql.connector.connect(
        user="root",
        password="",
    )

except mysql.connector.Error as e:
    print(f"Terjadi error pada program : {e}")
    print("Silahkan jalankan ulang program")
    os.system("C:\\xampp\\xampp-control.exe")

cur = conn.cursor()


def queryInsert():
    repeat = "y"
    while repeat != "n":
        showTable()
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            cur.execute(f"DESC {table}")
            field = [f[0] for f in cur]
            value = []

            for i in range(len(field)):
                value.append(input(f"Masukkan {field[i]} : "))
            
            sqlInsertQuery = f"""INSERT INTO {table} VALUES {tuple(value)}"""

            cur.execute(sqlInsertQuery)
            conn.commit()
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")
            mainMenu()

        repeat = input("\nIngin melanjutkan? [Y/N or Any key] : ").lower()


def showTable():
    os.system("cls")
    useDatabase()
    cur.execute("SHOW TABLES")
    listTable = ["".join(x) for x in cur]

    print("="*40)
    print("|{:^38}|".format("TABEL"))
    print("="*40)
    for i in range(len(listTable)):
        print("|{:^38}|".format(listTable[i]))
    print("="*40)


def querySelect():
    repeat = "y"
    while repeat != "n":
        showTable()
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            cur.execute(f"SELECT * FROM {table}")
            conTable = [list(x) for x in cur]

            for i in range(len(conTable)):
                print(conTable[i])
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")
            mainMenu()

        repeat = input("\nIngin melanjutkan? [Y/N or Any key] : ").lower()


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


def useDatabase():
    print("Database saat ini :", conn.database)


def mainMenu():
    os.system("cls")
    useDatabase()
    print("="*20)
    print("[1] Pilih database")
    print("[2] Query select")
    print("[3] Query insert")
    print("[0] Exit")
    print("="*20)

    choose = int(input("Masukkan pilihan : "))
    if choose == 1:
        selectDatabase()
        mainMenu()
    elif choose == 2:
        querySelect()
        mainMenu()
    elif choose == 3:
        queryInsert()
        mainMenu()
    elif choose == 0:
        exit()
    else:
        input("Input tidak sesuai!\n Tekan enter untuk lanjut!")
        mainMenu()


mainMenu()