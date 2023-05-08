print('BMI Calculator: ')
height = float(input('\nEnter Height in m: '))
weight = float(input('\nEnter Weight in kg: '))

bmi = weight/(height*height)

print("BMI for \n Height = " + str(height) + "\n Weight = " + str(weight) + " is\n BMI = " +  str(bmi) + ".")
