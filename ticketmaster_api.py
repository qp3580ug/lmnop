

import requests


def artist_list():
    
    ticketmasterKey = "SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ"
    url = 'https://app.ticketmaster.com/discovery/v2/attractions.json?classificationName=music&stateCode=MN&apikey=SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ'
    
   

    
    keyword = "concert"
    location = "minneapolis"
    
    try:
        data = requests.get(url).json()
        events = data['_embedded']['attractions']
        for event in events:
            artist_name = (event['name'])
            print(artist_name)




    except Exception as e:
        print("No venues found")
def venue_list():
    ticketmasterKey = "SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ"
    url = 'https://app.ticketmaster.com/discovery/v2/venues.json?stateCode=MN&apikey=SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ'

    try:
        data = requests.get(url).json()
        venues = data['_embedded']['venues']
        for venue in venues:
            venue_name = venue['name']
            venue_city = venue['city']['name']
            venue_state = venue['state']['name']
            print (venue_name)
            print(venue_city)
    
    except Exception as e:
        print("No venues found")

if __name__ == "__main__":
    venue_list()
    artist_list()

