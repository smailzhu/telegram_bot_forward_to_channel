#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('FORWARD_CHANNEL_ID')
def handle(msg):
    content_type, chat_type, chat_id, date, message_id = telepot.glance(msg, long=True)
    # http://telepot.readthedocs.io/en/latest/reference.html#telepot.Bot.forwardMessage

bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)