from django.test import TestCase

class TestMarkdownModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Test Data Setup Boilerplate")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to set up clean data.")
        pass

    def test_sample_method(self):
        print("Method: Test sample test method")
        self.assertFalse(False)

