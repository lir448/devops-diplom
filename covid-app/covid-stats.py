import requests
import json
from datetime import date, datetime
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, render_template, request
import sqlite3 as sql


def main_app():
    current_date = date.today()
    target_url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-01-01/{}".format(current_date)
    response = requests.get(target_url)
    global countries, timestamp
    countries = response.json()['countries']
    timestamp = datetime.today().replace(microsecond=0)
    table = response.json()['data']
    table = list(table.values())
    df = pd.DataFrame()


    for element in table:
        df_temp = pd.DataFrame(element)
        df = pd.concat([df,df_temp], axis=1)


    df = df.T
    df = df.drop(['stringency_legacy','stringency_legacy_disp'], axis=1)
    engine = create_engine('sqlite:///stats.db')
    df.to_sql('stats', con=engine, if_exists='replace', index=False)


def stress_test():
    prew = cur = 1
    element = 1500000


    for n in range(int(element-2)):
        prew, cur = cur, prew + cur


main_app()


app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html', countries = countries)


@app.route('/stats', methods=['POST','GET'])
def stats():
   country = request.form.get('country_code')
   con = sql.connect('stats.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from stats where country_code = ? order by deaths", (country,))
   rows = cur.fetchall();
   return render_template('stats.html', rows = rows, country = country)


@app.route('/update')
def update():
   main_app()
   return render_template('update.html', timestamp = timestamp)


@app.route('/stress')
def stress():
   stress_test()
   return render_template('stress.html')


if __name__ == '__main__':
    app.run()
