from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.book.book_db import BookDb

api = Namespace('Book', description='Manager data of books')

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
        return BookDb.index(), 200

    @api.expect(modelo)
    def post(self):
        return BookDb.create(request.json), 201


@api.route('/<id>')
class BookIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return BookDb.index(int(id)), 200

    @api.response(201, "Alterado com sucesso")
    @api.expect(modelo)
    def put(self, id: int):
        return BookDb.update(int(id), request.json), 201

    @api.response(201, "Deletado com sucesso")
    def delete(self, id: int):
        return BookDb.delete(int(id)), 201
