"Managing subscription list"

import json

print("Loading subscription file...")
try:
    with open("subscriptions.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        print("Loaded subscription file.")
except:
    with open("subscriptions.json", "w+", encoding='utf-8') as f:
        data = { "subscriptions": [] }
        json.dump(data, f)
        data = json.dumps(data)
        data = json.loads(data)
        print("Subscription file not present, generated one.")



def subscriptionWrite():
    '''Writes current subscription configuration to disk'''
    try:
        with open("subscriptions.json", "w", encoding='utf-8') as f:
            json.dump(data, f)
        return "wrote data successfully"
    except:
        return "writing failed"


def subscriptionAdd(channel):
    '''Adds channel specified to subscriptions'''
    if len(channel) == 24 and channel not in data["subscriptions"]:
        data["subscriptions"].append(channel)
        return "added channel "+channel+" successfully"
    return "need channel id"



def subscriptionRemove(channel):
    '''Removes specified channel from subscriptions'''
    for i in data["subscriptions"]:
        if i == channel:
            data["subscriptions"].remove(i)
            return "removed subscription "+i

def subscriptionList():
    '''Lists current subscriptions'''
    return data["subscriptions"] 
