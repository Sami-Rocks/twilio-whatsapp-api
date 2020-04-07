from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST', 'GET'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    chatbot = ChatBot('Fall')
    trainer= ListTrainer(chatbot)
    response = chatbot.get_response(msg)
   
    # Create reply
    resp = MessagingResponse()
    resp.message(str(response))
    
    
    return str(resp)

if __name__ == "__main__":
    app.run()