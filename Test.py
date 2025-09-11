x = 0;
y = 0;
operator = 0;
result = 0;

while True:
    def calc(operator, x, y, result):
        x = int(input("Enter first number: "));
        y = int(input("Enter 2nd number: "));
        operator = str(input("Enter operator: "));
        result = 0;
        
        match operator:
            case "+":
                result = x + y;
                print(result);
            case "-":
                result = x - y;
                print(result);
            case "*":
                result = x * y;
                print(result);
            case "/":
                result = x / y;
                print(result);
            case "%":
                result = x & y;
                print(result);
            case _:             
                print("");
    break;
            
calc(operator, x, y, result);