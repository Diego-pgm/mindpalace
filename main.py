from butler import Butler

def custom_menu(opts):
    hor = '###' * 10
    header = '{} file updater {}\n'.format(hor,hor)
    body = ''
    for key, value in opts.items():
        body = body + '{}) {}\n'.format(key, value)
    return header + body

my_butler = Butler('maintest.db')
opts = {"1":"Crete table", "2": "Show tables.", "3":"Show columns", "4":"Insert into table", "5":"Show table values", "0":"exit"}

while True:
    menu = custom_menu(opts)
    print(menu)
    opt = input('Select an option: ')
    if opt == '0':
        break
    elif opt == '1':
        my_butler.create_table()
        print('[+] Table created!')
    elif opt == '2':
        tables = my_butler.get_tables()
        print('[+] The tables are: {}'.format(tables))
    elif opt == '3':
        tables = my_butler.get_tables()
        print('Select a table: {}'.format(tables))
        table_name, cols = my_butler.get_columns()
        print('[+] The columns of {} are {}: '.format(table_name, cols))
    elif opt == '4':
        print('[-] Currently In Development! Sorry for the inconvenience')
    elif opt == '5':
        print('[-] Currently In Development! Sorry for the inconvenience')
    input('[+] Press any key to continue')