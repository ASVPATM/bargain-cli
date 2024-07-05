from Cities import cities_retriever
from itertools import count
from unidecode import unidecode
import sys
#import craigslist
import webbrowser
import difflib
import json
import os
from configs import config
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

sys.path.append('cli/city_wordlist')
sys.path.append('cli/websites')
from websites import craigslist, offerup, facebook_marketplace, ebay, temu, ali_express
from city_wordlist import cities

file_json = 'listings_data.json'

#JSON METHODS TO STORE
def load_json(file_json):
    if os.path.exists(file_json):
        with open(file_json, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def write_data(file_json, data):
     with open(file_json, 'w') as file:
        json.dump(data, file, indent=4)

config.json_listings = load_json(file_json)


def transport():
    #global transport_method
    while True:
        try:
            print("\nSelect\n1) Local\n2) Shipping\n3) Both")
            print("\n(IF YOU CHOOSE SHIPPING ONLY, CRAIGSLIST IS EXCLUDED)\n(IF YOU CHOOSE LOCAL ONLY, CRAIGSLIST, FACEBOOK MARKETPLACE, AND OFFERUP WILL BE AVAILABLE)")
            transport_method_answer = int(input("CHOOSE AN ANSWER: "))
            if transport_method_answer >= 1 and transport_method_answer <= 3:
                config.transport_method = transport_method_answer
                break
            else:
                print("Make sure to enter valid values from 1 --> 3")
        except ValueError:
            print("Enter Integer Values Only")
    

# ASK THE USER IF THEY WANT TO SET A MAXIMUM/MINIMUM PRICE
def setting_price():
    
    # global min_price
    # global max_price
    answer = ''
    attempts = 3
    while True:
        try:
            max_min_answer = str(input("\nDo You Want To Set a Maximum/Minimum Price?\n (PRESS Y OR N): ")).lower().strip()
            if max_min_answer == 'y' or max_min_answer == 'n':
                answer = max_min_answer
                break
            else:
                print("Invalid Number, Please Select between 1 or 2")
                print(str(attempts) + " Attempts Left")
                attempts-=1
                if attempts <= 0:
                    break
        except ValueError:
            print("Invalid Input, Please Enter a Number") 
    

    #IF THEY WANT TO SET A MAXIMUM/MINIMUM PRICE
    while True:
        if answer == 'y':
            try:
                min_price_answer = int(input("Min: "))
                max_price_answer = int(input("\nMax: "))
                if min_price_answer >= 0 and min_price_answer <= max_price_answer:
                    config.min_price = min_price_answer
                    config.max_price = max_price_answer
                    break
                else:
                    print("Make sure to enter valid values for the maximum/minimum. The minimum should be > 0 and <= maximum")
            except ValueError:
                print("Enter Integer Values Only")
        else:
            break

def city():
    
    #actual_city = ''
    #COLLECTS THE CITY FROM USER, PUTS CLOSEST MATCHES INTO ARRAY
    if config.transport_method == 1 or config.transport_method == 3:
        
        while True:
            try:
                nearest_city_answer = str(input("\nName the closest/largest city to you: ")).lower().strip()
                city_close_matches = difflib.get_close_matches(nearest_city_answer, cities.cities_list)

                if len(city_close_matches) != 0:
                    number = 1
                    for x in range(0, len(cities.cities_list)):
                        if unidecode(cities.cities_list[x]).lower().strip() == nearest_city_answer:
                            print (str(number) + ") " + cities.cities_full_list[x])
                            config.indexes.append(x)
                            number+=1
                    if number != 1:
                        break
                    else:
                        print("Not a Valid City")  
                
            except ValueError:
                print("WRONG")
    
    
    #print(len(city_close_matches))
    # ASKS FOR FURTHER CLARIFICATION FROM USER
        
        while True:
            try: 
                
                actual_city_answer = int(input("\nSelect a number based on your actual city: "))
                config.city_number = actual_city_answer
                if actual_city_answer >= 1 and actual_city_answer <= len(city_close_matches):
                    # for char in city_close_matches[actual_city_answer-1]:
                    #     if char != ',':
                    #         actual_city+=char
                    config.actual_city = cities.cities_list[config.indexes[config.city_number-1]]
                    break
                else:
                    print("Please select a value within the range shown")
            except ValueError:
                print("Enter Integer Values Only")
    else:
        config.city_number = 0

def move_Over():
    #CITY NAME
    pass

    #print(config.actual_city)
    #global city_full_name
    #CITY FULL NAME
    #print(config.city_number)

    #print(cities.cities_full_list[indexes[actual_city_answer]])
    
    # if config.transport_method != 1:
    #     config.city_full_name = cities.cities_full_list[config.indexes[config.city_number-1]]
    #print(city_full_name)


    #TRANSPORTATION METHODprint(transport_method)


    #IF THEY SELECT BOTH TRANSPORT METHODS
    # if transport_method == 3:
    #     craigslist.getEverything(city_full_name, transport_method, query)
    #     offerup.getEverything(city_full_name, transport_method, query)
    #     temu.getEverything(city_full_name, transport_method, query)
    #     facebook_marketplace.getEverything(city_full_name, transport_method, query)
    #     ebay.getEverything(city_full_name, transport_method, query)
    #     ali_express.getEverything(city_full_name, transport_method, query)
    
    # #IF THEY SELECT ONLY SHIPPING
    # elif transport_method == 2:
    #     offerup.getEverything(city_full_name, transport_method, query)
    #     temu.getEverything(city_full_name, transport_method, query)
    #     facebook_marketplace.getEverything(city_full_name, transport_method, query)
    #     ebay.getEverything(city_full_name, transport_method, query)
    #     ali_express.getEverything(city_full_name, transport_method, query)

    # #IF THEY SELECT ONLY LOCAL
    # else:
    #     craigslist.getEverything(city_full_name, transport_method, query)
    #     offerup.getEverything(city_full_name, transport_method, query)
    #     facebook_marketplace.getEverything(city_full_name, transport_method, query)

def handle_query():
    #global query
    while True:
        try:
            query_input = str(input("\nWhat would you like to look for today?: ")).strip()
            config.query = query_input
            break

        except ValueError:
            print("Invalid Query")


    

    
def all_together():
    first_time = 0

    while config.continue_search:
        try:
            if first_time == 0:
                craigslist.fetchPage(config.query, config.keep_looking_bottom, config.keep_looking_top)
                config.keep_looking_bottom+=3
                config.keep_looking_top+=3
                searching_input = int(input("\nPress: \n1) Keep Searching\n2) "
                                            +"Change Query\n3) Open in Browser\n4) Stop Searching"
                                            +"\nAnswer Here: "))    
            else:
                searching_input = int(input("\n1)Continue  2)Switch  3)Open Browser  4)Stop: "))

            if searching_input == 1:
                craigslist.fetchPage(config.query, config.keep_looking_bottom, config.keep_looking_top)
                config.keep_looking_bottom+=3
                config.keep_looking_top+=3
            elif searching_input == 2:
                keepLooking()
            elif searching_input == 3:
                # while True:
                #     try:
                #         open_in_browser_input = str(input("Would you like to open this in browser (Press Y or N): ")).lower().split()
                #         if open_in_browser_input == 'y' or open_in_browser_input == 'n':
                #             config.open_browser = open_in_browser_input
                #             break
                #     except ValueError:
                #         print("Not working")
                # if config.open_browser == 'y':
                    while True:
                                try:
                                    browser_index_input = int(input("Select the index of the listing you "
                                                                    + "you would like to open in your browser: "))
                                    webbrowser.open(get_href_by_index(browser_index_input))
                                    break
                                except ValueError:
                                    print("Still working")
                # else:
                #     config.continue_search = False
            elif searching_input == 4:
                config.continue_search = False
            first_time +=1
        except ValueError:
            print("Please enter a correct corresponding value!")
   

def keepLooking():
    while True:
        try:
            second_time = 0
            if second_time == 0:
                switched_query_input = str(input("What would you like to switch to?: ")).lower()
            else:
                switched_query_input == str(input("Try Again: "))
            confirm_input = str(input("\nAre you sure? (Press Y or N): ")).lower()
            not_confirmed = True
            if confirm_input == 'y':
                switched_query_input = config.query
                break
        except ValueError:
            print("Please enter valid values")
                                
        config.query = config.switched_query
        config.keep_looking_bottom = 0
        config.keep_looking_top = 3
        config.looking_answer = 'y'

def get_href_by_index(index):
    for listing_group in config.json_listings:
        for listing in listing_group:
            if listing['index'] == index:
                return listing['href']
    return None





def switch():
    pass
    
def specific_marketplaces():
    config.init()
    

def all_marketplaces():
    config.init()
    setting_price()
    transport()
    city()
    handle_query()
    move_Over()
    # print(Fore.BLACK)
    # print(Back.RED)
    # print(Style.DIM)
    all_together()


#MAIN CODE HERE
def main():
    pass
    
    

   
def commentedOutCode():
    pass
    # while config.looking_answer == 'y':
    #     if config.transport_method == 1:
    #         craigslist.fetchPage(config.query, config.keep_looking_bottom, config.keep_looking_top)
    #         search_until_stop()
    #     elif config.transport_method == 2:
    #         offerup
            
    #     config.keep_looking_bottom+=3
    #     config.keep_looking_top+=3
    # if config.looking_answer == 'switch':
    #     craigslist.fetchPage(c)


    # if config.looking_answer == 'n':
    #     while True:
    #         try:
    #             change_query_or_stop_input = str(input("Would you like to: \n1)Change Query\n2)Stop Searching\n\nPlease" 
    #                                                    +"Select an Answer"))
    #         except ValueError:
    #             pass    
     # while config.continue_search:
    #     if config.looking_answer == 'y':
    #         craigslist.fetchPage(config.query, config.keep_looking_bottom, config.keep_looking_top)
    #         config.keep_looking_bottom+=3
    #         config.keep_looking_top+=3
    #     elif config.looking_answer == 'switch':
    #         config.query = config.switched_query
    #         config.keep_looking_bottom = 0
    #         config.keep_looking_top = 3
    #         config.looking_answer = 'y'
    #     elif config.looking_answer == 'n':
    #         config.continue_search = False
        
        # while True:
        #     try:
        #         searching_input = int(input("\nPress: \n1) Keep Searching\n2) "
        #                                     +"Change Query\n3) Stop Searching"
        #                                     +"\nAnswer Here: "))
        #         print(searching_input)
        #         if searching_input == 1:
        #             config.looking_answer = 'y'
        #             break
        #         elif searching_input == 2:
        #             config.looking_answer == 'switch'
        #             break
        #         elif searching_input == 3:
        #             config.looking_answer == 'n'
        #             break
        #     except ValueError:
        #         print("Enter a Correct Value Please")

        # while True:
                #     try:
                #         second_time = 0
                #         if second_time == 0:
                #             switched_query_input = str(input("What would you like to switch to?: ")).lower()
                #         else:
                #             switched_query_input == str(input("Try Again: "))
                #         confirm_input = str(input("\nAre you sure? (Press Y or N): ")).lower()
                #         not_confirmed = True
                #         if confirm_input == 'y':
                #             switched_query_input = config.query
                #             break
                #     except ValueError:
                #         print("Please enter valid values")
                                
                # config.query = config.switched_query
                # config.keep_looking_bottom = 0
                # config.keep_looking_top = 3
                # config.looking_answer = 'y'
        # def search_until_stop():
    #     if config.looking_answer == 'n':
    #         return
    #     if config.looking_answer == 'switch':

    #     keep_searching_input = str(input("To continue searching, press y, otherwise press n")).lower()
    #     while True:
    #         try:
    #             keep_searching_input = str(input("\nTo continue searching, press y, otherwise press n: ")).lower()
    #             if keep_searching_input == 'y' or keep_searching_input == 'n':
    #                 config.looking_answer = keep_searching_input
    #                 break
    #             else:
    #                 print("Please select an answer between Y or N")
    #         except ValueError:
    #             print("Enter Correct Values Only Please") 

    # from pkg_resources import resource_string
    #      import json

    # cities_data = resource_string('world_cities', 'data/world-cities_json.json').decode('utf-8')
    #    cities = json.loads(cities_data)

    # print(cities[0])

    #actual_city_answer = 0
    # city_number = 0
    # city_full_name = ''
    # indexes = []
    # actual_city = ''

    #ASK IF THEY WANT LOCAL, SHIPPING OR BOTH


   
if __name__ == "__main__":
    main()
    
    
   





#def  

    






