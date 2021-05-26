from giphypop import upload
import csv
import io
from datetime import datetime
import pandas as pd

def upload_gifs():    
    gif_path = '../gifs/'
    urls = {}
    counter = 0
    
    date = datetime.today().strftime('%Y-%m-%d')
    dh = gif_path + "dwight_harry_" + date + ".gif"
    db = gif_path + "dwight_beatles_" + date + ".gif"
    mh = gif_path + "michael_harry_" + date + ".gif"
    mb = gif_path + "michael_beatles_" + date + ".gif"
    
    gif_dict = [
        {
        'path': dh,
        'artists': "dh",
        'date': date,
        'id': ""
        }, 
        {
        'path': db,
        'artists': "db",
        'date': date,
        'id': ""
        },
        {
        'path': mh,
        'artists': "mh",
        'date': date,
        'id': ""
        }, 
         {
        'path': mb,
        'artists': "mb",
        'date': date,
        'id': ""
        }]
    
    
    while counter < 4: 
        gif = upload(["shitpostsforrhe"], 
                     gif_dict[counter]['path'], 
                     username="amnbh", 
                     api_key="kL0fDnW1p2m8G4eoFZ0yiTXeA0NdcQlL")
        gif = str(gif.id)
        gif_dict[counter]['id'] = gif
        counter = counter + 1
        
    field_names= ['path', 'artists', 'date', 'id']
    
    with open('../data/urls.csv',  newline='', mode='a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(gif_dict)
        
    print("Uploaded GIFs and IDs written to CSV for " + date)
    
    
