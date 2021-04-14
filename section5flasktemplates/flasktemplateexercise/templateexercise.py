from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    lowercase = False
    uppercase = False
    number = False

    lowercase = any(c.islower() for c in username)
    uppercase = any(c.isupper() for c in username)
    number = username[-1].isdigit()

    report = lowercase and uppercase and number
    return render_template('report.html', report = report, lowercase = lowercase, uppercase = uppercase, number = number)

if __name__ == '__main__':
    app.run(debug=True)