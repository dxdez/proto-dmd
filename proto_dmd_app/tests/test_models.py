from django.test import TestCase
from proto_dmd_app.models import MarkdownContent

class TestMarkdownModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        MarkdownContent.objects.create(title="Test Page", content="This is the content of the test page", slug="test-page")
        pass

    def test_single_markdown_model(self):
        test_markdown = MarkdownContent.objects.get(id=1)
        self.assertEqual(test_markdown.title, "Test Page")
        self.assertEqual(test_markdown.content, "This is the content of the test page")
        self.assertEqual(test_markdown.slug, "test-page")

