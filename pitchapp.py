from flask import Flask, render_template, url_for 
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3a3b404948c4e3801e8a2a76859c4658'

@app.route("/")
@app.route("/home")
def main():
    return render_template('main.html')


@app.route("/About")
def about():
    return render_template ('about.html', title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template ('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template ('login.html', title = 'Login', form=form)

if __name__=='__main__':
    app.run(debug =True)