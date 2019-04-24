from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nome>")
def hello_world(nome):
    return ("Olá %s! Estou aprendendo Flask" %(nome), 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
