def calculate_bmi(height,weight):
    print("Height="+ str(height))
    
    print("Weight="+ str(weight))

    bmi = weight/(height ** 2)
    bmi = round(bmi,2)
    if bmi<18.5:
        print("You are under weight")
    elif bmi>=18.5 and bmi<=25.0:
        print("You are normal weight")
    else:
        print("You are overweight")



    return str(bmi)








print("BMI:"+calculate_bmi(1.73,57))
