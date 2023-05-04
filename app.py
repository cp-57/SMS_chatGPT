from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

# Initialize the OpenAI API client
openai.api_key = "OPEN_API_KEY"

@app.route("/sms", methods=["POST"])
def sms():
    # Get the incoming message body and phone number
    body = request.form.get("Body")
    from_number = request.form.get("From")

    # Call GPT-3.5 to get a response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "user", "content": body}
        ]
    )

    gpt_response = completion.choices[0].message.content

    # Send a text message back to the original phone number with the GPT-3.5 response
    resp = MessagingResponse()
    resp.message(gpt_response)
    return str(resp)
