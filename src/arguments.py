"Handles arguments given to main.py"

import json
import re
import sys

import data

argHelp = """
Subsclibe - A simple CLI application to manage and view subscriptions on Youtube.

ARGUMENTS
subsclibe - Launch Subsclibe Normally.
subsclibe help - Shows this help screen.

subsclibe convert piped (FILE) - Converts a Piped subscription file to Subsclibe
                  invidious (FILE) - Converts a Invidious subscription file to Subsclibe
"""


def args(args):
    print("Started with arguments:", args)
    if len(args) == 1: return

    if args[1] == "convert" and len(args) == 4:
        if args[2] == "piped":
            try:
                with open(args[3], "r", encoding='utf-8') as f:
                    jsondata = json.load(f)
                    for i in jsondata["subscriptions"]:
                        print("Found subscription:", re.findall(r"https:\/\/www\.youtube\.com\/channel\/(.*)", i["url"])[0])
                        data.subscriptionAdd(re.findall(r"https:\/\/www\.youtube\.com\/channel\/(.*)", i["url"])[0])
            except:
                print("invalid file")

        elif args[3] == "invidious":
            try:
                with open(args[3], "r", encoding='utf-8') as f:
                    jsondata = json.load(f)
                    for i in jsondata["subscriptions"]:
                        print("Found subscription:", i)
                        data.subscriptionAdd(i)
            except:
                print("invalid file")
        data.subscriptionWrite()
        sys.exit()

    else:
        print(argHelp)
        sys.exit()
