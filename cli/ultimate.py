from Cities import cities_retriever
from itertools import count
from unidecode import unidecode
import sys
#import craigslist
import difflib
from configs import config
from bs4 import BeautifulSoup

sys.path.append('cli/city_wordlist')
sys.path.append('cli/websites')
from websites import craigslist, offerup, facebook_marketplace, ebay, temu, ali_express
from city_wordlist import cities

# from pkg_resources import resource_string
# import json

# cities_data = resource_string('world_cities', 'data/world-cities_json.json').decode('utf-8')
# cities = json.loads(cities_data)

# print(cities[0])

#actual_city_answer = 0
# city_number = 0
# city_full_name = ''
# indexes = []
# actual_city = ''

#ASK IF THEY WANT LOCAL, SHIPPING OR BOTH
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
            max_min_answer = str(input("\nDo You Want To Set a Maximum/Minimum Price?\n (PRESS Y OR N): ")).lower()
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
            pass

def city():
    
    #actual_city = ''
    #COLLECTS THE CITY FROM USER, PUTS CLOSEST MATCHES INTO ARRAY
    if config.transport_method == 1 or config.transport_method == 3:
        
        while True:
            try:
                nearest_city_answer = str(input("\nName the closest/largest city to you: ")).lower()
                city_close_matches = difflib.get_close_matches(nearest_city_answer, cities.cities_list)

                if len(city_close_matches) != 0:
                    number = 1
                    for x in range(0, len(cities.cities_list)):
                        if unidecode(cities.cities_list[x]).lower() == nearest_city_answer:
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

    #print(config.actual_city)
    #global city_full_name
    #CITY FULL NAME
    print(config.city_number)

    #print(cities.cities_full_list[indexes[actual_city_answer]])
    
    if config.transport_method != 1:
        config.city_full_name = cities.cities_full_list[config.indexes[config.city_number-1]]
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
            query_input = str(input("What would you like to look for today?: "))
            config.query = query_input
            break

        except ValueError:
            print("Invalid Query")


def search_until_stop():
    pass
    


#MAIN CODE HERE
def main():
    config.init()
    setting_price()
    transport()
    city()
    handle_query()
    move_Over()
    print(config.actual_city, config.city_number, config.max_price, config.min_price, config.indexes)
    craigslist.main()
    
   

   
if __name__ == "__main__":
    main()
    
    
   





#def  

    






