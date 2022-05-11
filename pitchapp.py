from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3a3b404948c4e3801e8a2a76859c4658'

@app.route("/")
@app.route("/home")
def main():
    return render_template('main.html')


@app.route("/about")
def about():
    return render_template ('about.html', title = 'About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'An account has been created for {form.username.data}!','success')
        return redirect(url_for('main'))
    return render_template ('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@email.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main'))
        else:
            flash('Login unsuccessful, Please check username and password', 'danger')
    return render_template ('login.html', title = 'Login', form=form)

if __name__=='__main__':
    app.run(debug =True)