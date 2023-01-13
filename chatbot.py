
import json
import random

def ChatBot():
    
    # critical file
    data = json.load(open("./data.json"))
    
    print("BOT: Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily.\n")
    print(f"Suggestions: \nSetting Appointment: {random.choice(data['Choices']['SetAppointment'])}.\nCheck existing appointment: {random.choice(data['Suggestions']['GetAppointment'])}\n")
    
    while(True):
        userInput = input("You: ")
        if userInput.lower() in (response.lower() for response in data['Suggestions']['SetAppointment']):
            print(f"\nBOT: {random.choice(data['SetAppointment_Responses']['firstResponse'])}")
            print("Please type your full name: \n")
            userName = input("You: ")

            print(f"\nBOT: {random.choice(data['SetAppointment_Responses']['secondResponse'])}")
            [print(choice, end=", ") for choice in data['Medical_Departments']]
            userChosenDepartment = input("You: ")
            while(True):
                if userChosenDepartment.lower() in (choice.lower() for choice in data['Medical_Departments']):
                    break
                print(f"BOT: {random.choice(data['Error_Responses_Department'])}")
                userChosenDepartment = input("You: ")

            print(f"BOT: {random.choice(data['SetAppointment_Responses']['thirdResponse'])}")
            userContactNumber = input("You: ")
            
            break
        elif userInput.lower() in (response.lower() for response in data['Suggestions']['SetAppointment']):
            print("check existing appointment")
            break
        else:
            print("\nSorry, I do not recognize that command!")
        
        

ChatBot()