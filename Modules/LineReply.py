def LineReply(request):
    message = request.get_json().get('events')[0]
    print(message)
    replyToken = message.get('replyToken')
    messageType = message.get('message').get('type')
    return [message,replyToken,messageType]