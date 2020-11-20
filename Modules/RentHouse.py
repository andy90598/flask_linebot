import requests
from bs4 import BeautifulSoup
import json

def RentHouse(text):
    #租屋 台中市
    textSplit =text.split(' ')
    if len(textSplit) == 2:
        cityName = textSplit[1].replace('臺','台')
    else :
        cityName =''
        
    cityId = {'台北市': '1','基隆市': '2','新北市': '3','新竹市': '4','新竹縣': '5','桃園市': '6','苗栗縣': '7','台中市': '8','彰化縣': '10','南投縣': '11','嘉義市': '12','嘉義縣': '13','雲林縣': '14','台南市': '15','高雄市': '17','屏東縣': '19','宜蘭縣': '21','花蓮縣': '23','台東縣': '22','金門縣': '25','澎湖縣': '24','連江縣': '26'}
    
    if cityId.get(cityName) != None:
        cookies = {
            'urlJumpIp':cityId.get(cityName)
        }
        url='https://rent.591.com.tw/?kind=0&region='+cityId.get(cityName)
        print(url)
        r = requests.get(url,cookies=cookies)

        soup = BeautifulSoup(r.text , 'html.parser')

        houseCards = soup.select('.listInfo')

        carousel = {
        'type': 'carousel',
        'contents': [
            
            ]
        }
        count = 1
        for houseInfo in houseCards :
            imgUrl = houseInfo.select('.imageBox img')[0].get('data-original')
            titleArea = houseInfo.select('.infoContent h3 a')[0]
            title = titleArea.text
            infoUrl = 'https:'+titleArea.get('href')

            bubble={
                'type': 'bubble',
                'direction': 'ltr',
                'header': {
                    'type': 'box',
                    'layout': 'vertical',
                    'contents': [
                    {
                        'type': 'text',
                        'text': title,
                        'align': 'center',
                        'wrap': True,
                        'contents': []
                    }
                    ]
                },
                'hero': {
                    'type': 'image',
                    'url': imgUrl,
                    'size': 'full',
                    'aspectRatio': '1.51:1',
                    'aspectMode': 'cover'
                },
                'footer': {
                    'type': 'box',
                    'layout': 'horizontal',
                    'contents': [
                    {
                        'type': 'button',
                        'action': {
                        'type': 'uri',
                        'label': '查看詳細',
                        'uri': infoUrl
                        }
                    }
                    ]
                }
            }

            if count <= 12:
                carousel['contents'].append(bubble)
            else:
                break

            count += 1

        flexBox = [{
        'type': 'flex',
        'altText': 'this is a flex message',
        'contents': carousel
        }]
        # print(flexBox)
        return flexBox
    else:
        return ''