
import json
import random
import os.path as path
from collections import deque
import secrets
import string

def ChatBot():
    
    # critical file
    data = json.load(open("./data.json"))
    #dataPatients = json.load(open("./patients.json", "a")) if path.exists("patients.json") else json.load(open("./patients.json", "w"))

    print("BOT: Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily.\n")
    print(f"Suggestions: \nSetting Appointment: {random.choice(data['Choices']['SetAppointment'])}.\nCheck existing appointment: {random.choice(data['Suggestions']['GetAppointment'])}\n")
    
    while(True):
        userInput = input("You: ")
        if userInput.lower() in (response.lower() for response in data['Suggestions']['SetAppointment']):
            print(f"\nBOT: {random.choice(data['SetAppointment_Responses']['firstResponse'])}")
            print("Please type your full name: \n")
            userFullName = input("You: ")

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
            
            randomCode = ''.join(secrets.choice(string.ascii_letters + string.digits) for repetitions in range(random.randint(4,10)))
            if path.exists('patients.json'):
                queue = deque([])
                queue.append({"patientName": userFullName, "patientCheckupDepartment": userChosenDepartment, "userContactNumber": userContactNumber, "userAppointmentCode": randomCode})
                newPatientsData = open("patients.json", "w")
                newPatientsData.write(json.dumps(list(queue)))
                newPatientsData.close()
            else:
                existingFile = open("patients.json", "+")
                queue = deque(json.load(existingFile))
                HeadDate = queue[0]['DateTime']
                queue.append({"patientName": userFullName, "patientCheckupDepartment": userChosenDepartment, "userContactNumber": userContactNumber, "userAppointmentCode": randomCode})
                pass
            break
        elif userInput.lower() in (response.lower() for response in data['Suggestions']['SetAppointment']):
            print("check existing appointment")
            break
        else:
            print("\nSorry, I do not recognize that command!")

    data.close()
        
        

ChatBot()