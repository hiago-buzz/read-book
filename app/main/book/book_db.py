import sqlite3 as sql
from datetime import datetime
from app.main.utils.response import Response


class BookDb:

    @classmethod
    def create(cls, book):
        try:
            title = book['title']
            author = book['author']
            genre = book['genre']
            finish = book['finish']
            createAt = datetime.now()

            with sql.connect('database.db') as con:
                cur = con.cursor()

                cur.execute("INSERT INTO books (title,author,genre,finish,createAt) VALUES (?,?,?,?,?)",
                            (title, author, genre, finish, createAt))
                con.commit()

                sts = '200'
                msg = "Record successfully added"

                return Response.format_response(sts, msg)
                con.close()
        except:
            sts = '500'
            msg = "error in insert operation"
            return Response.format_response(sts, msg)
            con.close()

    @classmethod
    def indexAll(cls):
        try:
            with sql.connect('database.db') as con:
                con.row_factory = sql.Row

                cur = con.cursor()
                cur.execute("select * from books")
                print(cur)
                sts = '200'
                msg = "Listed success"

                data = [
                    dict(
                        id=row[0],
                        title=row[1],
                        author=row[2],
                        genre=row[3],
                        finish=row[4],
                        createAt=row[5]
                    ) for row in cur.fetchall()
                ]

                return Response.format_response(sts, msg, data)
                con.close()
        except:
            sts = '500'
            msg = "error in list operation"

            return Response.format_response(sts, msg)
            con.close()

            
