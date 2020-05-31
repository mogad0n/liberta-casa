from flask import Flask, render_template, url_for, request, redirect, flash
from forms import RegistrationForm, VerificationForm
from irc_register import ircregister
from irc_verify import ircverify


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
        email = request.form.get('email')
        response = ircregister(username, password, email)
        if response == "server failure":
            flash("Server Unavailable")
        elif response == "433":
            flash("Username already taken. Please select a different username")
        elif response == "success":
            return redirect(url_for('verify'))
        elif response == "failure":
            flash("Failure! Please try after some time or use NickServ.")

    return render_template('register.html', title='Register', form=form)

@app.route('/verify',methods=['GET', 'POST'])
def verify():
    form = VerificationForm()
    if request.method == 'POST':

        username = request.form.get('username')
        verif_code = request.form.get('verif_code')
        response = ircverify(username, verif_code)
        if response == "server failure":
            flash("Server Unavailable")
        elif response == "433":
            flash("Username under use. Please check your username or visit us for help")
        elif response == "success":
            return redirect(url_for('hello'))
        elif response == "failure":
            flash("Failure! Please try after some time or use NickServ.")
    return render_template('verify.html', title='Verify', form=form)


if __name__ == '__main__':
    app.run(debug=True)
