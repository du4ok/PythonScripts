import shelve

db = shelve.open('class-shelve')
bob = db['bob']
bob.giveRaise(.20)
db['bob'] = bob

tom = db['tom']
tom.giveRaise(.25)
db['tom'] = tom
db.close()