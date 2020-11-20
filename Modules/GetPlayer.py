def GetPlayer(text,PlayersModel):
    name = text.split('/')[1]
    query = PlayersModel.query.filter(PlayersModel.name.ilike('%'+name+'%')).first()
    if query != None:
        messages = [{
            'type': 'text',
            'text': f"{query.name}:{query.from_}-{query.to_}"
        }]
    else:
            messages = [{
            'type': 'text',
            'text': f"找不到與{name}相關的球員!"
        }]
    return messages