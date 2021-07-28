import requests
from bs4 import BeautifulSoup

def getHTML(url):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.content
    html_encode = BeautifulSoup(html, "html.parser")
    return html_encode

if __name__ == "__main__":
    search_text = '사과'
    html = getHTML(f'https://www.coupang.com/np/search?q={search_text}&channel=user')
    print(html)