from django.db import models
from books.models import Book  # Ensure 'books' app is in INSTALLED_APPS

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(blank=True, null=True)  # Allow null if blank is True

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}"
