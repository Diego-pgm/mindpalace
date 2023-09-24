import sqlite3
import pandas as pd

class Butler:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.tables_dic = {}
        
    def ask_table_name(self):
        table_name = input('Insert the table name: ')
        return table_name

    def ask_for_columns(self):
        cols = []
        cont = 1
        while True:
            print('Insert the column names press ENTER to stop')
            col = input('Insert the col no. {}: '.format(cont))
            cont += 1
            if col == '':
                break
            cols.append(col)
        return cols

    def create_query(self, lst): 
        query = "("
        for l in lst:
            query = query + l + ','
        query = query+')'
        query = query[::-1].replace(',','',1)
        query = query[::-1]
        return query

    def create_table(self):
        name = self.ask_table_name()
        cols = self.ask_for_columns()
        query = "CREATE TABLE {} ".format(name)
        end_query = self.create_query(cols)
        query = query+end_query
        print(query)
        try:
            self.cur.execute(query)
        except Exception as e:
            print(e)

    def get_tables(self):
        res = self.cur.execute("SELECT name FROM sqlite_master")
        return res.fetchall()

    def get_columns(self):
        table_name = self.ask_table_name()
        try:
            res = self.cur.execute("SELECT * from {}".format(table_name))
        except Exception as e:
            print(e)
        return table_name, [description[0] for description in res.description]

    def insert_into_table(self):
        tables = self.get_tables()
        print(tables)
        table_name, cols = self.get_columns()
        values = []
        for col in cols:
            value = input('Insert value for {}: '.format(col))
            value = "'{}'".format(value)
            values.append(value)
        query = "INSERT INTO {} VALUES".format(table_name)
        end_query = self.create_query(values)
        query = query + end_query
        print(query)
        try:
            self.cur.execute(query)
            self.con.commit()
            self.get_values(table_name)
        except Exception as e:
            print(e)

    def get_values(self, table_name):
        query = "SELECT * FROM {}".format(table_name)
        table = pd.read_sql(query, self.con)
        print(table)



#res = butler.get_tables()
#print('\nthe tables are: {}'.format(res))
#table_name, cols = butler.get_columns()
#print('The columns of {} are {}: '.format(table_name, cols))
#butler.insert_into_table()
#table_name = butler.ask_table_name()
#butler.get_values(table_name)
