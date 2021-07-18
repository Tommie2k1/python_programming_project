import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
cid = '1e2a98860e104b78b7cfc0b26abe9818'
secret = '918cdbdff1b046a3a94feafcb386d13d'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))
def print_here_are(artist):
    print("\nHere are 20 hits from {}:\n".format(artist))
def save_the_list(result_list, artist):
    save_it = input("\nWould you like to save the list of songs to a file? y/n")
    if save_it == "y" or save_it == "Y":
        with open("Track_list.txt", "w+") as save_list:
            save_list.write("See list of 20 {} hits:\n\n".format(artist))
            save_list.write("{}".format(result_list))
    else:
        print("\nNoted.  You do not want to save the list!")
def search_artist():
    artist = input("Choose an artist:")
    results = sp.search(q=artist, limit=20)
    found = False
    result_list = ''
    for idx, track in enumerate(results['tracks']['items'], start=1):
        found = True
    if found == True:
        print_here_are(artist)
        for idx, track in enumerate(results['tracks']['items'], start=1):
            result_list += '{}. {}\n'.format(idx, track['name'])
        print(result_list)
        save_the_list(result_list, artist)
    else:
        print("There is no artist with that name on Spotify, please try again!")
search_artist()
