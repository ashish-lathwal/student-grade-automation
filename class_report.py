import json
from class_info import json_file_name
import os

txt_result = "result.txt"
grade_division = {
    "A":"80-100",
    "B":"60-79",
    "C":"40-59",
    "D":"20-39",
    "E":"0-19"
}


def writeGrade(grade:str,grade_list:list,content:dict,file_name:str = None):
    file_name = file_name if file_name is not None else txt_result 
    try:
        with open(file_name,"a") as f:
            heading1 = "Student name"
            heading2 = "Student marks"

            f.write("\n" + "=" * 40 +"\n")
            f.write(f"{grade} GRADE ({grade_division[grade]})marks - {len(grade_list)} students\n")
            f.write("="*40 + "\n\n")

            f.write(f"{heading1:20} | {heading2}\n")
            f.write("-" * 21 + "|" + "-" * 21 + "\n")

            sorted_grade_list = sorted(grade_list,key=lambda x:content[x], reverse=True)
            for student in sorted_grade_list:
                f.write(f"{student:_<20} | {content[student]}\n")
            f.write("\n")

            print(f"Success writing {grade} grade to {file_name}")
    
    except Exception as e:
        print(f"Error happened writing {grade} grade to {file_name} ")

txt_result = "result.txt"

os.chdir(os.path.dirname(os.path.abspath(__file__)))
content = ""
#print(info.marks)
print(json_file_name)
try:
    with open(json_file_name,"r") as f:
        content = json.load(f)
        print("Content loaded successfully from 'class_info.json' to 'content'")
except Exception as e:
    print("ERROR while loading 'class_info.json' to 'content'")

total_students = 0
total_score = 0
top_score = 0
top_scorer = []
bottom_score = 100
bottom_scorer = []
gradeA_students = []
gradeB_students = []
gradeC_students = []
gradeD_students = []
gradeE_students = []

for key,value in content.items():
    total_score += value
    total_students +=1

    if value > top_score:
        top_scorer = []
        top_score = value
        top_scorer.append(key)
    elif value == top_score:
        top_scorer.append(key)
    
    if value < bottom_score:
        bottom_score = value
        bottom_scorer = []
        bottom_scorer.append(key)
    elif value == bottom_score:
        bottom_scorer.append(key)

    if value >= 80:
        gradeA_students.append(key)
    elif value >= 60:
        gradeB_students.append(key)
    elif value >= 40:
        gradeC_students.append(key)
    elif value >=20:
        gradeD_students.append(key)
    else:
        gradeE_students.append(key)

average = total_score/(total_students)

try:
    with open(txt_result,"w") as f:
        f.write("\n" + "=" * 40 + "\n")
        f.write("Result summary of class1\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Total marks = {total_score}\n")
        f.write(f"Total students = {total_students}\n")
        f.write(f"Average marks are = {average}\n\n")

        if len(top_scorer) == 1:
            f.write(f"Top scorer is {top_scorer[0]} with {top_score} marks\n")
        else:
            top_scorer_str = ", ".join(top_scorer)
            f.write(f"Top scorers are {top_scorer_str} with {top_score} marks\n")

        if len(bottom_scorer) == 1:
            f.write(f"Bottom scorer is {bottom_scorer[0]} with {bottom_score} marks\n")
        else:
            bottom_scorer_str = ", ".join(bottom_scorer)
            f.write(f"Bottom scorers are {bottom_scorer_str} with {bottom_score} marks\n\n")
        

except Exception as e:
    print(f"ERROR ocured while writing in {txt_result} file")

writeGrade("A",gradeA_students,content)
writeGrade("B",gradeB_students,content)
writeGrade("C",gradeC_students,content)
writeGrade("D",gradeD_students,content)
writeGrade("E",gradeE_students,content)
