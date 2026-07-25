def bmi(weight:float, height:float) -> float:
    return weight / (height**2)

def get_bmi_category(bmi: float) -> str:
    
    if bmi <18.5 :
        return "Underweight"
    elif bmi >=18.5 and bmi <=24.9 :
        return "Normal"
    elif bmi >=25 and bmi <=29.9:
        return "Overweight"
    else:
        return "Obese"
    
result = bmi(140,1.75)
print(round(result,2))
print(get_bmi_category(result))
