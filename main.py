from flask import Flask
from dotenv import dotenv_values


app: Flask = Flask(__name__)
v: dict =  dotenv_values('.env')


@app.route('/')
def index() -> str:
    return 'hello'



if __name__ == '__main__':
    app.run(v['HOST'], v['SPORT'], debug=True)