from utils import *


if __name__ == "__main__":  
    help()
    print("Enter your calculations below:")
    print("If you want to use result from previous calculation, use 'ans' as variable in next expression.")
    
    while True:
        try:
            expression = input("Enter calculation (or 'exit' to quit or 'help' to see usage): ")   # Take user input for calculations
            if expression.lower() == 'exit':
                break
            elif expression.lower() == 'help':
                help()
            else:
                ans = eval(expression)  # Evaluates the expression string as a line of code
                print(f"Result: {ans}")
        except Exception as e:
            print(f"Error: {e}")
    print("Calculator session closed.")