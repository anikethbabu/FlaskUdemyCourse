from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Aniketh"
    letters = list(name)
    pup_name = {'pup_name':'Sammy'}
    return render_template('basic.html', name=name,letters=letters, pup_name=pup_name)

if __name__ == '__main__':
    app.run(debug=True)