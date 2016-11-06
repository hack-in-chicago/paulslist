from django.test import TestCase
from classifieds.models import Category, Post

class ModelTestCases(TestCase):
    def setUp(self):
        Category.objects.create(name="foo")
        foo = Category.objects.get(name="foo")
        Post.objects.create(title="Make $$$ Fast", description="Go rob a bank.", category=foo,
            is_completed=False, is_insider=True)

    def test_category(self):
        category = Category.objects.get(name="foo")
        self.assertEqual(category.name, "foo")

    def test_post(self):
        post = Post.objects.get(title="Make $$$ Fast")
        self.assertEqual(post.description, "Go rob a bank.")
        self.assertEqual(post.category.name, "foo")
        self.assertEqual(post.is_completed, False)
        self.assertEqual(post.is_insider, True)
