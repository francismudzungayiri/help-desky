import random as rd
from datetime import datetime


def ticketing():
    
    chars = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    number = rd.choices(chars, k=7)
    
    ticket_number = ''.join(number)
    
    
    return ticket_number

def getDate():
    today = datetime.today()
    current = today.strftime("%d %b %Y") 
    return current


def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def dateCalculator(today, last):
    todae = datetime(today)
    previous = datetime(last)
    
    num = todae - previous
    result = ''
    if(num == 0):
        result = 'Today'
    elif (num == 1):
        result = 'Yesterday'
    else:
        result = f'{result}days ago'
    
    return result
    
    
    