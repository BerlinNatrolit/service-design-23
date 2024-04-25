from flask import Flask, request
import sqlite3
import requests
import json

app = Flask(__name__)
con = sqlite3.connect('local.db', check_same_thread=False)
con.row_factory = sqlite3.Row
cursor = con.cursor()

@app.route('/')
def index():
    return "navigate to /items for a list of items"

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        # return list of items
        response = cursor.execute('SELECT * FROM quotes')
        unpacked = [{k: item[k] for k in item.keys()} for item in response.fetchall()]
        return '{"students":' + str(unpacked).replace("'", '"') + '}'
    elif request.method == 'POST':
        student = request.form.get('student')
        git_user = request.form.get('git_user')
        cursor.execute(f'INSERT INTO quotes (student, favourite_user) VALUES (?,?)', (student, git_user))
        con.commit()
        return 'student added'


@app.route('/items/<item_id>', methods=['GET', 'DELETE'])
def profile(item_id):
    if request.method == 'GET':
        github_user = cursor.execute('SELECT favourite_user FROM quotes WHERE id=' + str(item_id)).fetchall()[0][0]
        user_details = requests.get('https://api.github.com/users/' + github_user)
        print(user_details)
        return str(user_details.text)
    elif request.method == 'DELETE':
        response = cursor.execute('DELETE FROM quotes WHERE id=' + str(item_id))
        con.commit()
        if (response.rowcount > 0):
            return "deleted"
        else:
            return 'could not delete', 404

@app.route('/api/docs')
def documentation():
    return open('docs/docs.yaml')

if __name__ == '__main__':
    app.run(debug=True)