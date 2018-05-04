#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ka-ui Chu 2018/05/03 @Taiwan
import os
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

TOKEN = os.environ.get('BOT_TOKEN') 
CHANNEL_ID = os.environ.get('FORWARD_CHANNEL_ID') 
PHOTO_FIELD_ID = os.environ.get('PHOTO_FIELD_ID')
SENDPHOTO_CAPTION = os.environ.get("SENDPHOTO_CAPTION")


def sendWelcomeMessage(chat_id):
    if PHOTO_FIELD_ID != None:
        bot.sendPhoto(chat_id, PHOTO_FIELD_ID, SENDPHOTO_CAPTION)


def handle(msg):
    pprint(msg)
    content_type, chat_type, chat_id, date, message_id = telepot.glance(msg, long=True)
    # http://telepot.readthedocs.io/en/latest/reference.html#telepot.Bot.forwardMessage
    bot.forwardMessage(CHANNEL_ID, msg['from']['id'], message_id, disable_notification=True)

    if content_type == "text":
        if msg['text']=="/start":
            sendWelcomeMessage(chat_id)

if __name__ == '__main__':
    if TOKEN==None or CHANNEL_ID==None:
        print("Please set BOT_TOKEN and CHANNEL_ID in os varialbe first")
        exit()

    bot = telepot.Bot(TOKEN)

    MessageLoop(bot, handle).run_as_thread()
    print( '%s (@%s) is Listening ...' % (bot.getMe()['first_name'], bot.getMe()['username']) )
    # Keep the program running.
    while 1:
        time.sleep(10)