import services.database as db
import models.Cliente as cliente

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (cliNome, cliIdade, cliProfissao) 
    VALUES (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM CLIENTE WHERE ClienteID = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumerList[0]

def Alterar(cliente):
    count = db.cursor.execute("""
    UPDATE Cliente
     SET cliNome = ?, cliIdade = ?, cliProfissao = ?
     WHERE ClienteID = ?""",
    cliente.nome, cliente.idade, cliente.profissao, cliente.id).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM Cliente WHERE ClienteID = ?""",
    id).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM CLIENTE")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumerList


