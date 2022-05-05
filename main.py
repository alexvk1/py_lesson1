import requests
# import json
from flask import Flask
# import math


def get_currencies():
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    js = r.json()
    currencies = list(js['Valute'].values())
    return currencies


def create_html(cur):
    text = '<h1>Курсы:</h1>'
    text += '<table border="1">'
    for cur_i in cur:
        text += '<tr>'
        text += '<td>' + cur_i['Name'] + '(*' + cur_i['CharCode'] + '*):</td><td>' + str(cur_i['Value']) + \
                ' руб </td><td>(' + str(round(cur_i['Previous'] - cur_i['Value'], 2)) + ')</td>'
        # text = text + curr['ID']
        text += '</tr>'
    text += '</table>'
    return text


print('Lets Start 13')
app = Flask(__name__)


@app.route("/")
def index():
    currencies = get_currencies()
    return create_html(currencies)


if __name__ == "__main__":
    app.run()
