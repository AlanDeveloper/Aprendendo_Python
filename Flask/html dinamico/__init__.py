#!-*- conding: utf8 -*-
from flask import Flask, render_template, request
from dep import Departamento
from deptoDAO import depDAO
from func import Funcionario
from funcDAO import funcDAO

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

# Registro

@app.route('/usuario', methods = ['GET', 'POST'])
def registerFunc():
    if request.method =='POST':
        obj = Funcionario(request.form['name'], request.form['depto'])
        funcDAO().inserirFuncionario(obj)

        return render_template('view.html', name=obj.obterNome())
    
    deptos = depDAO().buscarDepartamentos()
<<<<<<< HEAD
    return render_template('form.html', reg='/usuario', deptos = deptos, register=True)

@app.route('/depto', methods = ['GET', 'POST'])
def registerDepto():
    if request.method =='POST':
        obj = Departamento(request.form['name'])
        depDAO().inserirDepartamento(obj)

        return render_template('view.html', name=obj.obterNome())
    return render_template('form.html', reg = '/depto',register=False)

# Procurar

@app.route('/buscaFunc/<int:cod>')
def searchFunc(cod):
    func = funcDAO().buscarFuncionario(cod)

    return render_template('search.html', obj = func)

@app.route('/buscaDepto/<int:cod>')
def searchDepto(cod):
    dep = depDAO().buscarDepartamento(cod)

    return render_template('search.html', obj = dep)

# Listar

@app.route('/listFunc')
def listFunc():
    funcs = funcDAO().buscarFuncionarios()

    return render_template('list.html', objs = funcs)

@app.route('/listDepto')
def listDepto():
    deptos = depDAO().buscarDepartamentos()
=======
    return render_template('form.html', deptos = deptos)

@app.route('/depto', methods = ['GET', 'POST'])
def registerDepto():
    if request.method =='POST':
        obj = Departamento(request.form['name'])
        depDAO().inserirDepartamento(obj)

        return render_template('view1.html', name=obj.obterNome())
    return render_template('form1.html')


# Procurar

@app.route('/buscaFunc/<int:cod>')
def searchFunc(cod):
    func = funcDAO().buscarFuncionario(cod)
>>>>>>> 6d9e546586af24cf73778705315e89eb9c53f1f7

    return render_template('list.html', objs = deptos)

@app.route('/buscaDepto/<int:cod>')
def searchDepto(cod):
    dep = depDAO().buscarDepartamento(cod)

    return render_template('search1.html', obj = dep.__str__())

# Listar

@app.route('/listFunc')
def listFunc():
    funcs = funcDAO().buscarFuncionarios()

    return render_template('listFunc.html', funcs = funcs)

@app.route('/listDepto')
def listDepto():
    deptos = depDAO().buscarDepartamentos()

    return render_template('listDepto.html', deptos = deptos)


def main():
    app.env = 'development'
    app.run(debug=True, port=7000)

if __name__ == "__main__":
    main()
