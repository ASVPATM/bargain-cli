#import climage

#IMPORTS
from . import ultimate
from websites import craigslist, ebay, facebook_marketplace, ali_express, temu
import sys
import os



# INTRO MESSAGE (SUBJECT TO CHANGE)
print("Welcome to Bargain Search!\n\n A bargain search engine that utilizes already prexisting"+
" online marketplaces!\n\n Currently we only service\n- OfferUp\n- Craigslist\n- Facebook Marketplace\n- Ebay\n- "+
"Temu\n- Ali Express\n")

# ASK AND PROMPT USER IF THEY WANT TO SEARCH ALL SITES
print("Before We Get Started, Tell Me Where You Would Like to Search")

answer = 0
try:
    search_all_sites_answer = int(input("(SELECT 1 OR 2)\n\n1) All Marketplaces\n2) Specific Site?\n\n"))
    if search_all_sites_answer == 1 or search_all_sites_answer == 2:
        answer = search_all_sites_answer
    else:
        print("Invalid Number, Please Select between 1 or 2")
except ValueError:
    print("Invalid Input, Please Enter a Number")


#IF THEY WANT TO SEARCH ALL SITES
if answer == 1:
    ultimate.main()
elif answer == 2:
    pass
else:
    pass




