import requests
import json
import os
def ReplyMessage(replyToken,messages):
    #請使用自己的token
    accessToken = os.environ.get('ACCESSTOKEN', None)  
    
    headers ={
        'Content-Type':'application/json',
        'Authorization': 'Bearer '+accessToken
    }
    data ={
        'replyToken':replyToken,
        'messages':messages
    }
    url = 'https://api.line.me/v2/bot/message/reply'
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r