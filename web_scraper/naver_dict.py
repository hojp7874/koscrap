from urllib.parse import quote
from .modules.getHTML import getHTML
import json


class NaverDict:
    """네이버 사전에서 단어를 검색한 결과를 출력하는 클래스입니다.
    'search_text'는 네이버 사전에 검색할 단어를 의미합니다."""
    
    def __init__(self, search_text: str):
        """검색한 단어에 대한 정보를 인스턴스로 담습니다."""
        
        encode_text = quote(search_text)
        url = f'https://dict.naver.com/search.dict?dicQuery={encode_text}'
        html = getHTML(url)
        print(dir(html))
        ul = html.find("ul", {"id":"productList"})
        """
        lis = ul.findAll("li", {"class":"search-product"})[:data_num]
        response = {}
        response["error"] = error
        if lis == []:
            response["data"] = f"'{search_text}'에 대한 검색결과가 없습니다."
            return response
        results = {}
        for idx, li in enumerate(lis):
            result = {}
            for item in items:
                try:
                    if item == "image":
                        if idx < 8:
                            data = li.find("dt", {"class":"image"})
                            data = data.find("img").get("src")
                        else:
                            data = "이미지는 8개 까지가 최대입니다."

                    elif item == "name":
                        data = li.find("div", {"class":"name"}).get_text()
                        
                    elif item == "price":
                        data = li.find("em", {"class":"sale"})
                        data = data.find("strong", {"class":"price-value"}).get_text()

                    elif item == "star":
                        data = li.find("span", {"class":"star"})
                        data = data.find("em", {"class":"rating"}).get_text()

                    elif item == "url":
                        data = li.find("a").get("href")
                        data = "https://www.coupang.com" + data
                except Exception as ex:
                    error["exception_error"] = f"error message : {ex}"
                    break

                result[item] = data
            results[idx+1] = result
        response["data"] =results
        if results_type == 'json':
            return json.dumps(response)
        elif results_type == 'dict':
            return response
        """

    def input_valid(items, data_num, results_type):
        error = {}
        # items
        def item_error_processor(error_msg):
            error_msg = f"{error_msg}\n잘못된 정보를 수정합니다...\nitems=['image', 'name', 'price', 'star', 'url']"
            error["items"] = error_msg
            items = ['image', 'name', 'price', 'star', 'url']
            return items

        if type(items) != list or not items:
            items = item_error_processor("'items'의 형식이 잘못되었습니다.")
        else:
            for item in items:
                if item not in ["image", "name", "price", "star", "url"]:
                    items = item_error_processor(f"'{item}'은(는) 잘못된 items 옵션입니다.")
                    break
        # data_num
        if data_num != None and (type(data_num) != int or data_num <= 0):
            error_msg = f"'data_num'은 1 이상 정수만 허용됩니다.\n잘못된 정보를 수정합니다...\ndata_num={int(data_num) if int(data_num) >= 1 else None}"
            error["data_num"] = error_msg
            data_num = int(data_num) if int(data_num) >= 1 else None
        # results_type
        if results_type not in ('dict', 'json'):
            error_msg = f"'results_type'은 'dict' 또는 'json'만 가능합니다.\n잘못된 정보를 수정합니다...\nresults_type='dict'"
            error["results_type"] = error_msg
            results_type='dict'

        return items, data_num, results_type, error

    


if __name__ == "__main__":
    from pprint import pprint

    scrap = NaverDict("토끼")