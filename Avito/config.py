import configparser

def get_url_list():
    url_list = []
    
    config = configparser.ConfigParser()
    config.read('settings.ini')
    for str in config['FAVORITE_URL']:
        url_list.append(config['FAVORITE_URL'][str]) 
    return url_list
