from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
# Modules
from Modules.ReplyMessage import ReplyMessage 
from Modules.FistGame import FistGame
from Modules.MyScheduler import MyScheduler
from Modules.RentHouse import RentHouse
from Modules.LineReply import LineReply
from Modules.GetPlayer import GetPlayer
#Models
from Models.PlayersModel import PlayersModel
#other
import json
import os

MyScheduler()

db = SQLAlchemy()

app = Flask(__name__)

URL = os.environ.get('DATABASE_URL', None)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #line POST請求前處理
        message,replyToken,messageType = LineReply(request)

        #判斷是否為文字訊息
        if messageType == 'text':
            #取得使用者說的話
            text = message.get('message').get('text')
            print('text:',text)
            
            #猜拳
            fist = ['剪刀','石頭','布']
            if text in fist:
                messages = FistGame(text)
            elif text.find('租屋') != -1:
                #租屋 台中市
                messages = RentHouse(text)
            elif text.find('球員/') != -1:
                #球員/球員名稱
                messages = GetPlayer(text,PlayersModel)
            elif text.find('新增球員資料') != -1:
                f = open('nba.json','r',encoding='utf-8')
                nbaData = json.loads(f.read())
                allData =[]
                for player in nbaData['players']:
                    name = player.get('name')
                    from_ = int(player.get('from'))
                    to_ = int(player.get('to'))
                    position = ','.join(player.get('position'))
                    height = player.get('height')
                    weight = player.get('weight')
                    birthday = player.get('birthday')
                    college = ','.join(player.get('college')).replace("'","’")
                    allData.append(PlayersModel(name,from_,to_,position,height,weight,birthday,college))
                db.session.add_all(allData)
                db.session.commit()
                messages = [{
                    'type': 'text',
                    'text': '新增完成'
                }]
            else :
                messages = [{
                    'type': 'text',
                    'text': '我聽不懂你在說什麼'
                }]
            ReplyMessage(replyToken,messages) 

        return 'succeed'
    else: 
        return 'alive'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

    