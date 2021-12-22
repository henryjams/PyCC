# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:16:57 2021

@author: Hank
"""

def send_messages(messages):
    while unsent_msg:
        working = unsent_msg.pop()
        print(working)
        sent_msg.append(working)
        
unsent_msg = ['yo holmes', 'smell ya later', 'bite my shiny metal ass']
sent_msg = []

send_messages(unsent_msg)
print(unsent_msg)
print(sent_msg)