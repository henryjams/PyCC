# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:33:50 2021

@author: Hank
"""

def show_messages(unsent_messages):
    print(f"Printing messages:")
    for message in unsent_messages:
        print(unsent_messages)
        
def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        print("\nSending messages:")
        working_message = unsent_messages.pop()
        print(working_message)
        sent_messages.append(working_message)
        
unsent_messages = ['this messages is long', 'this is short', 'what about me?']
sent_messages = []

show_messages(unsent_messages)

send_messages(unsent_messages[:], sent_messages)

print("\nFinal list of messages:")
print(unsent_messages)
print(sent_messages)
    