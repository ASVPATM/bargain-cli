import sys
sys.path.append('cli/city_wordlist')
sys.path.append('cli/websites')
from websites import craigslist, offerup, facebook_marketplace, ebay, temu, ali_express
from city_wordlist import cities


#OFFERUP WILL GET DIFFERENT HTML TAGS DEPENDING ON IF LOCAL OR SHIPPING WAS CHOSEN

#MAIN CODE HERE
def main():
    pass


def getEverything(city_full_name, transport_method, query):
        if transport_method == 2:
            return None
        cities.shorten_city_name(city_full_name)




if __name__ == "__main__":
    main()