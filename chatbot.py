
import json
import random
import os
from datetime import datetime
from collections import deque
import secrets
import string


def ChatBot():
    # critical file
    file = open("./data.json")
    data = json.load(file)
    #dataPatients = json.load(open("./patients.json", "a")) if path.exists("patients.json") else json.load(open("./patients.json", "w"))

    print("BOT: Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily\n")
    print(f"Suggestions: \nSetting Appointment: {random.choice(data['Choices']['SetAppointment'])}.\nCheck existing appointment: {random.choice(data['Choices']['GetAppointment'])}\n")
    
    while(True):
        userInput = input("You: ")
        if userInput.lower() in (response.lower() for response in data['Choices']['SetAppointment']):
            print(f"\nBOT: {random.choice(data['SetAppointment_Responses']['firstResponse'])}")
            print("Please type your full name: \n")
            userFullName = input("You: ")

            print(f"\nBOT: {random.choice(data['SetAppointment_Responses']['secondResponse'])}")
            [print(choice, end=", ") for choice in data['Medical_Departments']]
            userChosenDepartment = input("\n\nYou: ")
            while(True):
                if userChosenDepartment.lower() in (choice.lower() for choice in data['Medical_Departments']):
                    break
                print(f"\nBOT: {random.choice(data['Error_Responses_Department'])}")
                userChosenDepartment = input("\nYou: ")

            print(f"\nBOT: {random.choice(data['SetAppointment_Responses']['thirdResponse'])}")
            userContactNumber = input("\nYou: ")
            
            patient = {}
            randomCode = ''.join(secrets.choice(string.ascii_letters + string.digits) for repetitions in range(random.randint(4,10)))

            if os.path.isfile("./patients.json") and os.stat("./patients.json").st_size != 0:
                existingFile = open("./patients.json", "r+")
                rawData = json.load(existingFile)
                queue = deque(rawData['patients'])
                newPatient = {randomCode: {"patientName": userFullName, "patientCheckupDepartment": userChosenDepartment, "userContactNumber": userContactNumber, "userAppointmentCode": randomCode, "DateTime": f"{str(datetime.now())}, {datetime.now().strftime('%H:%M:%S')}"} }
                queue.append(newPatient)
                existingFile.seek(0)
                existingFile.write(json.dumps({"patients": list(queue)}, indent=4))
                existingFile.close()

                # for printing purposes 
                patient['patientAppointmentCode'] = newPatient[randomCode]['userAppointmentCode']
                patient['patientDateTime'] = newPatient[randomCode]['DateTime']
            else:
                queue = deque([])
                queue.append({randomCode: {"patientName": userFullName, "patientCheckupDepartment": userChosenDepartment, "userContactNumber": userContactNumber, "userAppointmentCode":
                 randomCode, "DateTime": f"{str(datetime.now())}, {datetime.now().strftime('%H:%M:%S')}"}})
                newPatientsData = open("patients.json", "w")
                newPatientsData.write(json.dumps({"patients": list(queue)}, indent=4))
                newPatientsData.close()

                # for printing purposes 
                patient['patientAppointmentCode'] = queue[0][randomCode]['userAppointmentCode']
                patient['patientDateTime'] = queue[0][randomCode]['DateTime']
                
            
            print(f"Your appointment has been processed. Your appointment code # is {patient['patientAppointmentCode']}")
            print(f"Your scheduled appointment date is {patient['patientDateTime']}")
            # appointment number here
            print("Thank you for using our service. Have a great day!\n")
        elif userInput.lower() in (response.lower() for response in data['Choices']['SetAppointment']):
            print("check existing appointment")
            break
        elif userInput.lower() in (response.lower() for response in data['Choices']['ExitProgram']):
            print("Exiting program. Thank you for using our service!")
            break
        else:
            print("\nSorry, I do not recognize that command!")
    file.close()
    
        
        

ChatBot()