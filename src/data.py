import json

#data = open("subscriptions.json")
#data = json.load(data)

def subscriptionAdd(channel):
    data["subscriptions"]
    new_subscription = {"channel": channel}
    data["subscriptions"].append(new_subscription)


def subscriptionRemove(channel):
    for i in data["subscriptions"]:
        if i["channel"] == channel:
            data["subscriptions"].remove(i)
            break
    else:
        return "channel not subscribed to"


def subscriptionWrite():
    with open("subscriptions.json", "w") as f:
        json.dump(data, f)


def subscriptionList():
    return [] # just for testing before data management is put in
