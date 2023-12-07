#calculating average of two numbers
def calcaverage(num1,num2):
    return (num1 + num2)/2


#converting celcius to fahrenriete
def Cel_to_Fah(Tc):
    Tf = (Tc * 9/5) + 32
    return (Tf)

#coverting fahrenriete to celcius
def Fah_to_Cel(Tf):
    Tc = (Tf - 32) * (5/9)
    return Tc

#calculating the ages of people
def calculate_age(year_of_birth):
    current_year = 2023
    age = current_year - year_of_birth
    return age

#Area of a Triangle
def calculate_triangle_area(base,height):
    area = 0.5 * base * height
    return area


        