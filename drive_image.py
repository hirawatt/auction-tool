import requests
from urllib.parse import urlparse
import pandas as pd

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":

    player_info = pd.read_csv("./data/jito-4-team-list.csv")
    player_name_all = player_info["Name"]
    for index in range(len(player_name_all)):
        player_name = player_info.iat[index, 1]
        player_image = player_info.iat[index, 14]
        
        link = urlparse(player_image)
        image_id = link.query[3:]
        destination = './img/{}-{}.jpg'.format(index, player_name)
        download_file_from_google_drive(image_id, destination)
