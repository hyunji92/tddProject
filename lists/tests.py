from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


# Create your tests here.
#class SmokeTest(TestCase):   
#    def test_bad_maths(self):
#        self.assertEqual(1 + 1, 3)
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        # HttpRequest 객체를 생성해서 사용자가 어떤 요청을 브라우저에 보내는지 확인한다.
        request =  HttpRequest()
        response =  home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
        # 강조 - 단위 테스트는 기능 테스트에 의해 파생되며 더 실제 코드에 가깝다.
        # 'To-Do lists' text는 띄어쓰기에도 에러가 민감하게 나니까 조심하자.