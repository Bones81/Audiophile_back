# followed this YouTube video to build this file: https://youtu.be/xdq6Gz33khQ

from http import client
from lib2to3.pgen2 import token
import requests
import base64
import datetime
from urllib.parse import urlencode

client_id = 'a99dfe235c814dcda823e58b44a28596'
client_secret = '55495c730dda4c95991bca5dcd6a8247'

class SpotifyAPI(object):
  access_token = None
  access_token_expires = datetime.datetime.now()
  access_token_did_expire = True
  client_id = None
  client_secret = None
  token_url = 'https://accounts.spotify.com/api/token'

  def __init__(self, client_id, client_secret, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.client_id = client_id
    self.client_secret = client_secret

  def get_client_credentials(self):
    """
    Returns a base64 encoded string (not bytes)
    """
    client_id = self.client_id
    client_secret = self.client_secret
    if client_secret == None or client_id == None:
      raise Exception("You must set client_id and client_secret")
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode()) # more secure way to pass credentials, turns into base64 encoded bytes rather than string

    # client_creds.encode() # turns client_creds from str into bytes
    # base64.b64decode(client_creds_b64) would decode b64 str back into a byte str with original client_creds value -- this comment just here for reference. We aren't using this here. Spotify backend probably uses a line like this though
    return client_creds_b64.decode()

  def get_token_headers(self):
    client_creds_b64 = self.get_client_credentials()
    return {
      "Authorization": f"Basic {client_creds_b64}", # <base64 encoded client_id:client_secret> base64 encoded str
    }

  def get_token_data(self):
    return {
      "grant_type": "client_credentials",
    }
  
  def perform_auth(self):
    token_url = self.token_url
    token_data = self.get_token_data()
    token_headers = self.get_token_headers()
    r = requests.post(token_url, data=token_data, headers=token_headers)
    if r.status_code not in range(200, 299): 
      raise Exception("Could not authenticate client")
      return False
    data = r.json()
    now = datetime.datetime.now()
    access_token = data['access_token']
    expires_in = data['expires_in'] # seconds
    expires = now + datetime.timedelta(seconds=expires_in)
    self.access_token = access_token
    self.access_token_expires = expires
    self.access_token_did_expire = expires < now
    return True

  def get_access_token(self):
    token = self.access_token
    expires = self.access_token_expires
    now = datetime.datetime.now()
    if expires < now:
      self.perform_auth()
      return self.get_access_token()
    elif token == None:
      self.perform_auth()
      return self.get_access_token()
    return token
  
  def get_resource_header(self):
    access_token = self.get_access_token()
    headers = {
      "Authorization": f"Bearer {access_token}"
    }
    return headers

  def search(self, query, search_type='artist'): # type is built-in python operator
    # spotify.search
    headers = self.get_resource_header()
    endpoint = 'https://api.spotify.com/v1/search'
    # data = urlencode({"q": "Time", "type": "track",})
    # print(data)
    # lookup_url = f"{endpoint}?{data}"
    # r = requests.get(lookup_url, headers=headers)
    # print(r.json())
    # print(r.status_code)

    data = urlencode({"q": query, "type": search_type.lower(),})
    lookup_url = f"{endpoint}?{data}"
    r = requests.get(lookup_url, headers=headers)
    # print(r.json())
    print(r.status_code)
    if r.status_code not in range(200, 299):
      return {}
    return r.json()

  def get_resource(self, lookup_id, resource_type='albums', version='v1'):
    endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
    headers = self.get_resource_header()
    r = requests.get(endpoint, headers=headers)
    if r.status_code not in range(200, 299):
      return {}
    return r.json()

  def get_album(self, _id ):
    return self.get_resource(_id, resource_type='albums')

  def get_artist(self, _id):
    return self.get_resource(_id, resource_type='artists')
    
spotify = SpotifyAPI(client_id, client_secret) # set a SpotifyAPI class Object

# print(spotify.search('Come Together', 'track'))
api_response_for_beatles = spotify.get_artist('3WrFJ7ztbogyGnTHbHJFl2')
# print(api_response_for_beatles['genres'])

coldplay_artist_search_response = spotify.search('Coldplay','artist')
# print(coldplay_artist_search_response['artists']['items'][0]['name'])

album_search_response = spotify.search('Goodbye Yellow Brick Road','album')
print(album_search_response['albums']['items'][0]['artists'][0]['name'])
