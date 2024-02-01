from flask import Flask, request, jsonify
import traceback
import random
import openai
import os
from dotenv import load_dotenv
import uuid

load_dotenv()

openai.api_key = os.getenv('openai_api_key')

app = Flask(__name__)

@app.route('/webhook2', methods=['POST'])
async def webhook():
    miniasshole_responses = [
        "figure it out. ",
        "Please don't call dipo",
        "I took pride in a crappy work",
        "yeah I wrote it all but I don't know how it works too.",
        "OMG. Dipo isn't debugging it for you."
    ]
    try:
        would_be_filled
        return jsonify({'fulfillmentText': response})
    except:
        return jsonify({'fulfillmentText': random.choice(miniasshole_responses)})

if __name__ == "__main__":
    app.run()


