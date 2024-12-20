def interactive_story_game():
    print("Welcome to the Interactive Story Game!")
    print("You find yourself at a crossroads in a magical forest.")
    print("Choose your path to continue the journey.")

    choice1 = input("Do you want to go 'left' or 'right'? ").lower()

    if choice1 == 'left':
        print("You discover a sparkling river.")
        choice2 = input("Do you want to 'swim' across or 'walk' along the bank? ").lower()
        if choice2 == 'swim':
            print("A magical fish grants you a wish! You win!")
        elif choice2 == 'walk':
            print("You meet a friendly traveler who guides you to safety. You win!")
        else:
            print("You hesitate and get lost. Game over!")
    elif choice1 == 'right':
        print("You encounter a dark cave.")
        choice2 = input("Do you want to 'enter' the cave or 'stay' outside? ").lower()
        if choice2 == 'enter':
            print("Inside the cave, you find hidden treasure! You win!")
        elif choice2 == 'stay':
            print("A wild animal appears, and you run away. Game over!")
        else:
            print("You hesitate and lose your chance. Game over!")
    else:
        print("Invalid choice. The game restarts.")


interactive_story_game()
