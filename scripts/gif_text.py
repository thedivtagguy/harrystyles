from PIL import Image, ImageDraw, ImageFont, ImageSequence
import requests
import io
import random
import csv
import giphy_client
import time
from giphy_client.rest import ApiException
from datetime import datetime
from textfit import fit_text

def make_gif():
    date = datetime.today().strftime('%Y-%m-%d')
    # Read in CSV
    
    csv_file = '../data/lyrics.csv'
    
    # Define the Arrays
    michael_harry = []
    dwight_harry = []
    dwight_beatles = []
    michael_beatles = []
    
    # Columns to Arrays
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            michael_harry.append(row.get('michael_harry'))
            dwight_harry.append(row.get('dwight_harry'))
            dwight_beatles.append(row.get('dwight_beatles'))
            michael_beatles.append(row.get('michael_beatles'))
            
    # What item are we on?
    with open('item.txt') as f:
        item = f.readline()
    
    item = int(item)
    
    # Choose Quote from Array
    mh = michael_harry[item]
    dh = dwight_harry[item]
    db = dwight_beatles[item]
    mb = michael_beatles[item]
    quote_dict = {1: mh, 2: dh, 3: db, 4: mb}
    
    
    tags = ["mb", "dh", "db", "mh"]
    mic_b = ["michael scott", "the beatles", "john lennon", "the office"]
    dwi_b = ["dwight schrute", "the beatles", "the office", "rock and roll"]
    mic_h = ["michael scott", "harry styles", "watermelon sugar" ]
    dwi_h = ["dwight schrute", "harry styles", "watermelon sugar"]
    
    batch = 1
    artists = ''
    tag_name =""
    
    while batch <= 4:
        
        if batch == 1:
            artists = "michael_beatles"
            tag_name = random.choice(mic_b)
        elif batch == 2:
            artists = "dwight_harry"
            tag_name = random.choice(dwi_h)
        elif batch == 3:
            artists= "dwight_beatles"
            tag_name = random.choice(dwi_b)
        elif batch == 4:
            artists = "michael_harry"
            tag_name = random.choice(mic_h)
    
        # GIPHY RANDOM GIF 
        # create an instance of the API class
        api_instance = giphy_client.DefaultApi()
        api_key = 'kL0fDnW1p2m8G4eoFZ0yiTXeA0NdcQlL' # str | Giphy API Key.
        tag = tag_name # str | Filters results by specified tag. (optional)
        rating = 'g' # str | Filters results by specified rating. (optional)
        fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
        
        try: 
            # Random Endpoint
            api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)
        
        
        # Font Decisions
        fonts = ["MATURASC", "BebasNeue-Regular", "PLAYBILL", "HATTEN", "impact"]
        font_name = random.choice(fonts)
        print("Creating Gif for " + artists)
        im = Image.open(requests.get(api_response.data.image_original_url, stream=True).raw)
        width, height = im.size
        Font = ImageFont.truetype(font_name, 30)
        
        # Print the text
        frames = []
        for frame in ImageSequence.Iterator(im):
        	frame = frame.convert('RGBA')
        	d = ImageDraw.Draw(frame)
        	fit_text(frame, quote_dict[batch], Font, (255,255,0), height/2)
        	del d
        	frames.append(frame)
        my_bytes = io.BytesIO()                                                                
        
        gif_name = artists + "_" + date
        file_path = '../gifs/' + gif_name + '.gif'
        frames[0].save(file_path, save_all=True, append_images=frames[1:])
        
        batch = batch + 1
        
    print("Created GIFs for " + date + ", uploading them now...")

    
