from bs4 import BeautifulSoup
from urllib.parse import quote
from .modules.getHTML import getHTML


def coupang(search_text, options=["image", "name", "price", "star", "url"]):
    search_text = quote(search_text)
    url = f'https://www.coupang.com/np/search?q={search_text}&channel=user'
    html = getHTML(url)
    bsObj = BeautifulSoup(html, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    items = ul.findAll("li", {"class":"search-product"})[:8]
    results = {}
    for idx, item in enumerate(items):
        result = {}
        for option in options:
            if option == "image":
                data = item.find("dt", {"class":"image"})
                data = data.find("img").get("src")

            elif option == "name":
                data = item.find("div", {"class":"name"}).get_text()
                
            elif option == "price":
                data = item.find("em", {"class":"sale"})
                data = data.find("strong", {"class":"price-value"}).get_text()

            elif option == "star":
                data = item.find("span", {"class":"star"})
                data = data.find("em", {"class":"rating"}).get_text()

            elif option == "url":
                data = item.find("a").get("href")

            else:
                error = f"'{data}'는 잘못된 옵션입니다."
                return error

            result[option] = data
        results[idx+1] = result

    return results



if __name__ == "__main__":
    from pprint import pprint

    
    crawling = coupang("사과")
    pprint(crawling)