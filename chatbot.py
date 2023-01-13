
import json
import random

def ChatBot():
    # 0: suggestions
    # 1: user commands
    data = json.load(open("./data.json"))
    
    print("Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily.")
    print(f"Suggestions: \nSetting Appointment: {random.choice(data['suggestions']['SetAppointment'])}.\nWant to know existing appointment: {random.choice(data['suggestions']['GetAppointment'])}")
    
    while(True):
        userInput = input("You: ")
        
        pass

ChatBot()