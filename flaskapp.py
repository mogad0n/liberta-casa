from flask import Flask, render_template, url_for, request, redirect, flash
from forms import RegistrationForm
from irc_register import ircregister
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '189aee7e774aaedce1269c5a35966db7' #remove later

@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        response = ircregister(username, password)
        if response == "server failure":
            flash("Server Unavailable")
        elif response == "433":
            flash("Username already taken. Please select a different username")
        elif response == "success":
            flash(f"Account {username} registered")
            return redirect(url_for('hello'))
        elif response == "failure":
            flash("Failure! Please try after some time or use NickServ.")

    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    try :
        port = int(os.getenv("HTTP_PORT"))
    except :
        port = 5000
    host = os.getenv("HTTP_HOST") or "127.0.0.1"
    debug = os.getenv("DEBUG") or True
    app.run(debug=debug, host=host, port=port)
