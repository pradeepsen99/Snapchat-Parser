import json

username = input()

recieved = 0
print('-----SNAPS-----')
#Recieved snaps
with open('json/snap_history.json') as json_file:
    data = json.load(json_file)
    for p in data['Received Snap History']:
        if p['From'] == username: recieved = recieved + 1

    print('Snaps recieved = ' + repr(recieved))
    
#Sent snaps
sent = 0
with open('json/snap_history.json') as json_file:
    data = json.load(json_file)
    for p in data['Sent Snap History']:
        if p['To'] == username: sent = sent + 1

    print('Snaps sent = ' + repr(sent))
    print('')
    print('')
    
    
print('-----MESSAGES-----')
#Recieved messgaes
recieved = 0
with open('json/chat_history.json') as json_file:
    data = json.load(json_file)
    for p in data['Received Chat History']:
        if p['From'] == username: recieved = recieved + 1

    print('Messages recieved = ' + repr(recieved))
    
#Sent messages
sent = 0
with open('json/chat_history.json') as json_file:
    data = json.load(json_file)
    for p in data['Sent Chat History']:
        if p['To'] == username: sent = sent + 1

    print('Messages sent = ' + repr(sent))
    
print('')