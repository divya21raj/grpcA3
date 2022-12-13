from inventory_client import InventoryClient


def get_books(client, isbn_list):
    books = []
    for isbn in isbn_list:
        book = client.get_book(isbn)
        print(book)
        books.append(book)
    return books


if __name__ == "__main__":
    get_books(InventoryClient("localhost", 50051), ["isbn1", "isbn2"])
