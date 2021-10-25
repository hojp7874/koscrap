from urllib.parse import quote
from modules.get_soup import get_soup


class Product:
    """쿠팡에서 검색한 상품의 정보가 담겨있는 클래스입니다."""

    def __init__(self, image, name, price, star, url):
        self._image     = image
        self._name      = name
        self._price     = price
        self._star      = star
        self._url       = url
    
    def get_contents(self):
        """상품 정보를 반환합니다."""

        contents = {}
        contents['image']   = self._image
        contents['name']    = self._name
        contents['price']   = self._price
        contents['star']    = self._star
        contents['url']     = self._url

        return contents

    def get_image(self):
        """이미지 정보를 반환합니다."""
        return self._image
    
    def get_name(self):
        """이름 정보를 반환합니다."""
        return self._name
    
    def get_price(self):
        """가격 정보를 반환합니다."""
        return self._price
    
    def get_star(self):
        """별점 정보를 반환합니다."""
        return self._star
    
    def get_url(self):
        """URL 정보를 반환합니다."""
        return self._url


class Coupang:
    """쿠팡에서 상품 정보를 검색합니다."""

    def __init__(self):
        self._search_text   = None
        self._products      = []
    
    def __str__(self):
        """검색어 정보를 반환합니다."""

        return f"'{self._search_text}'에 대한 쿠팡 검색 결과입니다." if self._products else "검색결과가 없습니다."
        
    def search(self, search_text: str):
        """쿠팡에서 'search_text'를 검색하여 그 결과를 저장합니다."""

        self._search_text   = search_text
        self._products      = []

        encode_text = quote(self._search_text)
        url         = f'https://www.coupang.com/np/search?q={encode_text}'
        soup        = get_soup(url)
        ul          = soup.find("ul", {"id":"productList"})
        if ul == None:
            result = f"'{self._search_text}'에 대한 검색결과가 없습니다."
            print(result)
            
            return result

        products    = ul.findAll("a", {"class":"search-product-link"})
        for idx, product in enumerate(products):
            url         = 'https://www.coupang.com/' + product.get("href")
            image       = product.find("img").get("src") if idx < 8 else None
            name        = product.select_one(".name").get_text()
            price       = product.select_one(".price-value").get_text()
            star        = product.select_one(".rating").get_text() if product.select_one(".rating") != None\
                                                                   else None
            self._products.append(Product(image, name, price, star, url))
    
    def get_images(self):
        """검색 결과로 나온 이미지들을 리스트 형태로 반환합니다."""

        img_list = list(filter(lambda x: x, map(lambda x: x._image, self._products)))

        return img_list

    def get_product(self, idx, option=None):
        f"""'{idx}'번째 상품에 대한 정보를 가져옵니다."""

        product = self._products[idx]
        if option == None:
            return product.get_contents()
        elif option == 'image':
            return product.get_image()
        elif option == 'name':
            return product.get_name()
        elif option == 'price':
            return product.get_price()
        elif option == 'star':
            return product.get_star()
        elif option == 'url':
            return product.get_url()
        else:
            result = f"'option' 형식이 잘못되었습니다."
            return result


if __name__ == "__main__":
    coupang = Coupang()
    coupang.search('나비')
    print('@@@')
    print(coupang)
    # print(coupang.get_images())
    print(coupang.get_product(0))
    print(coupang.get_product(0, 'imag'))