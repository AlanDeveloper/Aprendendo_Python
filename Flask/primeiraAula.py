from flask import Flask

app = Flask(__name__)

@app.route('/teste')
def helloword():
    return "A + B = " + str(soma(1, 1))

@app.route('/teste/<a>/<int:b>')
def testeint(a, b):
    return "Variável: {}, versão: {}".format(a, b)

def soma(a, b):
    return a + b

def main():
    app.env = 'development'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()