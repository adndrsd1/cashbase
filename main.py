import mysql.connector
import os, asyncio

async def connectToDatabase():
    os.system("C:\\xampp\\xampp_start.exe")

async def closeConnection():
    os.system("C:\\xampp\\xampp_stop.exe")

def lobby(myCursor):
    os.system("cls")
    print("===SELAMAT DATANG DI PROGRAM DATABASE===")
    myCursor.execute("SHOW DATABASES")
    listDatabase = ["".join(x) for x in myCursor]

    print("="*25)
    print("|{:^23}|".format("DATABASE"))
    print("="*25)
    for i in range(len(listDatabase)):
        print("|{:<23}|".format(listDatabase[i]))
    print("="*25)

    choose = input("Pilih database : ")
    myCursor.execute(f"USE {choose}")

def selectDatabase(myCursor):
    os.system("cls")
    myCursor.execute("SHOW DATABASES")
    listDatabase = ["".join(x) for x in myCursor]

    print("="*25)
    print("|{:^23}|".format("DATABASE"))
    print("="*25)
    for i in range(len(listDatabase)):
        print("|{:<23}|".format(listDatabase[i]))
    print("="*25)

    choose = input("Pilih database : ")
    myCursor.execute(f"USE {choose}")

def useDatabase(myConnection):
    print("Database saat ini :", myConnection.database)

def showTable(myConnection, myCursor):
    os.system("cls")
    useDatabase(myConnection)
    myCursor.execute("SHOW TABLES")
    listTable = ["".join(x) for x in myCursor]

    print("="*40)
    print("|{:^38}|".format("TABEL"))
    print("="*40)
    for i in range(len(listTable)):
        print("|{:^38}|".format(listTable[i]))
    print("="*40)

def querySelect(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"SELECT * FROM {table}")
            conTable = [list(x) for x in myCursor]

            for i in range(len(conTable)):
                print(conTable[i])
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")

        repeat = input("\nIngin melanjutkan? [Y/N or Any key] : ").lower()

def queryInsert(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"DESC {table}")
            field = [f[0] for f in myCursor]
            value = []

            for i in range(len(field)):
                value.append(input(f"Masukkan {field[i]} : "))
            
            sqlInsertQuery = f"""INSERT INTO {table} VALUES {tuple(value)}"""

            myCursor.execute(sqlInsertQuery)
        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")

        repeat = input("\nIngin melanjutkan? [Y/N or Any key] : ").lower()

def queryUpdate(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))
    
        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"DESC {table}")
            field = [f[0] for f in myCursor]
            print(field)

            myCursor.execute(f"SELECT * FROM {table}")
            conTable = [list(x) for x in myCursor]

            for i in range(len(conTable)):
                print(conTable[i])
            
            selectField = input("Pilih field yang akan diupdate : ")
            newValue = input("Masukkan data baru : ")
            selectData = input("Masukkan primary key (kolom pertama): ")

            sqlUpdateQuery = f"""UPDATE {table}
                                SET {selectField} = '{newValue}' 
                                WHERE {field[0]} = '{selectData}'"""
            
            myCursor.execute(sqlUpdateQuery)

        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulang!")

def queryDelete(myConnection, myCursor):
    repeat = "y"
    while repeat != "n":
        showTable(myConnection, myCursor)
        print("="*20)
        print("[1] Pilih table")
        print("[2] Exit")
        print("="*20)
        choose = int(input("Masukkan pilihan : "))

        if choose == 1:
            table = input("Pilih table : ")
            myCursor.execute(f"DESC {table}")
            field = [f[0] for f in myCursor]
            print(field)

            myCursor.execute(f"SELECT * FROM {table}")
            conTable = [list(x) for x in myCursor]

            for i in range(len(conTable)):
                print(conTable[i])
                
            selectFieldDelete = input("Pilih field yang akan didelete : ")
            dataDelete = input("Masukkan data yang ingin didelete : ")

            sqlDeleteQuery = f"""DELETE FROM {table}
                                WHERE {selectFieldDelete} = '{dataDelete}'""" 

            myCursor.execute(sqlDeleteQuery) 

        elif choose == 2:
            break
        else:
            input("Input tidak sesuai!\nEnter untuk mengulangi!")            

def mainMenu(myConnection, myCursor):
    while True:
        os.system("cls")
        useDatabase(myConnection)
        print("="*20)
        print("[1] Pilih database")
        print("[2] Query select")
        print("[3] Query insert")
        print("[4] Query update")
        print("[5] Query delete")
        print("[0] Exit")
        print("="*20)

        choose = int(input("Masukkan pilihan : "))
        if choose == 1:
            selectDatabase(myCursor)
        elif choose == 2:
            querySelect(myConnection, myCursor)
        elif choose == 3:
            queryInsert(myConnection, myCursor)
        elif choose == 4:
            queryUpdate(myConnection, myCursor)
        elif choose == 5:
            queryDelete(myConnection, myCursor)
        elif choose == 0:
            break
        else:
            input("Input tidak sesuai!\n Tekan enter untuk lanjut!")

async def main():
    await connectToDatabase()
    print("Connected to database succesfully!")

    try:
        myConnection = mysql.connector.connect(
            user="root",
            password="",
            autocommit = True,
        )

    except mysql.connector.Error as e:
        print(f"Terjadi error pada program : {e}")
    
    myCursor = myConnection.cursor()
    input("Press enter to continue")
    try :
        connectToDatabase()
        lobby(myCursor)
        mainMenu(myConnection, myCursor)
    except Exception as error:
        print(f"Terjadi error : {error}")
    await closeConnection()
    print("Disconnected succesfully!")
    
asyncio.run(main())