from flask import Flask,render_template,request
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)

users = {}

todos = {users: }



@app.route('/notes', methods=['GET', 'PUT', 'POST', 'DELETE'])
def getURL1():
    if request.method == 'POST':
        username = request.form['username']
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