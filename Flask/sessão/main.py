from flask import Flask, render_template, request, session
from funcDAO import funcDAO

app = Flask(__name__, template_folder='template')

@app.route('/func', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        res = funcDAO().login(request.form['login'], request.form['pass'])

        if res == True:
            session['username'] = request.form['login']
            session['password'] = request.form['pass']
            return render_template('logado.html', date=session)
        else:
            return 'Dados incorretos'
    return render_template('form.html')

@app.route('/exit')
def exit():
    session = []
    return 'deslogado <a href="/func">Home</a>'

def main():
    app.secret_key = 'minha chave'
    app.env = 'development'
    app.run(debug=True, port=7000)

if __name__ == "__main__":
    main()