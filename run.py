'''
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    a = 1
    b = 6
    c = a + b
    return "Hola mundo, mi suma es esta: " + str(c)
'''

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)