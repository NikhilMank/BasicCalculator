from utils import *


if __name__ == "__main__":  
    help()
    print("Enter your calculations below:")
    print("If you want to use result from previous calculation, use 'ans' as variable in next expression.")
    ans = None
    while True:
        try:
            expression = input("Enter calculation (or 'exit' to quit or 'help' to see usage)\nUse 'ans' to use result from previous calculation: ")   # Take user input for calculations
            expression = expression.lower()
            if expression.strip() == 'exit':
                break
            elif expression.strip() == 'help':
                help()
            else:
                if ans is not None:
                    if 'div(' in expression:
                        func_args=expression[expression.find('(')+1:expression.find(')')].split(',')
                        a = ans if func_args[0].strip()=='ans' else float(func_args[0].strip())
                        b = ans if func_args[1].strip()=='ans' else float(func_args[1].strip())
                        ans = div(a,b,ans)
                    else:
                        ans = eval(expression)  # Evaluates the expression string as a line of code
                else:
                    ans = eval(expression)
                print(f"Result: {ans}")
        except Exception as e:
            print(f"Error: {e}")
    print("Calculator session closed.")