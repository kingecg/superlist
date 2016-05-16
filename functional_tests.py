#  charset=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.implicitly_wait(1000)
        self.browser.quit()


    def test_can_start_a_list_and_retrive_it_later(self):
        # tom open list home page
        self.browser.get("http://localhost:8000")
        # he find TO-DO in title
        self.assertIn('TO-DO', self.browser.title, 'Assert title include to do')
        #她注意到头部有TO-DO字样
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('TO-DO',header_text,'她注意到头部有TO-DO字样')
        #可以输入待办事项
        input_box= self.browser.find_element_by_id("id_new_item")
        self.assertEqual(input_box.get_attribute('placeholder'),'please input new todo')
        #after input something and press enter, ui is update
        self._inputToDoItme('买鱼虫')
        self._assertToDoItemInList('1:买鱼虫')

        #input another an item and press enter , there should be two items in list
        self._inputToDoItme('用鱼虫钓鱼')
        self._assertToDoItemInList('1:买鱼虫')
        self._assertToDoItemInList('2:用鱼虫钓鱼')
        # self.fail('Finish the test')

    def _inputToDoItme(self,item):
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys(item)
        input_box.send_keys(Keys.ENTER)
        return

    def _assertToDoItemInList(self,item):
        list_box = self.browser.find_element_by_id('id_list_table')
        rows = list_box.find_elements_by_tag_name('tr')
        self.assertIn(item, [row.text for row in rows])

if __name__ == '__main__':
    unittest.main()
