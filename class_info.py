import random
import os
import json

json_file_name = "class_info.json"

def change_directory_to_this_file():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

def json_dump(file,content):
    try:
        with open(file,"w") as f:
            json.dump(content,f,indent=4)
            print(f"successfully 'dumped' content in {file}")
    except Exception as e:
        print(f"Error while dumping in {file} : {e}")


    

marks = [random.randint(0,100) for _ in range(100)]

students = [
    "Emma Johnson", "Liam Smith", "Olivia Garcia", "Noah Williams", "Ava Brown",
    "Ethan Jones", "Sophia Miller", "Lucas Davis", "Isabella Rodriguez", "Mason Martinez",
    "Mia Hernandez", "Elijah Lopez", "Charlotte Gonzalez", "Oliver Wilson", "Amelia Anderson",
    "Aiden Thomas", "Harper Taylor", "James Moore", "Evelyn Jackson", "Benjamin Martin",
    "Abigail Lee", "Alexander Perez", "Emily Thompson", "Daniel White", "Elizabeth Harris",
    "Michael Sanchez", "Sofia Clark", "Henry Ramirez", "Victoria Lewis", "Jackson Walker",
    "Madison Robinson", "Sebastian Young", "Chloe Allen", "Matthew King", "Ella Wright",
    "David Scott", "Grace Green", "Joseph Baker", "Lily Adams", "Samuel Nelson",
    "Natalie Hill", "John Carter", "Zoe Mitchell", "Jonathan Perez", "Leah Roberts",
    "Nathan Turner", "Hannah Phillips", "Ryan Campbell", "Layla Parker", "Christian Evans",
    "Audrey Edwards", "Julian Collins", "Claire Stewart", "Isaac Sanchez", "Sarah Morris",
    "Joshua Rogers", "Anna Reed", "Andrew Cook", "Samantha Morgan", "Gabriel Bell",
    "Aria Murphy", "Dylan Bailey", "Lucy Rivera", "Caleb Cooper", "Ellie Richardson",
    "Jack Cox", "Stella Howard", "Luke Ward", "Violet Torres", "Adam Peterson",
    "Skylar Gray", "Connor Ramirez", "Penelope James", "Nathan Watson", "Brooklyn Brooks",
    "Hunter Kelly", "Savannah Sanders", "Cameron Price", "Caroline Bennett", "Thomas Wood",
    "Nora Barnes", "Landon Ross", "Mila Henderson", "Jordan Coleman", "Lillian Jenkins",
    "Julian Perry", "Paisley Powell", "Eli Long", "Nova Patterson", "Nicholas Hughes",
    "Eleanor Flores", "Ezra Washington", "Aubrey Butler", "Angel Simmons", "Elena Foster",
    "Levi Gonzales", "Maya Bryant", "Isaac Alexander", "Kinsley Russell", "Owen Griffin"
]

class_info = dict(zip(students,marks))
change_directory_to_this_file()
json_dump(file=json_file_name,content=class_info)


