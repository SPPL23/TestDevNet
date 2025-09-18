print("If function for Temp Conversion")
tem_Unit1 = input("Choose a unit needed to be convert [Celsius, Fahrenheit, Kelvin]: ")
tem_Val1 = float(input(f"Enter value for {tem_Unit1}: "))
tem_Unit2 = input(f"{tem_Val1} {tem_Unit1} to be converted to [Celsius, Fahrenheit, Kelvin]: ")

#if Function
def tempCalc(tem_Unit1, tem_Val1, tem_Unit2):
    #C to F
    if tem_Unit1 == "Celcius" or tem_Unit1 == "C" and tem_Unit2 == "Fahrenheit" or tem_Unit2 == "F":
        con_Vert = (tem_Val1 * 9 / 5) + 32
        print(con_Vert)
    #F to C
    elif tem_Unit1 == "Fahrenheit" or tem_Unit1 == "F" and tem_Unit2 == "Celcius" or tem_Unit2 == "C":
        con_Vert = (tem_Val1 - 32) * 5 / 9
        print(con_Vert)
    #C to K
    elif tem_Unit1 == "Celsius" or tem_Unit1 == "C" and tem_Unit2 == "Kelvin" or tem_Unit2 == "K":
        con_Vert = tem_Val1 + 273.15
        print(con_Vert)
    #K to C
    elif tem_Unit1 == "Kelvin" or tem_Unit1 == "K" and tem_Unit2 == "Celcius" or tem_Unit2 == "C":
        con_Vert = tem_Val1 - 273.15
        print(con_Vert)
    #F to K
    elif tem_Unit1 == "Fahrenheit" or tem_Unit1 == "F" and tem_Unit2 == "Kelvin" or tem_Unit2 == "K":
        con_Vert = (tem_Val1 - 32) * 5 / 9 + 273.15
        print(con_Vert)
    #K to F
    elif tem_Unit1 == "Kelvin" or tem_Unit1 == "K" and tem_Unit2 == "Fahrenheit" or tem_Unit2 == "F":
        con_Vert = (tem_Val1 - 273.15) * 9 / 5 + 32
        print(con_Vert)
    else:
        print(f"Cannot calculate {tem_Unit1} to {tem_Unit2}")

    return(tem_Unit1, tem_Val1, tem_Unit2)