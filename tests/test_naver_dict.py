import sys
sys.path.append('..')
from web_scraper.naver_dict import NaverDict


class TestNaverDict:
    def test_no_search_text(self):
        NaverDict('')


if __name__ == "__main__":
    TestNaverDict().test_no_search_text()