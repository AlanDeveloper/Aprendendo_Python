from flask import Flask 
from flask import render_template

app = Flask(__name__, template_folder='template')

@app.route('/user/<user>', methods = ['POST'])
def ola(user):
    return render_template('form.html', name=user)

def main():
    app.env = 'development'
    app.run(debug=True, port=7000)

if __name__ == "__main__":
    main()
