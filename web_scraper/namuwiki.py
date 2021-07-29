from bs4 import BeautifulSoup
from urllib.parse import quote
from modules.getHTML import getHTML


class Chapter:
    """나무위키에서의 한 쳅터에 대한 클래스입니다."""

    def __init__(self, title, content):
        self._title = title
        self._content = content
        self._parent = None
    
    def set_parent(self, parent_node):
        self._parent = parent_node


class Namuwiki:
    """나무위키에서 'search_text'를 검색한 결과를 저장하는 클래스입니다."""

    def __init__(self, search_text: str):
        """'search_text'는 나무위키에서의 검색어 입니다.
        
        example:
            wiki = Namuwiki('강아지')"""
        
        self._chapters = {}
        
        encode_text = quote(search_text)
        url = f'https://namu.wiki/w/{encode_text}'
        html = getHTML(url)
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.select('.wiki-heading')
        titles = list(map(lambda x: x.text, titles))
        contents = soup.select('.wiki-heading-content')
        contents = list(map(lambda x: x.text, contents))
        for idx, title in enumerate(titles):
            self._chapters[title.split('. ')[0]] = Chapter(title.split('[편집]')[0], contents[idx])
        # print(self._chapters[1]._title)
    
    def __str__(self):
        """클래스를 출력하면 첫 번째 쳅터(주로 '개요')의 내용을 출력합니다.
        
        example:
            print(wiki)

            >> 어린 개를 일컫는 순우리말이다. (...이하 중략)"""

        title = self._chapters['1']._title
        content = self._chapters['1']._content
        return f"{title}\n{content}"
    
    def get_list(self):
        """쳅터의 목록을 list 형태로 가져옵니다.
        
        example:
            print(wiki.get_list)
            
            >> ['1', '1.1', '2', '3', '3.1']"""
        
        return list(self._chapters.keys())

    def get(self, chapter_num):
        """'chapter_num'에 해당하는 내용을 출력합니다.
        
        example:
            print(wiki.get(2)
            
            >> 2. 본래 뜻과 다르게 사용하는 경우
                어린 자식이나 손주를 부르는 말로도 쓰며, (...이하 중략)
            
        참고로, 내용이 존재하지 않을 수도 있습니다."""
        
        title = self._chapters[chapter_num]._title
        content = self._chapters[chapter_num]._content
        if not content:
            content = '(내용이 존재하지 않습니다.)'
        return f"{title}\n{content}"

if __name__ == "__main__":
    from pprint import pprint
    wiki = Namuwiki("디스아너드")
    print(wiki.get('2'))
    print(wiki.get_list())