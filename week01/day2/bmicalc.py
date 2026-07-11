def bmi(weight:float, height:float) -> float:
    return weight / (height**2)

result = bmi(70,1.75)

print(round(result,2))