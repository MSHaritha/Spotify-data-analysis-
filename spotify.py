import requests
import pandas as pd

#Function to get Spotify access token
def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
'grant_type': 'client_credentials',
'client_id': "5460ee03e82d4724984066633f5e1a46",
'client_secret': "d7f0f73c9165484c89f44933ea2461cf",
})
auth_data = auth_response.json()
return auth_data['access_token']

#Function to search for a track and get its ID
def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
url = f"https://api.spotify.com/v1/search?q={query}&type=track"
response = requests.get(url, headers={
'Authorization': f'Bearer {token}'
})
json_data = response.json()
try:
    first_result = json_data['tracks']['items'][0]
track_id = first_result['id']
return track_id
    except (KeyError, IndexError):
return None

#Function to get track details
def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
response = requests.get(url, headers={
'Authorization': f'Bearer {token}'
})
json_data = response.json()
image_url = json_data['album']['images'][0]['url']
return image_url

#Your Spotify API Credentials
client_id = 'dabcc892f1d248e3a69bcf45b2cf7bcf'
client_secret = '589d852e1ab945ebb664794ef1f60414'

#Get Access Token
access_token = get_spotify_token(client_id, client_secret)

#Read your DataFrame (replace 'your_file.csv' with the path to your CSV file)
df_spotify = pd.read_csv('Spotify-dataset.csv', encoding='ISO-8859-1')

#Loop through each row to get track details and add to DataFrame
for i, row in df_spotify.iterrows():
    track_id = search_track(row['track_name'], row['artist_name'], access_token)
if track_id:
    image_url = get_track_details(track_id, access_token)
df_spotify.at[i, 'image_url'] = image_url

#Save the updated DataFrame (replace 'updated_file.csv' with your desired output file name)
df_spotify.to_csv('updated_file.csv', index=False)