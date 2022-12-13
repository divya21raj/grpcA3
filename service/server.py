import logging
from concurrent import futures

import grpc

import inventory_service_pb2, book_pb2, inventory_service_pb2_grpc
from inventory_service_pb2_grpc import CreateBookServicer


class Server(CreateBookServicer):
    book_dict = {
        "isbn1": {
            "author": {
                "birth_year": -2057565939,
                "first_name": "ad nisi",
                "last_name": "dolor cupidatat non elit anim"
            },
            "genre": "UNKNOWN",
            "isbn": "isbn1",
            "published_year": -289307578,
            "title": "ad pariatur"
        }
    }

    def CreateBook(self, request, context):
        print(request.book)
        self.book_dict[request.book.isbn] = request.book
        return inventory_service_pb2.Response(code=200)

    def GetBook(self, request, context):
        print(request)
        book = self.book_dict.get(request.isbn, None)
        print(book)
        if book:
            book_object = book_pb2.Book(isbn=book["isbn"], title=book["title"], author=book["author"],
                                        genre=book["genre"], published_year=book["published_year"])
            return book_object

        return book_pb2.Book()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_CreateBookServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
