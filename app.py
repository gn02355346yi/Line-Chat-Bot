from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random

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
    gag = {"衛斯理是誰" : "衛斯理是元介", "馬首姓什麼":"詹, 馬首是詹", "周玉蔻老了變什麼":"老coco"}
    message = event.message.text
    ID = event.source.user_id
    profile = line_bot_api.get_profile(ID)
    if any(x in message for x in ["地點", "哪裡", "住哪","在哪"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "在九樓喔！"))

    elif any(x in message for x in ["幾歲", "年紀", "年齡","貴庚"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "五十歲！！"))   

    elif any(x in message for x in ["誰辦", "主辦","主持", "mc"]):
        line_bot_api.reply_message(event.reply_token, [ImageSendMessage(original_content_url='https://i.imgur.com/lIZYmaX.png',
    preview_image_url='https://i.imgur.com/lIZYmaX.png'),ImageSendMessage(original_content_url='https://cc.tvbs.com.tw/news3.0/tvbs/news/entertainment/images/2015/11/06/2.jpg?__scale=h:441,w:662,cx:3,cy:0,ch:437,cw:659',
    preview_image_url='https://cc.tvbs.com.tw/news3.0/tvbs/news/entertainment/images/2015/11/06/2.jpg?__scale=h:441,w:662,cx:3,cy:0,ch:437,cw:659')])

    elif any(x in message for x in ["多久", "到幾點", "結束"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "大約兩小時喔！")) 

    elif any(x in message for x in ["時間", "幾點", "時候", "何時"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "時間是 8/10 中午12點喔！"))    

    elif any(x in message for x in ["獎品", "禮物", "紀念品"]):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "我們的禮物是秘密不能講明，就算我愛你也不能夠說明"))
            
    elif any(x in message for x in ["你是誰", "你叫什麼", "名字","哪位"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "你好~ 我是蛋糕！"),StickerSendMessage(package_id = '3', sticker_id = '124')] )      
    
    elif any(x in message for x in ["Ines", "ines", "白庭安"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "Ines在拍孤兒怨續集喔！"),ImageSendMessage(original_content_url='https://i.imgur.com/lIZYmaX.png',
    preview_image_url='https://i.imgur.com/lIZYmaX.png')])
    
    elif any(x in message for x in ["Daniel", "daniel", "郭道儒"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "Daniel在賣手錶喔！"),ImageSendMessage(original_content_url='https://cc.tvbs.com.tw/news3.0/tvbs/news/entertainment/images/2015/11/06/2.jpg?__scale=h:441,w:662,cx:3,cy:0,ch:437,cw:659',
    preview_image_url='https://cc.tvbs.com.tw/news3.0/tvbs/news/entertainment/images/2015/11/06/2.jpg?__scale=h:441,w:662,cx:3,cy:0,ch:437,cw:659')])
    
    elif any(x in message for x in ["Lawrence", "lawrence", "羅倫斯"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "Lawrence在佛羅倫斯喔"),ImageSendMessage(original_content_url='https://img.appledaily.com.tw/images/ReNews/20150622/640_a31496282a31c58a46c19028b9a28ed7.jpg',
    preview_image_url='https://img.appledaily.com.tw/images/ReNews/20150622/640_a31496282a31c58a46c19028b9a28ed7.jpg')])    
    
    elif any(x in message for x in ["你好", "妳好", "嗨", "安安"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = profile.display_name + "你好!" + " 要來參加 Appreciation Day 活動喔～"),StickerSendMessage(package_id = '3', sticker_id = '134')])
    
    elif any(x in message for x in ["來幹嘛", "目的", "做什麼", "做啥"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = profile.display_name + "你好!" + " 我是來宣傳 Appreciation Day 活動的喔～"),StickerSendMessage(package_id = '3', sticker_id = '134')])
    
    elif any(x in message for x in ["要幹嘛", "內容", "活動"]):
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text = "吃吃喝喝有吃有拿喔！ 還有Intern們拍的精彩影片～"),StickerSendMessage(package_id = '3', sticker_id = '134')])
    
    elif message in gag:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = gag[message])) 
 
            
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
