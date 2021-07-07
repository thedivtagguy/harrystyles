from giphypop import upload
import csv
import os.path

def upload_gifs():    
    gif_path = '../gifs/'
    counter = 0
    
  # What item are we on?
    with open('item.txt') as f:
        item = f.readline()
    
    item = int(item)
    dh = gif_path + "dwight_harry_" + str(item) + ".gif"
    db = gif_path + "dwight_beatles_" + str(item) + ".gif"
    mh = gif_path + "michael_harry_" + str(item) + ".gif"
    mb = gif_path + "michael_beatles_" + str(item) + ".gif"
    
    gif_dict = [
        {
        'path': dh,
        'artists': "dh",
        'item': item,
        'id': ""
        }, 
        {
        'path': db,
        'artists': "db",
        'item': item,
        'id': ""
        },
        {
        'path': mh,
        'artists': "mh",
        'item': item,
        'id': ""
        }, 
         {
        'path': mb,
        'artists': "mb",
        'item': item,
        'id': ""
        }]
    
    
    while counter < 4: 
        gif = upload(["shitpostsforrhe"], 
                     gif_dict[counter]['path'], 
                     username="yourusername", 
                     api_key="yourkey")
        print("Uploading GIF #" + str(counter))
        gif = str(gif.id)
        gif_dict[counter]['id'] = gif
        counter = counter + 1
        
    field_names= ['path', 'artists', 'item', 'id']
    file_exists = os.path.isfile('../data/urls.csv')
    x = 0

    # Write headers only if new file
    with open ('../data/urls.csv', 'a') as csvfile:
        field_names= ['path', 'artists', 'item', 'id']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=field_names)
    
        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header
        
        while x < 4:
            writer.writerow({'path': gif_dict[x]['path'], 
                             'artists': gif_dict[x]['artists'],
                             'item': gif_dict[x]['item'], 
                             'id': gif_dict[x]['id']
                             })
            x = x + 1

        
    print("Uploaded GIFs and IDs written to CSV for " + str(item))
    
    
