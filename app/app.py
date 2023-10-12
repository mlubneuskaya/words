import datetime
import psycopg2
import os
from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Sample API"})

app = Flask(__name__)

app.register_blueprint(blueprint, url_prefix=SWAGGER_URL)

DATABASE_URL = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()


@app.route('/add/', methods=['POST'])
def enter_word():
    word = request.json
    word = "'{}'".format(word)
    current_time = "'{}'".format(str(datetime.datetime.now()))
    cursor.execute("INSERT INTO entered_data VALUES ({}, {});".format(word, current_time))
    conn.commit()
    return "added word {}".format(word)


@app.route('/get/', methods=['GET'])
def get_words():
    cursor.execute("SELECT * FROM entered_data ORDER BY time DESC LIMIT 5")
    words = cursor.fetchall()
    return words


@app.route('/', methods=['GET'])
def hello_world():
    return "Hello world"


if __name__ == '__main__':
    app.run()
    cursor.close()
    conn.close()
