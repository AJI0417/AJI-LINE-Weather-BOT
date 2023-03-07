from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi, WebhookHandler
)
from flask import Flask, render_template, request, abort
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

line_bot_api = LineBotApi('L2Vo1hLpJWnisu+VRhYHChs0eUDPvshGxbBwLzLXDa8jFVMJJ/tV1DwwhA4QvP2hYnZQBPn9zLC+PZCrNYJyNhsoAv3HHZ40N1RUKQQK/hO/yzA8AjAbl+y+8qmp06mZSImzcdZShZge0F4ikDXJDQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f3c8476f41d209a4924b3013deaac41c')


@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@app.route('/')
def index():
    return "OKOK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
