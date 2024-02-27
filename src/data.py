import json

print("Loading subscription file...")
try:
    with open("subscriptions.json", "r") as f:
        data = json.load(f)
        print("Loaded subscription file.")
except:
    with open("subscriptions.json", "w+") as f:
        data = { "subscriptions": [] }
        json.dump(data, f)
        data = json.dumps(data)
        data = json.loads(data)
        print("Subscription file not present, generated one.")



def subscriptionWrite():
    try:
        with open("subscriptions.json", "w") as f:
            json.dump(data, f)
    except:
        return "writing failed"


def subscriptionAdd(channel):
    if len(channel) == 24:
        data["subscriptions"].append(channel)
        return "added channel "+channel+" successfully"
    else:
        return "need channel id"



def subscriptionRemove(channel):
    for i in data["subscriptions"]:
        if i == channel: 
            data["subscriptions"].remove(i)
            break

def subscriptionList():
    return data["subscriptions"] 
