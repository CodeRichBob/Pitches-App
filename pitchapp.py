from flask import Flask, render_template, url_for 
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3a3b404948c4e3801e8a2a76859c4658'

@app.route("/")
@app.route("/main")
def main():
    return render_template('main.html')


@app.route("/About")
def about():
    return "<h1>Here you learn about us</h1>"

if __name__=='__main__':
    app.run(debug =True)