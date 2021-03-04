from flask import Flask,render_template,request
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)

users = {}

todos = {}

@app.route('/user', methods=['GET', 'PUT', 'POST', 'DELETE'])
def getURL():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        users[username] = password
        return {username: password}

    if request.method == 'PUT':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        users[username] = password
        return {username: password}

    if request.method == 'GET':
        return users

    if request.method == 'DELETE':
        username = request.form['username']
        del users[username]
        del users[password]
        return users



@app.route('/notes', methods=['GET', 'PUT', 'POST', 'DELETE'])
def getURL1():
    if request.method == 'POST':
        id = request.form['id']
        data = request.form['data']
        print(id, data)
        todos[id] = data
        return {id: data}

    if request.method == 'PUT':
        id1 = request.form['id']
        data = request.form['data']
        print(id1, data)
        todos[id1] = data
        return {id1: data}

    if request.method == 'GET':
        return todos

    if request.method == 'DELETE':
        id = request.form['id']
        del todos[id]
        return todos


if __name__ == "__main__":
    app.run(debug=True)