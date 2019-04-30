from flask import Flask
from funcDAO import serverDAO

app = Flask(__name__)

@app.route('/func/<int:cod>')
def searchFunc(cod):
    svDAO = serverDAO()
    func = svDAO.buscarFuncionario(cod)

    return func.__str__()

def main():
    app.env = 'development'
    app.run(debug=True, port=7000)

if __name__ == "__main__":
    main()
