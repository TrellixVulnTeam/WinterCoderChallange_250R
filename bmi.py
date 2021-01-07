
import random

weight = int(input("Please write your mass (kg): "))
height = float(input("Please write your height (m): "))
bmi = weight/(height*height)
time_for_exercise = []
if bmi <= 18.5:
     result = print('Your BMI is', bmi, 'which means you are underweight.')
     time_for_exercise = [4,5,6]
elif bmi > 18.5 and bmi < 25:
     result =print('Your BMI is', bmi, 'which means you have normal weight.')
     time_for_exercise = [7,8,9]
elif bmi > 25 and bmi < 30:
     result =print('Your BMI is', bmi, 'which means you are overweight.')
     time_for_exercise = [10,11,12]
elif bmi > 30 and bmi < 35:
     result =print('Your BMI is', bmi, 'which means you are obese (class I).')
     time_for_exercise = [13,14,15]
elif bmi > 35 and bmi < 40:
     result =print('Your BMI is', bmi, 'which means you are obese (class II).')
     time_for_exercise = [16,17,18]
elif bmi > 40:
     result =print('Your BMI is', bmi, 'which means you are obese (class III).')
     time_for_exercise = [19,20,21]
else:
    result = print('There is an error with your input')
    time_for_exercise = [22,23,24]

physical_activities = ['running', 'swimming', 'hiking', 'biking']

day = f" {result} You should try {random.choice(physical_activities)} for {random.choice(time_for_exercise)}  minutes"
print(day)
training_txt_file = open("training_plan.txt","w+")
training_txt_file.write(f" {result} You should try {random.choice(physical_activities)} for {random.choice(time_for_exercise)}  minutes")
training_txt_file.close()