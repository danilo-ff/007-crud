import pyodbc 

cnxn = conn = pyodbc.connect('DSN=TESTE; DATABASE=crud_python; Trusted_Connection=yes;')

cursor = cnxn.cursor()