from flask import Flask
from waitress import serve

from bigMac_app.services import get_country_data

app = Flask(__name__)



@app.route('/')
def main_api():
    return get_country_data()

if __name__ == '__main__':
    serve(app)