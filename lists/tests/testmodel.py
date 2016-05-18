from django.test import TestCase
from lists.models import Item


class ItemTest(TestCase):
    def test_item_should_can_be_saved(self):
        itemA = Item(text="ItemA")
        itemA.save()
        savedItems = Item.objects.all()
        self.assertEqual(1,savedItems.count())
