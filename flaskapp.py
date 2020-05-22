from flask import Flask, render_template, url_for, request, redirect
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '189aee7e774aaedce1269c5a35966db7'

@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
