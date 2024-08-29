### Delete the Book Instance

```python
book = Book.objects.get(id=1)
book.delete()
books = Book.objects.all()
print(books)
