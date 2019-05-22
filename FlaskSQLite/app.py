from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("Olá Mundo! Estou aprendendo Flask", 200)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tb_aluno;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
def getAlunosByID():
    pass
def getCursos():
    pass
def getCursosByID():
    pass
def getTurmas():
    pass
def getTurmasByID():
    pass

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
