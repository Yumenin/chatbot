
import json
import random
import os
from datetime import datetime
from datetime import date
from collections import deque
import secrets
import string

def genRandomDate():
    return datetime(2023, 1, random.randint(date.today().day, 28), hour=random.randint(12, 18), minute=random.randint(0, 30))

def ChatBot():
    # critical file
    file = open("./data.json")
    data = json.load(file)
    #dataPatients = json.load(open("./patients.json", "a")) if path.exists("patients.json") else json.load(open("./patients.json", "w"))
    print("\n======================  E-KonsultaMo Bot  ========================================")
    print("============================================================================")
    print(f"\nSetting Appointment Commands: {data['Choices']['SetAppointment']}\n\nGetting Appointment Commands: {data['Choices']['GetAppointment']}")
    print("============================================================================")
    # print(f"\nSuggestions: \nSetting Appointment: {random.choice(data['Choices']['SetAppointment'])}.\nCheck existing appointment: {random.choice(data['Choices']['GetAppointment'])}\n")
    
    # print("BOT: Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily.\n")
    # print("BOT: Please type an appropriate command to start something.\n")
    while(True):
        print("BOT: Hello there! I am a bot designed to help you schedule appointments with your doctor quickly and easily.\n")
        print("BOT: Please type an appropriate command to start something.\n")
        print(f"\nSuggestions: \nSetting Appointment: {random.choice(data['Choices']['SetAppointment'])}.\nCheck existing appointment: {random.choice(data['Choices']['GetAppointment'])}\n")
        userInput = input("You: ")
        if userInput.lower() in [response.lower() for response in data['Choices']['SetAppointment']]:

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
                newPatient = {randomCode: {"patientName": userFullName, "patientCheckupDepartment": userChosenDepartment, "userContactNumber": userContactNumber, "userAppointmentCode": randomCode, "DateTime": f"{genRandomDate()}"} }
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
                 randomCode, "DateTime": f"{genRandomDate()}"}})
                newPatientsData = open("patients.json", "w")
                newPatientsData.write(json.dumps({"patients": list(queue)}, indent=4))
                newPatientsData.close()

                # for printing purposes 
                patient['patientAppointmentCode'] = queue[0][randomCode]['userAppointmentCode']
                patient['patientDateTime'] = queue[0][randomCode]['DateTime']
                
            print(f"BOT: Your appointment has been processed. Your appointment code # is {patient['patientAppointmentCode']}\n")
            print(f"BOT: Your scheduled appointment date is {patient['patientDateTime']}\n")
            # appointment number here
            print("BOT: Returning you back to the original state.\n")

        elif userInput.lower() in [response.lower() for response in data['Choices']['GetAppointment']]:
            patientsFile = None
            patientsData = None
            try:
                patientsFile = open("./patients.json")
            except FileNotFoundError:
                print('\nBOT: Patients.json does not exist yet in current directory.')
                print("\nBOT: Make an appointment first to start using this functionality.\n")
                continue

            patientsData = json.load(patientsFile)
            print(f"\nBOT: {random.choice(data['GetAppointment_Responses'])}:\n")
            appointmentCode = input("You: ")

            if len([patient for patient in patientsData['patients'] if appointmentCode in patient.keys()]):

                print("\nBOT: Existing Appointment Details Found.\n")
                patientAppointmentDetails = [patient for patient in patientsData['patients'] if appointmentCode in patient.keys()][0]
                print("=== Appointment Details ===")
                print(f"Patient Name: {patientAppointmentDetails[appointmentCode]['patientName']}")
                print(f"Patient Department: {patientAppointmentDetails[appointmentCode]['patientCheckupDepartment']}")
                print(f"Appointment Time: {patientAppointmentDetails[appointmentCode]['DateTime']}")
                print(f"Your appointment number is {patientsData['patients'].index(patientAppointmentDetails) + 1}\n")
                input("Press anything to continue...\n")
                print("BOT: Returning you back to the original state.")
                print()
            else:
                print("BOT: No appointment code found, returning you to the state prior to execution of the command.\n")
                continue
        elif userInput.lower() in [response.lower() for response in data['Choices']['ExitProgram']]:
            print("\nBOT: Exiting program. Thank you for using our service!\n")
            break
        else:
            print(f"\nBOT: {random.choice(data['UnrecognizedCommand_Responses'])}\n")
    file.close()



ChatBot()
