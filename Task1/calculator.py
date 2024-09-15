if __name__ == '__main__':
    num_1 = int(input('Enter a Number: '))
    while True:
        oper = input('''What Operation do you want?
        For Addition : +
        For Subtraction: -
        For Multiplication: *
        For Division: /
        To Get result: =
        ''')

        match oper:
            case '+':
                num_2 = int(input('Enter the number: '))
                num_1 += num_2
            case '-':
                num_2 = int(input('Enter the number: '))
                num_1 -= num_2
            case '*':
                num_2 = int(input('Enter the number: '))
                num_1 *= num_2
            case '/':
                num_2 = int(input('Enter the number: '))
                num_1 /= num_2
            case '=':
                break
            case _:
                print("Wrong Choice Input:")
    print(f"The result is {num_1}")