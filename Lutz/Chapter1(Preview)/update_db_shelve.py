from initdata import tom
import shelve

db = shelve.open('people-shelve')
sue = db['sue']
tom = db['tom']
sue['pay'] *= 1.10
tom['name'] = 'Tom Tom'
db['sue'] = sue
db['tom'] = tom
db.close()