from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def _createPostRequest(self, postBody: dict) -> object:
        """this method return post request object with postbody
        the postBody is a dict
        """
        request = HttpRequest()
        request.method = "POST"
        for name,value in postBody.items():
            request.POST[name]= value
        return request

    def test_root_url_resolve_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_should_return_correct_html(self):
        request= HttpRequest()
        response = home_page(request)
        self.assertEqual(response.content.decode(), render_to_string("home.html"))

    def test_homepage_can_process_post_request(self):
        posttext = 'By some thing'
        request = self._createPostRequest({'item_text': posttext})
        response = home_page(request)
        self.assertEqual(302,response.status_code)

    def test_homepage_can_save_post_item(self):
        request = self._createPostRequest({
            'item_text':'new_item_add'
        })
        response = home_page(request)
        self.assertEqual(302, response.status_code)
        allItems = list(Item.objects.all())
        self.assertIn('new_item_add',[item.text for item in allItems],'item not saved!')

    def test_homepage_can_display_saved_items(self):
        Item.objects.create(text = 'Entry 1')
        Item.objects.create(text='Entry 2')
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('Entry 1',response.content.decode())
        self.assertIn('Entry 2', response.content.decode())
# Create your tests here.
