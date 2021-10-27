from bs4 import BeautifulSoup

def parse_page(page):
    object = {}
    object_list = []

    soap = BeautifulSoup(page, 'html.parser')
    item_list = soap.find('div', {'class' : 'items-items-kAJAg'})
    items = item_list.find_all('div', {'data-marker' : 'item'})
    for item in items:
        object['id'] = item.get('data-item-id')
        object['description'] = item.find('meta', {'itemprop' : 'description'}).get('content')
        object['link'] = item.find('div', {'class' : 'iva-item-titleStep-_CxvN'}).find('a').get('href')
        priceStep = item.find('div', {'class' : 'iva-item-priceStep-QN8Kl'})
        object['priceCurrency'] = priceStep.find('meta', {'itemprop' : 'priceCurrency'}).get('content')
        object['price'] = priceStep.find('meta', {'itemprop' : 'price'}).get('content')
        object_list.append(object)
    return object_list
        
