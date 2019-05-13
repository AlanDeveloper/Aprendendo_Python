from flask import Flask
from flask import render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario', methods = ['GET', 'POST'])
def register():
    if request.method =='POST':
        username = request.form['name']
        return render_template('view.html', name=username)
    return render_template('form.html')

@app.route('/busca/<int:cod>')
def search(cod):
    return render_template('search.html', name=cod)

def main():
    app.env = 'development'
    app.run(debug=True, port=7000)

if __name__ == "__main__":
    main()
