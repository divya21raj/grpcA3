import grpc
import sys

sys.path.append('../service/')

import inventory_service_pb2_grpc, inventory_service_pb2


class InventoryClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.client = inventory_service_pb2_grpc.InventoryServiceStub(self.channel)

    def create_book(self, book):
        return self.client.CreateBook(inventory_service_pb2.CreateBookRequest(book=book))

    def get_book(self, isbn):
        return self.client.GetBook(inventory_service_pb2.GetBookRequest(isbn=isbn))
