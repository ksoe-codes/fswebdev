print('BMI Calculator: ')
height = float(input('\nEnter Height in m: '))
weight = float(input('\nEnter Weight in kg: '))

bmi = weight/(height*height)

print("Your BMI is " + str(bmi))
if bmi < 18.5:
    print(" You are underweight.")
elif bmi >= 18.5 and bmi <25:
    print(" You have normal weight.")
elif bmi > 25 and bmi < 30:
    print(" You are overweight.")
elif bmi > 30 and bmi < 35:
    print(" You are obese.")
elif bmi > 35:
    print(" You are clinically obese.")