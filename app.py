import time
import sys
import datetime
import psycopg2
from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Sample API"})

app = Flask(__name__)

app.register_blueprint(blueprint, url_prefix=SWAGGER_URL)

conn = None
for i in range(10):
    try:
        conn = psycopg2.connect(database="data", host="postgres-container",
                                user="postgres", password="password", port="5432")
    except psycopg2.OperationalError:
        pass
    if conn:
        break
    time.sleep(1)
if not conn:
    sys.exit()
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


if __name__ == '__main__':
    app.run()
    cursor.close()
    conn.close()
