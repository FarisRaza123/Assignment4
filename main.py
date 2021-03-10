from flask import Flask,render_template,request
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)



todos = {users: {}}



@app.route('/notes', methods=['GET', 'PUT', 'POST', 'DELETE'])
def getURL1():
    if request.method == 'POST':
        username = request.form['username']
        id = request.form['id']
        data = request.form['data']

        usernotes = todos[username]

        if usernotes is not None:
            usernotes[id] = data
        else
            todos[username] = {id: data}

        return {id: data}

    if request.method == 'PUT':
        if request.method == 'POST':
            username = request.form['username']
            id = request.form['id']
            data = request.form['data']

            usernotes = todos[username]

            if usernotes is not None:
                usernotes[id] = data
            else
                todos[username] = {id: data}

            return {id: data}

    if request.method == 'GET':
        return todos

    if request.method == 'DELETE':
        username = request.form['username']
        id = request.form['id']

        if usernotes is not None:
            del usernotes[id]

        return {id: data}


if __name__ == "__main__":
    app.run(debug=True)