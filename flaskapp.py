from flask import Flask, render_template, url_for, request, redirect
from forms import RegistrationForm
from irc_register import ircregister


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
        ircregister(username, password)
        response = ircregister()
        if response == "server failure":
            print("x") #add a redirect to a different route?
        elif response == "433":
            print("Please select a different Nick") # Figure out how to deliver this response. popups suck.
        elif response == "success":
            print("Successfull Registration") # add a redirect to the home page?
        elif response == "failure":
            print("Unknown Error") # Try later...

    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
