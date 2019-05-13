#!-*- conding: utf8 -*-
from flask import Flask
from flask import render_template, request
from dep import Departamento
from deptoDAO import depDAO
from func import Funcionario
from funcDAO import funcDAO

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario', methods = ['GET', 'POST'])
def register():
    if request.method =='POST':
        obj = Funcionario(request.form['name'], request.form['depto'])
        fcDAO = funcDAO()
        fcDAO.inserirFuncionario(obj)

        return render_template('view.html', name=obj.obterNome())
    
    dpDAO = depDAO()
    deptos = dpDAO.buscarDepartamentos()
    return render_template('form.html', deptos = deptos)

@app.route('/busca/<int:cod>')
def search(cod):
    fcDAO = funcDAO()
    func = fcDAO.buscarFuncionario(cod)

    return render_template('search.html', obj = func.__str__())

def main():
    app.env = 'development'
    app.run(debug=True, port=7000)

if __name__ == "__main__":
    main()
