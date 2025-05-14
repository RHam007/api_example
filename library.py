from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

from flask import jsonify



BOOKS = {
    "1": {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "publication_year": 1979},
    "2": {"title": "1984", "author": "George Orwell", "publication_year": 1949},
    "3": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": 1960}
}

class Books(Resource):
    def get(self):
        return jsonify(BOOKS)
    
from flask import request

class Books(Resource):
    def get(self):
        search_query = request.args.get('search')
        if search_query:
            results = [book for book in BOOKS.values() if
                       search_query.lower() in book['title'].lower() or
                       search_query.lower() in book['author'].lower()]
            return jsonify(results)
        return jsonify(BOOKS)
    
from flask_restful.reqparse import RequestParser
from flask import abort

parser = RequestParser()
parser.add_argument('title', type=str, required=True, help="Title is required")
parser.add_argument('author', type=str, required=True, help="Author is required")
parser.add_argument('publication_year', type=int, required=True, help="Publication year is required")

def authenticate(username, password):
    return username == 'admin' and password == 'password'

class Books(Resource):
    def post(self):
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password):
            abort(401, description="Authentication required")

        args = parser.parse_args()
        new_id = str(int(max(BOOKS.keys(), default=0)) + 1)
        BOOKS[new_id] = {
            'title': args['title'],
            'author': args['author'],
            'publication_year': args['publication_year']
        }
        return jsonify(BOOKS[new_id])

class Book(Resource):
    def get(self, book_id):
        if book_id not in BOOKS:
            abort(404, description="Book not found")
        return jsonify(BOOKS[book_id])

api.add_resource(Books, '/books/')
api.add_resource(Book, '/books/<string:book_id>')

from threading import Thread

def run_app():
    app.run(debug=True, use_reloader=False)

thread = Thread(target=run_app)
thread.start()


#install postman (postman.com/downloads)

"""
New book data:

{
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "publication_year": 1979
}

Step 6
Setting up Authentication (Basic Auth)
Some of your API endpoints, like adding a new book, might require authentication to restrict access to authorized users. This is like ensuring that only librarians can add new books to the library. Postman provides a convenient way to include authentication credentials in your requests. Here's how to set up Basic Auth in Postman:

In your Postman request tab, click on the "Authorization" tab.

Select "Basic Auth" from the "Type" dropdown.

Enter the username and password you've set up for your API.

Now, when you send the request, Postman will include the authentication credentials. If you get a 401 Unauthorized error even after setting up authentication, double-check that you've entered the correct username and password, and that your API's authentication logic is working as expected.

"""

