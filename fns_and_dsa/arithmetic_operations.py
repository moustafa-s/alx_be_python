def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return float(num1) + float(num2)
        case "subtract":
            return float(num1) - float(num2)
        case "multiply":
            return float(num1) * float(num2)
        case "divide":
            if num2 != 0:
                return float(num1) / float(num2)
            else:
                return print("can not divide by zero")
