import mysql.connector

def Conectar():
    db = mysql.connector.connect(host='localhost', user='root', password='21122012', database='testdatabase')
    return db

def CriarTabela(db):
    mycursor = db.cursor()
    mycursor.execute("create table RH(id int, nome varchar(50), cargo varchar(50), salario double)")

def Inserir(db):
    mycursor = db.cursor()
    mycursor.execute("insert into RH(id, nome, cargo, salario) values(1, 'Lorran', 'DEV', 20.00)")

def Buscar(db):
    mycursor = db.cursor()
    mycursor.execute("select * from testdatabase.RH")
    for x in mycursor:
        print(x)


Banco = Conectar()
Inserir(Banco)
Buscar(Banco)