from .models import Venue
from .models import Artist
import requests
from django.http import HttpResponse
from django.db import IntegrityError

def get_data(requests):
        try:
                artist_list()
                venue_list()
                return HttpResponse('ok')
        except Exception as e:
                return HttpResponse('failed')
        
def artist_list():
    
    ticketmasterKey = "SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ"
    url = 'https://app.ticketmaster.com/discovery/v2/attractions.json?classificationName=music&stateCode=MN&apikey=SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ'

    
    try:
        data = requests.get(url).json()
        events = data['_embedded']['attractions']
        for event in events:
            artist_name = (event['name'])
            new_artist = Artist(name = artist_name)
            new_artist.save()
            print(artist_name)
        ## calling api for events and finding artists
        ## saving name and creating new Artist Object

    except Exception as e:
        print(e)
        
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
            new_venue = Venue(name = venue_name, city = venue_city, state = venue_state)
            new_venue.save()
            print (venue_name)
            print(venue_city)

        ## calling api for venues and finding venue
        ## saving name, cityand state and creating new Venue Object

    except IntegrityError as e: 
        print('duplicate entry added')
        print(e)

if __name__ == "__main__":
    get_data(requests)

