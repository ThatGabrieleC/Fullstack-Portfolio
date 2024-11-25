from Website import create_app
from flask import render_template

portfolio = create_app()

@portfolio.route('/')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    portfolio.run(debug=True)