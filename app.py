from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('P/X8ZpZKKhbaNB26XwTYPXgJ0ocZsIQeuOZgXLVa2WtnlkhxZZLYhqBp/yL6JzqVGtQ8ORoO3Ome299YE4dna+yVWLhsszE2K/MIK2xPdvJ/6M8Qi1Ca5Cq+633O+AWGrjW/CJ8xATx10AieQpNtZAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6e357d65cf80d1d96dd153225542fd73')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    ID = event.source.user_id
    profile = line_bot_api.get_profile(ID)
    if "地點" in message:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "地點在九樓喔！"))
    elif "時間" in message:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "時間是 8/10 下午四點喔！"))    
    elif any(x in message for x in ["你", "是誰", "名字","叫什麼"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "你好~ 我是帥哥道儒"),StickerSendMessage(package_id = '3', sticker_id = '124')] )      
    elif profile.display_name == "Ines":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = profile.display_name + "拍孤兒怨"))
    else:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = profile.display_name + "你好!"),StickerSendMessage(package_id = '3', sticker_id = '1')])

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
