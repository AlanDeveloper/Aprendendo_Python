from flask import Flask, render_template, request, session, redirect
from funcDAO import funcDAO

app = Flask(__name__, template_folder='template')

@app.before_first_request
def  before():
    session['logged_in'] = False

@app.route('/')
def redi():
    return redirect('/func')

@app.route('/func', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if session['logged_in'] == False:
            res = funcDAO().login(request.form['login'], request.form['pass'])

            if res:
                session['logged_in'] = True
                session['username'] = request.form['login'] or session['username']
                session['password'] = request.form['pass'] or session['password']
                return redirect('/func/view')
            else:
                return 'Dados incorretos'
        else: 
            return redirect('/func/view')
    return render_template('form.html')

@app.route('/func/view')
def dados():
    if session['logged_in']:
        return render_template('logado.html', date=session)
    return redirect('/func')

@app.route('/func/exit')
def exit():
    session['logged_in'] = False
    return 'deslogado <a href="/func">Home</a>'

@app.route('/func/add', methods=['GET', 'POST'])
def add():
    if session['logged_in']:
        if request.method =='POST':
            return 'registrado'
        return render_template('add.html')
    return redirect('/func')

def main():
    app.secret_key = 'minha chave'
    app.env = 'development'
    app.run(debug=True, port=2001)

if __name__ == "__main__":
    main()