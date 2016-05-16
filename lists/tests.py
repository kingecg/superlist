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
    def test_homepage_can_process_post_request(self):
        request = HttpRequest()
        request.method = "POST"
        posttext = 'By some thing'
        request.POST['item_text'] = posttext
        response = home_page(request)
        self.assertIn(posttext,response.content.decode())
# Create your tests here.
