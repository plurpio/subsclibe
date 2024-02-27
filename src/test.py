import main
import os

data = main.subscriptions.subscriptionFetch()

video = data[int(input("Input video order id thingy idk "))][0]

os.system("mpv https://youtu.be/"+video)

#data = main.subscriptions.channelFetch(main.channel.channelID("mrbeast"))
#for i in data:
#    print("\n\nVideo ID:", i[0])
#    print("Title:", i[1])
#    print("Channel:", i[2])
#    print("Time:", i[3])
#    print("Description:", i[4])
