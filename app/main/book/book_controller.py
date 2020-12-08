from flask_restplus import Resource, Namespace, fields
from flask import request
from app.main.book.book_db import BookDb
from app.main.utils.response import Response

api = Namespace('Book', description='Manager data of books')

parser = api.parser().add_argument('user_name', location='headers')

modelo = api.model('BookModel', {
    'title': fields.String,
    'author': fields.String,
    'finish': fields.Date,
    'genre': fields.String,
    'user_name': fields.String,
}, validate=True)


@api.doc(parser=parser)
@api.route('/')
class BookController(Resource):

    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        try:
            request.headers['User-Name']
            return BookDb.index(), 200
        except KeyError:
            return Response.format_response('401', 'Unauthorized user Name is required')

    @api.doc(body=modelo)
    def post(self):
        try:
            request.headers['User-Name']
            return BookDb.create(request.json), 201
        except KeyError:
            return Response.format_response('401', 'Unauthorized user Name is required')


@api.doc(parser=parser)
@api.route('/<id>')
class BookIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        try:
            request.headers['User-Name']
            return BookDb.index(int(id)), 200
        except KeyError:
            return Response.format_response('401', 'Unauthorized user Name is required')

    @api.response(201, "Alterado com sucesso")
    @api.expect(modelo)
    def put(self, id: int):
        try:
            request.headers['User-Name']
            return BookDb.update(int(id), request.json), 201
        except KeyError:
            return Response.format_response('401', 'Unauthorized user Name is required')

    @api.response(201, "Deletado com sucesso")
    def delete(self, id: int):
        try:
            request.headers['User-Name']
            return BookDb.delete(int(id)), 201
        except KeyError:
            return Response.format_response('401', 'Unauthorized user Name is required')
        
