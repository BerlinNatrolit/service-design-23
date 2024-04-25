from flask import Flask

app = Flask(__name__)

names = ['Erik Baaken', 'Magnus Petersson', 'Jannik Skovgaard', 'Ivan Kokalovic']

@app.route('/')
def hello():
    return 'Welcome to this API\nGo to endpoint students for more things.'

@app.route('/students')
def students():
    stus = '{"students":['
    for name in names:
        stus = stus + '{"name":"' + name + '"},'
    
    if stus[-1] == ',':     # Remove last , from previous loop so we get correct JSON.
        stus = stus[:-1]
    stus = stus + ']}'
    return stus

if __name__ == '__main__':
    app.run()