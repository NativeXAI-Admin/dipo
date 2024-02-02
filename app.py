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
    random_responses = [
        "hey, I think you made a mistake.",
        "Please try a different query.",
        'Try {"queryResult": {"queryText": "Hello, how are you?"}}',
        'Try agin, Take a break and try again.'
    ]
    try:
        would_be_filled
        return jsonify({'fulfillmentText': response})
    except:
        return jsonify({'fulfillmentText': random.choice(random_responses)})

if __name__ == "__main__":
    app.run()


