import random
def game():
    low = 1
    high = 100
    try_count = 10
    goal_number = random.randint(low, high)

    while True:
        try_count -= 1
        user_guess = int(input("Guess a number between 1 and 100: \n\n"))
        if user_guess == goal_number:
            print(f"You guessed right!  your try count: {10-try_count}")
            break
        elif user_guess < goal_number:
            print("Too low!")
        else:
            print("Too high!")

        if try_count == 0:
            print("You Lose!")
            break

def main():
    game()

if __name__ == '__main__':
    main()
