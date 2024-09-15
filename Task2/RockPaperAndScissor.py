import random as ra
if __name__ == '__main__':
    print('''Welcome to the game!
    Let's play Rock, Paper and Scissors!
    Type Rock for Rock, Paper for Paper and Scissors for Scissors.
    To end the game just type END!
    ''')
    u_count = 0
    c_count = 0
    while True:
        user = input("What are you going to throw! ").lower()
        computer = ra.randrange(1,3) # 1. is going to be rock, 2. is paper and 3. is scissors

        match user:
            case 'rock':
                if computer == 1:
                    print(f'''It's a tie! We both selected Rock
                    Score
                    You: {u_count} and Computer: {c_count}''')
                elif computer == 3:
                    u_count += 1
                    print(f'''You won!
                    Score
                    You: {u_count} and Computer: {c_count}''')

                else:
                    c_count += 1
                    print(f'''You loose!
                    Score
                    You: {u_count} and Computer: {c_count}''')

            case 'paper':
                if computer == 2:
                    print(f'''It's a tie! you both selected Paper
                                Score
                                You: {u_count} and Computer: {c_count}''')
                elif computer == 1:
                    u_count += 1
                    print(f'''You won!
                                Score
                                You: {u_count} and Computer: {c_count}''')

                else:
                    c_count += 1
                    print(f'''You loose!
                                Score
                                You: {u_count} and Computer: {c_count}''')

            case 'scissors':
                if computer == 3:
                    print(f'''It's a tie! you both selected Scissors
                                Score
                                You: {u_count} and Computer: {c_count}''')
                elif computer == 2:
                    u_count += 1
                    print(f'''You won!
                                Score
                                You: {u_count} and Computer: {c_count}''')

                else:
                    c_count += 1
                    print(f'''You loose!
                                Score
                                You: {u_count} and Computer: {c_count}''')

            case 'end':
                if u_count>c_count:
                    print("You are a God at this game!")
                    break
                elif c_count>u_count:
                    print("Hehe! I Won.")
                    break
                else:
                    print("Let's play some other time too!")
                    break
            case _:
                print("Type the correct option!")