from Avito.request import get_html
from Avito.config import get_url_list
from Avito.parse import parse_page

def main():
    url_list = get_url_list()
    for url in url_list:
        page = get_html(url)
        obj_list = parse_page(page)
    print(obj_list)

if __name__ == '__main__':
    main()