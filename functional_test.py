from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        #암묵적 대기 추가
        self.browser.implicitly_wait(3)
        # 셀레늄 테스트에 있어 기본적인 로직이다.

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 델라는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러간다
        self.browser.get('http://localhost:8000')
        # 웹 페이지 타이틀과 헤더가 'To-do'를 표시하고있다.
        self.assertIn('To-Do', self.browser.title)
        # 테스트 어설션을 만들기 위해, assert 대신에 self.assertIn 사용
        self.fail('Finish the test!')
        # 강제적 테스트 실패 

        # 바로 작업을 추가하기로 한다.

        # "세일 상품 사기" 라고 텍스트 상자에 입력한다

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에 
        # "1: 세일 상품 사기" 아이템이 추가된다.

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
        # 다시 "세일 상품 사고 사용하기" 라고 입력한다.
        
        # 페이지는 다시 갱신되고, 두 개의 아이템이 목록에 보인다
        # 델라는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
        # 사이트는 그녀를 위한 특정 URL을 생성해 준다.
        # 이때 URL에 대한 설명도 함께 제공된다.
        
        # 해당 URL에 접속하면 그녀가 만든 작업 목록이 그대로 있는 것을 확인 할 수 있다.
        
        # 잔다.

        # 일단 생략 
        browser.quit()

        #assert 'Django' in browser.title

if __name__ == '__main__':
    unittest.main(warnings= 'ignore' )
    # unittest.main() 호출하여 unittest테스트 실행자를 실행한다.
    # 이 코드는 실행자 이기 때문에 클래스에 있어야한다. 