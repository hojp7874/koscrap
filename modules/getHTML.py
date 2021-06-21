import requests

def getHTML(url):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.content
    return html

if __name__ == "__main__":
    search_text = '사과'
    html = getHTML(f'https://www.coupang.com/np/search?q={search_text}&channel=user')
    print(html)