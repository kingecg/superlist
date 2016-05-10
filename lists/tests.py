from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_root_url_resolve_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_should_return_correct_html(self):
        request= HttpRequest()
        response = home_page(request)
        self.assertEqual(response.content.decode(), render_to_string("home.html"))

# Create your tests here.
