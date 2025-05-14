
# install the nest_asynco library with flask and flask_restful and uncomment line 13
#!pip install nest_asyncio flask flask_restful

import nest_asyncio as nest_asyncio
from flask import Flask, request
from flask_restful import Api, Resource
from threading import Thread

books = [
    {"isbn": "1234567890", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99},
    {"isbn": "0987654321", "title": "1984", "author": "George Orwell", "price": 8.99}
]

app = Flask(__name__)
api = Api(app)

class Book(Resource):
      def get(self, isbn=None):
        if isbn:
            for book in books:
                if book['isbn'] == isbn:
                    return book, 200
            return {"message": "Book not found"}, 404
        return books, 200

      def post(self):
        new_book = request.json
        books.append(new_book)
        return new_book, 201

      def put(self, isbn):
        for book in books:
            if book['isbn'] == isbn:
                book.update(request.json)
                return book, 200
        return {"message": "Book not found"}, 404

      def delete(self, isbn):
        global books
        books = [book for book in books if book['isbn'] != isbn]
        return {"message": "Book deleted"}, 200

api.add_resource(Book, '/books', '/books/<string:isbn>')

nest_asyncio.apply()
def run_app():
    app.run(port=5000, debug=False)

thread = Thread(target=run_app)
thread.start()

print("API is running! Test it at http://127.0.0.1:5000/books")