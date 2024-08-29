### Retrieve the Book Instance

```python
book = Book.objects.get(id=1)
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
