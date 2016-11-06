from django.test import TestCase
from classifieds.models import Category, PeopleGroup, Post

class ModelTestCases(TestCase):
    def setUp(self):
        Category.objects.create(name="foo")
        foo = Category.objects.get(name="foo")
        Post.objects.create(title="Make $$$ Fast", description="Go rob a bank.", category=foo,
            country="United States", is_completed=False, is_insider=True)
        PeopleGroup.objects.create(name="Jews", description="God's chosen people",
            global_pop=11000000, percent_unreached=98)

    def test_category(self):
        category = Category.objects.get(name="foo")
        self.assertEqual(category.name, "foo")

    def test_peoplegroup(self):
        jews = PeopleGroup.objects.get(name="Jews")
        self.assertEqual(jews.description, "God's chosen people")
        self.assertEqual(jews.global_pop, 11000000)
        self.assertEqual(jews.percent_unreached, 98)

    def test_post(self):
        post = Post.objects.get(title="Make $$$ Fast")
        self.assertEqual(post.description, "Go rob a bank.")
        self.assertEqual(post.category.name, "foo")
        self.assertEqual(post.is_completed, False)
        self.assertEqual(post.is_insider, True)
