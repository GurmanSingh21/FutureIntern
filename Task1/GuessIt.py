import random
if __name__ == '__main__':

    random_number = random.randrange(1,100)
    count = 0
    while True:
        num = int(input("Guess the number: "))
        if num == random_number:
            print(f"You got it!!, you took {count+1} tries.")
            break
        elif num == random_number and count == 0:
            print("BullsEye!!!!")
            break
        elif random_number-10 <= num < random_number:
            print("You are close a little higher!")
            count +=1
        elif random_number<num<=random_number+10:
            print("Ahh! Go a little low.")
            count += 1
        elif num<random_number-10:
            print("You are very low!")
            count += 1
        else:
            print("You are very high!!")
            count += 1