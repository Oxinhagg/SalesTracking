from bs4 import BeautifulSoup

def parse_page(page):
    ad = {}

    soap = BeautifulSoup(page, 'html.parser')
    item_list = soap.find('div', {'class' : 'items-items-kAJAg'})
    items = item_list.find_all('div', {'data-marker' : 'item'})
    for item in items:
        ad['id'] = item.get('data-item-id')
        ad['description'] = item.find('meta', {'itemprop' : 'description'}).get('content')
        ad['link'] = item.find('div', {'class' : 'iva-item-titleStep-_CxvN'}).find('a').get('href')
        priceStep = item.find('div', {'class' : 'iva-item-priceStep-QN8Kl'})
        ad['priceCurrency'] = priceStep.find('meta', {'itemprop' : 'priceCurrency'}).get('content')
        ad['price'] = priceStep.find('meta', {'itemprop' : 'price'}).get('content')
    return ad
        
