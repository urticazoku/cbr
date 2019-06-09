import unittest
from selenium import webdriver
import page

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.ru")

    def test(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_google_input("Центральный банк РФ"), True
        main_page.click_search_button()
        search_results_page = page.SearchResultsPage(self.driver)
        search_results_page.get_site()
        cbr_page = page.CBRPage(self.driver)
        assert cbr_page.is_cbr_page(), 'Центральный банк Российской Федерации'
        cbr_page.get_reception()
        cbr_page.send_gratitude()
        cbr_page.about_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()