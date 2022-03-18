# followed this YouTube video to build this file: https://youtu.be/xdq6Gz33khQ

from http import client
from lib2to3.pgen2 import token
import requests
import base64
import datetime
from urllib.parse import urlencode
from decouple import config

client_id = config("SPOTIFY_ID")
client_secret = config("SPOTIFY_SECRET")

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
    
spotify = SpotifyAPI(client_id, client_secret) # set a SpotifyAPI class Object

spotify.perform_auth()

access_token = spotify.access_token

# spotify.search 
headers = {
  "Authorization": f"Bearer {access_token}"
}

endpoint = 'https://api.spotify.com/v1/search'
# data = urlencode({"q": "Time", "type": "track",})
# print(data)
# lookup_url = f"{endpoint}?{data}"
# r = requests.get(lookup_url, headers=headers)
# print(r.json())
# print(r.status_code)

data = urlencode({"q": "A Lannister always pays his debts", "type": "track",})
print(data)
lookup_url = f"{endpoint}?{data}"
r = requests.get(lookup_url, headers=headers)
# print(r.json())
print(r.status_code)