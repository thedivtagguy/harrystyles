import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes

sender_email = "dwightbeatlesmichaelharry@gmail.com"
receiver_email = "amanbhargava2001@gmail.com"
password = input("Type your password and press enter:")

msg = EmailMessage()

# generic email headers
msg['Subject'] = 'Hello there'
msg['From'] = 'dwightbeatlesmichaelharry@gmail.com'
msg['To'] = 'amanbhargava2001@gmail.com>'

# set the plain text body
msg.set_content('This is a plain text body.')

# now create a Content-ID for the image
image_cid = make_msgid(domain='xyz.com')
# if `domain` argument isn't provided, it will 
# use your computer's name

# set an alternative html body
msg.add_alternative("""\
<html>
    <body>
        <p>This is an HTML body.<br>
           It also has an image.
        </p>
        <img src="cid:{image_cid}">
    </body>
</html>
""".format(image_cid=image_cid[1:-1]), subtype='html')
# image_cid looks like <long.random.number@xyz.com>
# to use it as the img src, we don't need `<` or `>`
# so we use [1:-1] to strip them off


# now open the image and attach it to the email
with open('/header/header.jpg', 'rb') as img:

    # know the Content-Type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    # attach it
    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)


# the message is ready now
# you can write it to a file
# or send it using smtplib

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )