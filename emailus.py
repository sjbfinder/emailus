import os 
from email.message import EmailMessage
import ssl
import smtplib
import json
import requests
import time



while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(key)
    data = data.json()
    Btcprice=(f"{data['symbol']} price is {data['price']}")

    email_sender="sjbfinder@gmail.com"
    Random="pmxastrgusttvblk"
    booreceiver= "sjbfinder@gmail.com"
    boo="sjbboopathiraj.adobe@gmail.com"
    dhaya="dhayabtc08@gmail.com"
    subject=Btcprice + '('+current_time+')'
    body=Btcprice + '('+current_time+')'

    em=EmailMessage()
    em['From']=email_sender
    em['To']= boo
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
        smtp.login(email_sender,Random)
        smtp.sendmail(email_sender,boo,em.as_string())
        smtp.sendmail(email_sender,dhaya,em.as_string())
        print("sent")
    time.sleep(300) 