import urllib
import urllib.request
import webbrowser
import sys
from bs4 import BeautifulSoup
import requests
sys.path.append('cli/city_wordlist')
sys.path.append('cli/websites')
sys.path.append('cli/configs')
# import ultimate
from configs import config
from city_wordlist import cities
import ultimate
from colorama import Fore, Back, Style
# from websites import ultimate
# from city_wordlist import cities
base_url = "https://craigslist.org"


location = ''


def fetchPage(query, search_index_bottom, search_index_top):
    
    temp_array = []
    location = config.actual_city
    
    if config.max_price != 0 and config.min_price != 0:
        url = f"https://{location}.craigslist.org/search/sss?max_price={config.max_price}&min_price={config.min_price}&query={config.query}#search=1~gallery~{config.page_number}~0"
        #print(url)
        response = requests.get(url)
    else:
        url = f"https://{location}.craigslist.org/search/sss?query={config.query}#search=1~gallery~{config.page_number}~0"
        #print(url)
        response = requests.get(url)

    
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    listings = soup.findAll('li', class_='cl-static-search-result')
    
    
    if len(listings) > 1:
        for x in range(search_index_bottom, search_index_top):
            print("\n")
            listing = listings[x]
            title = listing.find('div', class_='title').text
            href = listing.find('a')['href']
            price = listing.find('div', class_='price').text
            location = listing.find('div', class_='location').text.strip()

            new_listing = [
                {
                    'index': x,
                    'title': title,
                    'href': href,
                    'price': price,
                    'location': location

                }
            ]
            config.json_listings.append(new_listing)
            ultimate.write_data(ultimate.file_json, config.json_listings)

            #print(new_listing)
            config.craigslist_array.append(new_listing)

            print("Index: {}".format(x))
            print("Title: {}".format(title))
            print("URL: {}".format(href))
            print("Price: {}".format(price))
            print("Location: {}".format(location))
    elif len(listings) == 1:
        print("\n")
        print("Index: {}".format(x))
        listing = listings[0]
        title = listing.find('div', class_='title').text
        href = listing.find('a')['href']
        price = listing.find('div', class_='price').text
        location = listing.find('div', class_='location').text.strip()
        print("Title: {}".format(title))
        print("URL: {}".format(href))
        print("Price: {}".format(price))
        print("Location: {}".format(location))
        config.looking_answer = 'n'
    else:
        print("\nNo Results")
        

    
def keepSearching():
     pass



def main():
    pass
    
    

def commentedOutCode():
    pass
    #print(Fore.RED + " some text")
    #config.init()
    #print(config.city_full_name)
    #print(cities.shorten_city_name(config.city_full_name))
    #print(config.query)

    # while config.looking_answer == 'y':
    #     fetchPage(config.query, config.keep_looking_bottom, config.keep_looking_top)
    #     ultimate.search_until_stop()
    #     config.keep_looking_bottom+=3
    #     config.keep_looking_top+=3
    
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
    # def getEverything(city_full_name, transport_method, query):
#         if transport_method == 2:
#             return None
#         cities.shorten_city_name(city_full_name)
#         print(transport_method)
#         fetchPage(query)
    # handle change of query and possibly change of location 
        # while True:
        #     try:
        #         switch_or_stop_input = str(input("\nNO RESULTS. \n\nWould you like to switch your query or" +
        #       " stop searching? (Write SWITCH or NO)")).lower()
        #         if switch_or_stop_input == 'switch':
        #             config.looking_answer = 'switch'
        #             while True:
        #                 try:
        #                     switch_query_input = str(input("\nWhat would you like"
        #                                         +" to switch your query to?"))
        #                     config.switched_query = switch_query_input
        #                     break
        #                 except ValueError:
        #                     print("Invalid Query")
        #             continue
        #         elif switch_or_stop_input == 'no':
        #             config.looking_answer = 'n'
        #             #fetchPage()
        #             break
        #     except ValueError:
        #         print("Please select between SWITCH OR NO")

        

        



    # print(url)
    # html = response.content
    # soup = BeautifulSoup(html, 'html.parser')
    # listing = soup.find('li', class_='cl-static-search-result')
    # title = listing.find('div', class_='title').text
    # href = listing.find('a')['href']
    # price = listing.find('div', class_='price').text
    # location = listing.find('div', class_='location').text.strip()

    # print("Title: {}".format(title))
    # print("URL: {}".format(href))
    # print("Price: {}".format(price))
    # print("Location: {}".format(location))
    #print(len(listings))
    
    
    # for x in range(min(search_index, len(listings))):
    #     print("\n")
    #     listing = listings[x]
    #     title = listing.find('div', class_='title').text
    #     href = listing.find('a')['href']
    #     price = listing.find('div', class_='price').text
    #     location = listing.find('div', class_='location').text.strip()

    #     print("Title: {}".format(title))
    #     print("URL: {}".format(href))
    #     print("Price: {}".format(price))
    #     print("Location: {}".format(location))


    


if __name__ == "__main__":
    main()

