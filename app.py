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
    if any(x in message for x in ["地點", "哪裡"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "地點在九樓喔！"))
    elif any(x in message for x in ["時間", "幾點", "時候"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "時間是 8/10 下午四點喔！"))    
    elif any(x in message for x in ["你是誰", "你叫什麼", "名字"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "你好~ 我是帥哥道儒 想跟我說話的話要先加我好友喔！"),StickerSendMessage(package_id = '3', sticker_id = '124')] )      
    elif "Ines" in message:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "Ines在拍孤兒怨續集喔！"),ImageSendMessage(original_content_url='https://pic.pimg.tw/boxout/1424621892-2067594777.jpg?v=1424621893',
    preview_image_url='https://pic.pimg.tw/boxout/1424621892-2067594777.jpg?v=1424621893')])
    elif any(x in message for x in ["你好", "妳好", "嗨"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = profile.display_name + "你好!" + " 要來參加 Appreciation Day 活動喔～"),StickerSendMessage(package_id = '3', sticker_id = '134')])
    elif any(x in message for x in ["來幹嘛", "目的", "做什麼", "做啥"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = profile.display_name + "你好!" + " 我是來宣傳 Appreciation Day 活動的喔～"),StickerSendMessage(package_id = '3', sticker_id = '134')])
    elif any(x in message for x in ["要幹嘛", "內容", "活動"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "吃吃喝喝有吃有拿喔！ 還有Intern們拍的精彩影片～"),StickerSendMessage(package_id = '3', sticker_id = '134')])
    elif message == "衛斯理是誰":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "衛斯理是元介"))  
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message + "你大頭啦"))         
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
