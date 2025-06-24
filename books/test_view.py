def test_get_absolute_url(self):
       book = Book.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of book #1
       #and load the URL /books/list/1
       self.assertEqual(book.get_absolute_url(), '/books/list/2')