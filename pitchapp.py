from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)



app.config['SECRET_KEY'] = '3a3b404948c4e3801e8a2a76859c4658'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User (db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), unique = True, nullable = False )
    email = db.Column(db.String(120), unique = True, nullable = False )
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)


    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(20), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


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