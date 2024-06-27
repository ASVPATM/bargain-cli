import urllib
import urllib.request
import webbrowser
import sys
from bs4 import BeautifulSoup
import requests
sys.path.append('/home/asvplen/cli/city_wordlist')
sys.path.append('/home/asvplen/cli/websites')
# import ultimate
from configs import config
from city_wordlist import cities
# from websites import ultimate
# from city_wordlist import cities
base_url = "https://craigslist.org"

location = ''
def fetchPage(query):
    
    location = config.actual_city
    
    if config.max_price != 0 and config.min_price != 0:
        url = f"https://{location}.craigslist.org/search/sss?max_price={config.max_price}&min_price={config.min_price}&query={config.query}"
        print(url)
        response = requests.get(url)
    else:
        url = f"https://{location}.craigslist.org/search/sss?query={config.query}"
        print(url)
        response = requests.get(url)

    print(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    listing = soup.find('li', class_='cl-static-search-result')
    title = listing.find('div', class_='title').text
    href = listing.find('a')['href']
    price = listing.find('div', class_='price').text
    location = listing.find('div', class_='location').text.strip()

    print("Title: {}".format(title))
    print("URL: {}".format(href))
    print("Price: {}".format(price))
    print("Location: {}".format(location))

    


def getEverything(city_full_name, transport_method, query):
        if transport_method == 2:
            return None
        cities.shorten_city_name(city_full_name)
        print(transport_method)
        fetchPage(query)

def main():
    #config.init()
    #print(config.city_full_name)
    #print(cities.shorten_city_name(config.city_full_name))
    #print(config.query)

    fetchPage(config.query)
    
    #response = requests.get()
    
    # base_url = "https://craigslist.org"
    # specific_url = "https://*.craigslist.org/search/sss?query=*"
    # website = ""
    # response = ""

    # # user input on nearest city 
    # inp = input("What is your city? (Choose the largest city near you). Press Y or N \n")
    # if inp.lower() == 'y':
    #     response = 'y'
    #     website = webbrowser.open("https://portland.craigslist.org/search/sss?query=laptop#search=1~gallery~0~0")
    
    # if response == 'y':
    #     website = webbrowser.open("https://portland.craigslist.org/search/sss?query=laptop#search=1~gallery~0~0")
    # #response = urllib.request.urlopen("https://portland.craigslist.org/search/sss?query=laptop#search=1~gallery~0~0")

    # #html_data = website.read().decode('utf-8')
    # #print(html_data)
    # #print(inp.strip().lower())
    # print("Running craigslist script")


    #
    

    


if __name__ == "__main__":
    main()