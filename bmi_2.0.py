height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

calculate = int(weight) / (float(height)**2)
result = round(calculate, 1)

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result > 18.5 and result < 25:
    print(f"Your BMI is {result:.1f}, you have a normal weight.")
elif result >= 25 and result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result >= 30 and result < 35:
    print(f"Your BMI is {result}, you are obese.")
elif result >= 35:
    print(f"Your BMI is {result}, you are clinically obese.")