from .models import Venue
from .models import Artist
from .models import Show
import requests
from django.http import HttpResponse
from django.db import IntegrityError

def get_data(requests):
        try:
                artist_list()
                venue_list()
                get_shows()
                return HttpResponse('ok')
                # gettign artist, venues and shows and providing an httpresponse if successful
        except Exception as e:
                print(e)
                return HttpResponse('failed')
                
        
def artist_list():
    
    url = 'https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&stateCode=MN&apikey=SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ'
    
    artists = Artist.objects.all().order_by('name')
    artist_names = []
    for artist in artists:
            artist_names.append(artist.name)
    try:
        data = requests.get(url).json()
        events = data['_embedded']['events']
        for event in events:
            artist_name = (event['name'])
            if artist_name not in artist_names:
                new_artist = Artist(name = artist_name)
                new_artist.save()
                print('artist '+ artist_name + ' added')
        ## calling api for events and finding artists
        ## saving name and creating new Artist Object if not already created
            else:
                print('duplicate artist')
    except Exception as e:
        print(e)
        
def venue_list():
    
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
            

        ## calling api for venues and finding venue
        ## saving name, cityand state and creating new Venue Object

    except IntegrityError as e: 
        print('duplicate entry added')
        print(e)


def get_shows():

        url = 'https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&stateCode=MN&apikey=SJJrApYrXbEOEkWUk32lxQ3p9FMSLydJ'
        venues = Venue.objects.all().order_by('name')
        
        try:
            data = requests.get(url).json()
            events = data['_embedded']['events']
        
            for event in events:
                    artist_name = event['name']
                    venue_name = event['_embedded']['venues'][0]['name']
                    date = event['dates']['start']['dateTime']
                    
                    venues = Venue.objects.filter(name=venue_name)
                    artists = Artist.objects.filter(name=artist_name)

                    if(len(venues) > 0 and len(artists) > 0):
                        matching_venue = venues[0]
                        matching_artist = artists[0]
                        new_show = Show(show_date = date, artist = matching_artist, venue = matching_venue)
                        
                        new_show.save()
                    else:
                        print('no shows for artists/venues currently')
                    
        except Exception as e: 
                print('Error fetching shows')
                print(e)

if __name__ == "__main__":
    get_data(requests)

