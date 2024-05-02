def calculate_bmi(height,weight):
    print("Height="+ str(height))
    
    print("Weight="+ str(weight))

    bmi = weight/(height ** 2)
    bmi = round(bmi,2)
    if bmi<18.5:
        print("You are under weight")
        return -1
    elif bmi>=18.5 and bmi<=25.0:
        print("You are normal weight")
        return 0
    else:
        print("You are overweight")
        return 1











print("BMI:"+str(calculate_bmi(1.73,57)))
