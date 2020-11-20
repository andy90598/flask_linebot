import random

def FistGame(playerFist):
    # 如果使用者輸入 剪刀、石頭、布其中之一
    # 系統返回隨機一種拳法，並判斷輸贏
    # 傳送輸贏結果給使用者
    fist = ['剪刀','石頭','布']
    sticker = ['292','295','296']
    # 判斷是否要猜拳
    ai = random.randint(0,2)
    player = fist.index(playerFist)
    # 平手
    if ai == player :
        messages=[
            {
                'type': 'sticker',
                'packageId': '4',
                'stickerId': sticker[ai]
            },
            {
                'type': 'text',
                'text':'電腦出'+fist[ai]+'，平手'
            }
        ]
    # 玩家勝利結果
    elif (ai== 0 and player==1) or (ai == 1 and player == 2) or (ai == 2 and player == 0):
        messages=[
            {
                'type': 'sticker',
                'packageId': '4',
                'stickerId': sticker[ai]
            },
            {
                'type': 'text',
                'text':'電腦出'+fist[ai]+'，你獲勝'
            }
        ]
    # 玩家失敗結果
    else: 
        messages=[
            {
                'type': 'sticker',
                'packageId': '4',
                'stickerId': sticker[ai]
            },
            {
                'type': 'text',
                'text': '電腦出'+fist[ai]+'，你輸了'
            }
        ]
    return messages