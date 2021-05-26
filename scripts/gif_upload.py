from giphypop import upload
import csv
from datetime import datetime
import os.path

def upload_gifs():    
    gif_path = '../gifs/'
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
    file_exists = os.path.isfile('../data/urls.csv')
    x = 0

    # Write headers only if new file
    with open ('../data/urls.csv', 'a') as csvfile:
        field_names= ['path', 'artists', 'date', 'id']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=field_names)
    
        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header
        
        while x < 4:
            writer.writerow({'path': gif_dict[x]['path'], 
                             'artists': gif_dict[x]['artists'],
                             'date': gif_dict[x]['date'], 
                             'id': gif_dict[x]['id']
                             })
            x = x + 1

        
    print("Uploaded GIFs and IDs written to CSV for " + date)
    
    
