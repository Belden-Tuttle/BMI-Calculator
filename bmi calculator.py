print("BMI Calculator")

h= input("Enter height(in): ")
h= float(h)
h= (h*.0254)

w= input("Enter weight(lb): ")
w= float(w)
w= (w*.45)

bmi= (w)/(h*h)

print()

if bmi < 18.5:
    print("BMI:", bmi, " You are underweight.")

if bmi >= 18.5 and bmi <= 24.9:
    print("BMI:", bmi, " You are at a healthy weight.")

if bmi > 24.9 and bmi <30:
    print("BMI:", bmi, " You are overweight.")

if bmi >= 30:
    print("BMI:", bmi, " You are obese.")   
