from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Product
from django.core.files.uploadedfile import SimpleUploadedFile


User =get_user_model()


class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Папка')
        image = SimpleUploadedFile("koshelekimg.jpg", content=b'', content_type="image/jpg")
        self.product = Product.objects.create(
            category=self.category,
            name="test-product",
            image=image,
            price=Decimal('50'),
        )

    def test_sometest(self):
        self.product.get_absolute_url()
        self.assertEqual(self.product.price, Decimal('50'))
