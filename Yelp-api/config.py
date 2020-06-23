
"""
To get a YELP_API_KEY:
- Go to https://www.yelp.com/fusion
- At the bottom, click on **Get Started**.
- Sign up or log in.
- Type in the required fields (you can enter anything it doesn't really matter), then click **Create New App**.
- Copy the value in the field **API Key**.
"""
YELP_API_KEY = '2UgtWdV0VWaCEJ620PvM7GoWnPTzKJgZ2tWahYQznXb8wcwQ-SN2zv4TQ5rxVb5thkGJRJ249v_739A_aSfGk5sUg-8QGVlXkJD_w31X_yiQCdR8bYESyVhI-E3uXnYx'
"""python search.py
SEARCH_TERM is pretty much the same thing you would type into the Yelp search box.
It can be used in addition OR instead of SEARCH_CATEGORIES.
"""
SEARCH_TERM = "restaurants"


"""
SEARCH_CATERGORIES can be one or more comma separated categories from:
https://www.yelp.ca/developers/documentation/v3/category_list
- Select the appropriate country from the dropdown on the top right
- Use the lowercase value in brackets from that page (eg. "catering" NOT "Caterers")
"""
SEARCH_CATERGORIES = {"category": {'alias':'', 'title': '', "parent_aliases": ['restaurants']}}



"""
SEARCH_LOCATIONS can be in different formats (eg. a postal code, full address, city+state, etc.)
- It searches as radius of 25 miles from the center point of the location.
- Don't worry about partially overlapping locations (eg. Toronto vs. Etobicoke), as duplicate entries are automatically removed.
"""
SEARCH_LOCATIONS = [
    "Palmdale, CA",


    

]

OUTPUT_FILENAME = 'Greater_la_data.csv'
