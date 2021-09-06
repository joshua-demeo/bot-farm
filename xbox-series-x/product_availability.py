import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# Local imports
from urls import gamestop, bestbuy, amazon


def product_checker(url: str, retailer: str):
    '''
    Requests will be made to a specific product page. The contents parsed
    are checked for identifying information that tells whether the product
    is available.
    '''
    
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0'

    # Make request
    # NOTE: Request does not work for bestbuy
    if retailer == 'bestbuy':
        response = requests.get(url, headers={'User-Agent': user_agent})
        webpage = response.text
    else:
        request = Request(url, headers={'User-Agent': user_agent})
        webpage = urlopen(request).read()

    # Get contents of webpage
    contents = soup(webpage, "html.parser")
    print('Fetched Webpage Contents')

    # What are we searching for
    # NOTE: identifier is some text that indicates the product is NOT available
    if retailer == 'gamestop':
        element_type = 'button'
        attributes = {'id': 'add-to-cart'}
        identifier = 'Not Available'
    if retailer == 'bestbuy':
        element_type = 'button'
        attributes = {'data-button-state': 'COMING_SOON'}
        identifier = 'Coming Soon'
    if retailer == 'amazon':
        element_type = 'div'
        attributes = {'id': 'availability'}
        identifier = "We don't know when or if this item will be back in stock"

    # Get exact element
    element = contents.find(element_type, attrs=attributes)
    # Coerce dtype: bs4.element.Tag -> str
    str_element = str(element)
    # print(str_element)
    product_available = identifier not in str_element

    if product_available:
        print(f'Product is available at {retailer}')
    else:
        print(f'Product is NOT available at {retailer}')


def main():
    product_checker(gamestop, 'gamestop')
    product_checker(amazon, 'amazon')
    product_checker(bestbuy, 'bestbuy')

if __name__ == "__main__":
    main()
