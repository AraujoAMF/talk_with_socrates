#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
app = Flask(__name__)
#create chatbot
SOCRATES = ChatBot("SOCRATES", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    socrates_response = str(SOCRATES.get_response(userText))
    
    return str(SOCRATES.get_response(userText))
if __name__ == "__main__":
    app.run()