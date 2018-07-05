height = int(input("Your height (cm)? "))
weight = int(input("Your weight (kg)? "))
meter = height / 100
BMI = weight / (meter * meter)

if BMI < 16:
    print ("Severely underweight:(( ")

elif BMI < 18.5:
    print ("Underweight:( ")

elif BMI < 25:
    print ("Normal:) ")

elif BMI < 30:
    print ("Overweight:( ")

else:
    print ("Obese:((( ")
