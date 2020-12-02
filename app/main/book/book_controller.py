from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.book.book_db import BookDb

api = Namespace('Book',description='Manager data of books')

modelo = api.model('BookModel', {
    'title': fields.String,
    'author': fields.String,
    'finish': fields.Date,
    'genre': fields.String,
})

@api.route('/')
class BookController(Resource):
    @api.response(200, "Busca realizada com sucesso") 
    def get(self):
        return BookDb.indexAll(), 200
    @api.expect(modelo) 
    def post(self):
        return BookDb.create(request.json), 201