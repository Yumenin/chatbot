
import json
import random

def ChatBot():
    # 0: suggestions
    # 1: user commands
    data = json.load(open("./data.json"))
    
    print("BOT: Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily.\n")
    print(f"Suggestions: \nSetting Appointment: {random.choice(data['suggestions']['SetAppointment'])}.\nCheck existing appointment: {random.choice(data['suggestions']['GetAppointment'])}\n")
    
    while(True):
        userInput = input("You: ")
        if userInput.lower() in (response.lower() for response in data['suggestions']['SetAppointment']):
            print(f"BOT: {random.choice(data['SetAppointment_Responses']['firstResponse'])}")
            print("Please type your full name: \n")
            userName = input("You: ")
            print(f"BOT: {random.choice(data['SetAppointment_Responses']['secondResponse'])}")
            print("")
            break
        elif userInput.lower() in (response.lower() for response in data['suggestions']['SetAppointment']):
            print("check existing appointment")
            break
        else:
            print("Sorry, I do not recognize that command!")
        
        

ChatBot()