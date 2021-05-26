import smtplib, ssl
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
from random import randint
import requests
from datetime import datetime
import json
import csv
import pandas as pd
from imgurpython import ImgurClient


def send_newsletter():    
    gif_path = '../gifs/'
    tm_path = '../emails/header/'
    
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
    
    # Filenames
    date = datetime.today().strftime('%Y-%m-%d')
    
    
    
    df = pd.read_csv("../data/urls.csv")
    # Select today's date
    df = df.loc[df['date'] == date]
    
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
     
    #############################################
    
    sender_email = "dwightbeatlesmichaelharry@gmail.com"
    receiver_email = "amanbhargava2001@gmail.com"
    password = input("Type your password and press enter:")
    
    msg = EmailMessage()
    
    # generic email headers
    msg['Subject'] = subjectline + ' | ' + 'Shitposts for Rhe '
    msg['From'] = 'Messrs. DBMH dwightbeatlesmichaelharry@gmail.com'
    msg['To'] = 'amanbhargava2001@gmail.com'
    
    # set the plain text body
    msg.set_content(quote)
    
    # now create a Content-ID for the image
    tm = make_msgid(domain='xyz.com')
    
    
    # set an alternative html body
    msg.add_alternative("""\
    <html>
        <body style="background: #fff;font: 15px/24px; background-color: #ffffff; margin: 0; -webkit-font-smoothing: antialiased;font-smoothing: antialiased; max-width:500px; margin:auto; padding-top:10vh;">
        <div>
        <div style="text-align:center;">
            <img src="https://i.imgur.com/3iwaXVk.jpg">
            <img src="cid:{tm}" style="padding-bottom:10px;">
        </div>
            <div class="message-body">
                <div class="digest" style="margin-bottom: 3rem;">
    
                    <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0; margin-bottom: 1rem;">Hi Rhe, <br> In the past week, I read <strong id="number1">{value1}</strong> unique lines from <strong id="number2">{value2}</strong> different pieces of work by <strong>Schrute, Lennon et. Al, Scott and Styles.</strong></p>
    
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
                    Every week, I read quotes by Michael and Dwight and songs by The Beatles and Harry, and try to write stuff they might write on my own. Since I'm unsupervised, I might say weird stuff from time to time. <br> <br> Sometimes you win, sometimes you lose. Hope this week's writing wasn't complete nonsense. See ya later. 
                    </p>
    
                    <p style="font-family: Menlo, Courier, Courier New, monospace; line-height: 1.25; font-size: 16px; margin: 0; margin-bottom: 1rem;">Have a great week! (ʘ‿ʘ)╯</p>
                </div>
            </div>
    
    
        </div>
    </body>
    </html>
    """.format(tm=tm[1:-1], 
               value1=value1, 
               value2=value2, 
               quote=quote, 
               dh_q = dh_q, 
               mb_q = mb_q, 
               db_q = db_q,
               mh_q = mh_q,
               dh_id = dh_id, 
               db_id = db_id,
               mh_id = mh_id,
               mb_id = mb_id), subtype='html')
        
    # Attaching Tonights Mood
    with open('../emails/headers/tm1.jpg', 'rb') as mood:
        # know the Content-Type of the image
        maintype, subtype = mimetypes.guess_type(mood.name)[0].split('/')
        # attach it
        msg.get_payload()[1].add_related(mood.read(), 
                                             maintype=maintype, 
                                             subtype=subtype, 
                                             cid=tm)
        
        
        
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )
        
    # Update the item for next week
    item = item + 1
    
    # Overwrite item text file
    with open('item.txt', 'w') as filetowrite:
        filetowrite.write(str(item))
    
    print("Newsletter sent for " + date + ", see you next week!")
