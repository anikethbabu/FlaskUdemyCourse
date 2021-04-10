from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!<h1>"

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1] == 'y':
        return "<h1>Hi {}! You puppylatin name is {}<h1>".format(name, name[0:len(name) - 1] + "iful")
    return "<h1>Hi {}! You puppylatin name is {}<h1>".format(name, name + 'y')

if __name__ == '__main__':
    app.run()