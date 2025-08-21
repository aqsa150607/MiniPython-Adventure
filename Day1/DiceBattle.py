import random
import time

ch = "y"

while ch == "y":
    # Generate user and robot dice rolls
    user_dice = random.randint(1, 6)
    robot_dice = random.randint(1, 6)

    # Show rolling effect
    print("\nRolling the dice...")
    time.sleep(0.5)

    # Display results
    print(f"You got: {user_dice}")
    print(f"Robot got: {robot_dice}")
    time.sleep(0.5)

    # Determine round winner
    if user_dice > robot_dice:
        print("🎉 You won this round!")
    elif user_dice < robot_dice:
        print("🤖 Robot won this round!")
    else:
        print("It's a tie!")
    ch = input("Do you want to continue? [Y/n]: ").casefold()

print("See you later thanks for playing!")
