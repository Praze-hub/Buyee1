import factory

from E_Commerce.product.models import Brand, Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test_category'



