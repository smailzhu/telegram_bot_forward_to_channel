#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ka-ui Chu 2018/05/03 @Taiwan
import os
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

TOKEN = os.environ.get('BOT_TOKEN') 
#os.environ["BOT_TOKEN"] = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
CHANNEL_ID = os.environ.get('FORWARD_CHANNEL_ID') 
#os.environ["FORWARD_CHANNEL_ID"] = "CHANEEL_ID"

def handle(msg):
    content_type, chat_type, chat_id, date, message_id = telepot.glance(msg, long=True)
    # http://telepot.readthedocs.io/en/latest/reference.html#telepot.Bot.forwardMessage
    bot.forwardMessage(CHANNEL_ID, msg['from']['id'], message_id, disable_notification=True)


if __name__ == '__main__':
    if TOKEN==None or CHANNEL_ID==None:
        print("Please set Bot Token and Channel ID in os varialbe first")
        exit()

    bot = telepot.Bot(TOKEN)

    MessageLoop(bot, handle).run_as_thread()
    print( '%s (@%s) is Listening ...' % (bot.getMe()['first_name'], bot.getMe()['username']) )
    # Keep the program running.
    while 1:
        time.sleep(10)