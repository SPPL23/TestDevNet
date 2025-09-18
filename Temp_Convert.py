#Dictionary Function   
def dictempCalc():

    print("Dictionary function for Temp Conversion")
    con_Units = input("Choose a conversion method [c-f, f-c, f-k, k-f, c-k, k-c]: ")
    tem_Val = float(input("Enter value: "))

    con_Table = {
        "c-f": (tem_Val * 9 / 5) + 32,
        "f-c": (tem_Val - 32) * 5 / 9,
        "f-k": (tem_Val - 32) * 5 / 9 + 273.15,
        "k-f": (tem_Val - 273.15) * 9 / 5 + 32,
        "c-k": tem_Val + 273.15,
        "k-c": tem_Val - 273.15
    }
    
    if con_Table[con_Units]:
        print(con_Table[con_Units])
    else:
        print("Invalid")

    return(con_Table, con_Units, tem_Val)

if __name__ == "__main__":
    print("TempModule")