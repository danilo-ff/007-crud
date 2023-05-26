import pyodbc



conn = pyodbc.connect('DSN=TESTE;Trusted_Connection=yes;')
print("Conexão concluida como sucesso")