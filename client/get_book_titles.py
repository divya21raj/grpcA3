from inventory_client import InventoryClient

if __name__ == "__main__":
    client = InventoryClient("localhost", 50051)

    isbn_list = ["isbn1", "isbn2"]
    for isbn in isbn_list:
        book = client.get_book(isbn)
        print(book)

