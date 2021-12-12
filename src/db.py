import sqlite3
import fire
from config.cfg import DATABASE, TRAINING_DATA
import pandas as pd
from utils import read_data
from sqlalchemy import create_engine


def create_table():
    print('Start to create table ...')
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('''CREATE TABLE iris ("index", "sepal.length" real, "sepal.width" real, "petal.length" real, "petal.width" real, "variety" text)''')
    con.commit()
    con.close()
    print(f'Iris table created finish. DB: {DATABASE}')


def insert_data():
    print('Start to read data...')
    df = read_data(TRAINING_DATA)
    engine = create_engine(f'sqlite:///{DATABASE}', echo=False)
    df.to_sql('iris', con=engine, if_exists='append')
    print('Sample data insert finish.')


if __name__ == '__main__':
    fire.Fire()