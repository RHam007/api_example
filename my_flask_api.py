"""
This is a learning example of API creation provided by MicroSoft via Coursera.

All code is provided as part of the Python Web Development course, and reproduced here for learning use only.
"""
#Install Flask-RESTful before proceeding
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class BookList(Resource):
    def get(self):
        # Logic to return data, replace with actual data
        return {'books': ["The Lord of the Rings", "Pride and Prejudice", "To Kill a Mockingbird", "1984", "Harry Potter and the Sorcerer's Stone"]}
    
    def post(self):
        # Creating a new book in the example data
        return {'message': 'Book Created'}, 201 # 201 is the expected return code for a successful "creation" operation

class Book(Resource):
    def get(self, book_id):
        # Logic to find and return the book information
        return {'book': {1: 'The Lord of the Rings',
                         2: 'Pride and Prejudice',
                         3: 'To Kill a Mockingbird', 
                         4: '1984',
                         5: "Harry Potter and the Sourcerer's Stone"}} #Again, replace with actual data
    
    def put(self,book_id):
        # Logic to update a specific book
        return {'message': 'Book Updated'}
    
    def delete(self, book_id):
        # Logic to remove a book from the list
        return {'message': 'Book Deleted'}

# Adds the API route (default routing for Flask development server is 127.0.0.1:5000/[route])
api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)