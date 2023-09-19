import sqlite3

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

    def store_columns(self, table_name, cols):
        self.tables_dic[table_name] = cols

    def create_table(self):
        name = self.ask_table_name()
        cols = self.ask_for_columns()
        statement = "CREATE TABLE {} (".format(name)
        for col in cols:
            statement = statement + col + ','
        statement = statement+')'
        statement = statement[::-1].replace(',','',1)
        statement = statement[::-1]
        self.cur.execute(statement)

    def get_tables(self):
        res = self.cur.execute("SELECT name FROM sqlite_master")
        return res.fetchall()

butler = Butler('test.db')
ques = input('Create new table? (y/n) ')
if ques == "y":
    try:
        butler.create_table()
    except Exception as e:
        print(e)
res = butler.get_tables()
print('\nthe tables are: {}'.format(res))
# Insert into a table 
