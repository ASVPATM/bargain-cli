import sys
sys.path.append('/home/asvplen/cli/city_wordlist')
sys.path.append('/home/asvplen/cli/websites')
import craigslist, offerup, facebook_marketplace, ebay, temu, ali_express, ultimate
import cities


#MAIN CODE HERE
def main():
    pass


def getEverything(city_full_name, transport_method, query):
        if transport_method == 2:
            return None
        cities.shorten_city_name(city_full_name)


if __name__ == "__main__":
    main()