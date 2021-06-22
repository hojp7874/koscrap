from bs4 import BeautifulSoup
from urllib.parse import quote
from .modules.getHTML import getHTML
import json


def coupang(search_text, items=["image", "name", "price", "star", "url"], data_num=8, results_type='dict'):
    search_text = quote(search_text)
    url = f'https://www.coupang.com/np/search?q={search_text}&channel=user'
    html = getHTML(url)
    bsObj = BeautifulSoup(html, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    if not 0 < data_num <= 8:
        print(f"{data_num}이(가) ")
    lis = ul.findAll("li", {"class":"search-product"})[:data_num]
    results = {}
    for idx, li in enumerate(lis):
        result = {}
        for item in items:
            if item == "image":
                data = li.find("dt", {"class":"image"})
                data = data.find("img").get("src")

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

            else:
                error = f"'{item}'은(는) 잘못된 옵션입니다. ex) items=['image', 'name', 'price', 'star', 'url']"
                return error

            result[item] = data
        results[idx+1] = result

    if results_type == 'json':
        return json.dumps(results)
    elif results_type == 'dict':
        return results
    else:
        return f"'results_type={results_type}'은(는) 잘못된 타입입니다. ex) results_type='dict' 또는 results_type='json'"


if __name__ == "__main__":
    from pprint import pprint

    crawling = coupang("사과")
    pprint(crawling)