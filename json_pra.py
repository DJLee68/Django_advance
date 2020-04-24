import json

diary = {
    'id' : '3',
    'title' : 'hi',
    'body' : 'my name is DJ',
}

print(diary)
print(type(diary))

diary_s = json.dumps(diary) #dumps : dictionary --> json

print(diary_s)
print(type(diary_s))

diary_back = json.loads(diary_s)

print(diary_back)
print(type(diary_back))
