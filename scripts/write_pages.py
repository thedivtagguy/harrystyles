import smtplib, ssl
from email.message import EmailMessage
from random import randint
import requests
import datetime
from datetime import datetime 
import json
import csv
import pandas as pd
import cloudinary
from cloudinary import uploader
from monsterurl import get_monster

def writepage():    
    
    cloudinary.config(
     cloud_name = 'yourthing',  
     api_key = 'yourkey',  
     api_secret = 'yoursecret'  
     )
    
     # What item are we on?
    with open('item.txt') as f:
        item = f.readline()
    
    item = int(item) 
    i = str(item)
    x = item
    j = item + 1
    mood = cloudinary.uploader.upload("../emails/headers/tm"+str(j)+".jpg")
    mood = mood['url']
    ###### Variables for the Emails #######
    
    # Random Stats
    value1 = randint(0, 2000)
    value1 = str(value1)
    value2 = randint(70, 250)
    value2 = str(value2)
    
    # Quote of Interest 
    while True:
        quote = requests.get('https://officeapi.dev/api/quotes/random')
        quote = json.loads(quote.text)
        quote = quote['data']['content']
        if(len(quote) <= 150):
            break
    
    # Subject line
    
    while True:  
        subjectline = requests.get('https://breakingbadapi.com/api/quote/random')  
        subjectline = json.loads(subjectline.text)
        subjectline = subjectline[0]['quote']
        if(len(subjectline) <= 70):  
            break  
        
    subjectline = requests.get('https://breakingbadapi.com/api/quote/random')
    subjectline = json.loads(subjectline.text)
    subjectline = subjectline[0]['quote']
    
    
    ##### Get the GIFs for today ready #####
    
    
    df = pd.read_csv("../data/urls.csv")
    # Select Item
    df = df.loc[df['item'] == x]
    
    dh_id = df.loc[df['artists'] == 'dh']['id'].item()
    db_id = df.loc[df['artists'] == 'db']['id'].item()
    mh_id = df.loc[df['artists'] == 'mh']['id'].item()
    mb_id = df.loc[df['artists'] == 'mb']['id'].item()
    
    
    
    ####### Pulling the Lines for Today's Email#########
    
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
    item = item 
    
    # Choose Quote from Array
    quote_dict = {1: michael_harry[item], 
                  2: dwight_harry[item], 
                  3: dwight_beatles[item], 
                  4: michael_beatles[item]
                  }
    
    
    dh_q = str(quote_dict[2]) # Gif 1
    mb_q = str(quote_dict[4]) # Gif 2
    db_q = str(quote_dict[3]) # Gif 3
    mh_q = str(quote_dict[1]) # Gif 4
     
  
    # Write Text
    text = """\
    <html>
        <body style="background: #fff;font: 15px/24px; background-color: #ffffff; margin: 0; -webkit-font-smoothing: antialiased;font-smoothing: antialiased; max-width:500px; margin:auto; padding-top:10vh;">
        <div>
        <div style="text-align:center;">
        <h1 style="
    font-family: Menlo, Courier;
    font-weight: 600;
    font-size: 38px;
    text-align: center;
">GIF-y Lyrical Nonsense</h1>
            <img src="https://i.imgur.com/3iwaXVk.jpg">
            <img src="{mood}" style="width:80%;">

        </div>
            <div class="message-body">
                <div class="digest" style="margin-bottom: 3rem;">
    
                    <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0; margin-bottom: 1rem;">Hi, <br> I just read <strong id="number1">{value1}</strong> unique lines from <strong id="number2">{value2}</strong> different pieces of work by <strong>Schrute, Lennon et. Al, Scott and Styles.</strong></p>
    
                    <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0; margin-bottom: 1rem;">This quote caught my eye <strong>{quote}</strong>.</p>
    
                </div>
    
                <div class="top-by-share" style="margin-bottom: 3rem;">
                    <p class="section-title" style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; font-weight: bold;  margin: 0; padding-bottom:10px;">BASED ON MY READING, I TRIED WRITING THESE LINES FOR YOU</p>
    
                    <div class="link" style="margin-bottom: 2rem; text-align:center;">
                        <img src="https://media.giphy.com/media/{dh_id}/source.gif" style="padding:10px;">
                        <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0;">{dh_q}</p>
    
                    </div>
    
                    <div class="link" style="margin-bottom: 2rem; text-align: center;">
                    <img src="https://media.giphy.com/media/{db_id}/source.gif" style="padding:10px;">
                        <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0;">{db_q}</p>
    
                    </div>
    
                    <div class="link" style="margin-bottom: 2rem;text-align: center;">
                    <img src="https://media.giphy.com/media/{mh_id}/source.gif" style="padding:10px;">
                        <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0;">{mb_q}</p>
    
                    </div>
    
                    <div class="link" style="margin-bottom: 2rem;text-align: center;">
                    <img src="https://media.giphy.com/media/{mb_id}/source.gif" style="padding:10px;">
                        <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0;">{mh_q}</p>
    
                    </div>
                </div>
                <div class="promo" style="margin-bottom: 3rem;">
                    <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0; margin-bottom: 1rem;">
                    I read quotes by Michael and Dwight and songs by The Beatles and Harry, and try to write stuff they might write on my own. Since I'm unsupervised, I might say weird stuff from time to time. <br> <br> Sometimes you win, sometimes you lose. Hope this writing wasn't complete nonsense. Thanks for reading.
                    </p>
    
                    <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0; margin-bottom: 1rem;">Have a great week! (ʘ‿ʘ)╯</p>
                    <h6 style="padding-bottom:10px;font-size:8px;text-align:right;color:gray;">Header by thatsbelievable via tumblr</h6>

                </div>
            </div>
    
    
        </div>
    </body>
    </html>
    """.format(value1=value1, 
               value2=value2, 
               quote=quote, 
               dh_q = dh_q, 
               mb_q = mb_q, 
               db_q = db_q,
               mh_q = mh_q,
               dh_id = dh_id, 
               db_id = db_id,
               mh_id = mh_id,
               mb_id = mb_id, 
               mood = mood)
        
    file = open("../pages/" + get_monster() + ".html" ,"w", encoding="utf-8")
    file.write(text)
    file.close() 
        
    # Update the item for next week
    item = item + 1
    
    # Overwrite item text file
    with open('item.txt', 'w') as filetowrite:
        filetowrite.write(str(item))
    
    print("Newsletter generated for " + str(item -1))
