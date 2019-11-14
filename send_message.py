from flask import Flask, request
from twilio.rest import Client
import requests, json
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
#load_dotenv(dotenv_path=env_path)
load_dotenv(find_dotenv())

app = Flask(__name__)
#https://timberwolf-mastiff-9776.twil.io/demo-reply

@app.route('/')
def index():
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     from_='whatsapp:+14155238886',
                     body='Your appointment is coming up on July 21 at 3PM',
                     to='whatsapp:+233242407403'
                 )

    print(message.sid)
    return message.body


@app.route('/recieve', methods=['POST'])
def webhook():
    print("webhook"); sys.stdout.flush()
    
    if request.method == 'POST':
        print(request.json)
        index()
        return '', 200

    else:
        abort(400)


if __name__ == '__main__':
    app.run()