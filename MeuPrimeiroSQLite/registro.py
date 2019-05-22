import sqlite3

#conexão com o banco,  se já existir ele vai se conectar. Caso contrario, ele irá criar
conn = sqlite3.connect('estudantes.db')
cursor = conn.cursor()

lista = [('Fabio', 'Rua da Merda', '2000-02-20','201513880060'),
('Samuel', 'Rua dos Boy', '2000-02-20','201513680070')]

cursor.executemany("""
    INSERT INTO tb_estudante (nome, endereco, nascimento, matricula)
    VALUES (?,?,?,?)
""", lista)

conn.commit()
print('Dados Inseridos com sucesso.')
conn.close()
