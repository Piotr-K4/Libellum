from django.contrib.auth.models import User
from django.http import response
from django.test import TestCase
from books.models import Book, Language, BookCategories, SubBookCategories, BookTags
from users.models import Profil
from books.forms import BookForm
from users.models import Profil
from django.urls import reverse

class BookFormTest(TestCase):
    serialized_rollback = True
    def setUp(self):
        self.user =  User.objects.create_user(username="lol", password="zaq1@WSX")
        self.profil = Profil.objects.get(user=self.user)
        self.langugae = Language.objects.create(name="Kurwix", code="KRX")
        self.category = BookCategories.objects.create(categoryName="poezja")
        self.subcategory = SubBookCategories.objects.create(subCategoryName="wiersze", bookcategory=self.category)
        self.booktag = BookTags.objects.create(name="tag1")
        self.book_one = Book.objects.create(
                title = "Book1",
                author = "Book1",
                publisher = "Book1",
                date_realease = "2012-09-09",
                isbn = "8343501236087",
                language = self.langugae,
                category = self.subcategory,
                addedByUser = self.profil,
                pages = 10
                )

        self.book_two = Book.objects.create(
                title = "Book2",
                author = "Book2",
                publisher = "Book2",
                date_realease = "2012-02-09",
                isbn = "8343501236127",
                language = self.langugae,
                category = self.subcategory,
                addedByUser = self.profil,
                pages = 10
                )

    
    def test_tags_split(self):
        """Test written to check addbook view which remove whitespaces and seperate tags from input field"""
        self.client.login(username="lol", password="zaq1@WSX")

        form_data = {
                "title": "Testowo",
                "author": "Tag",
                "tags": "Tag1, Tag2 , Tag3,Tag4",
                "publisher": "Tag",
                "date_realease": "2011-11-11",
                "isbn": "8343501236234",
                "language": self.langugae.pk,
                "category": self.subcategory.pk,
                "addedByUser": self.user.pk,
                "pages": 10,
                }

        response = self.client.post(reverse("addbook"), form_data, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_count_books_by_user(self):
        print(Book.objects.filter(addedByUser=self.profil).count())



