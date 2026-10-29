# my first Adventure Game in Python programming language


def start_game():
    """Display game introduction and get player name."""
    print("\n" + "=" * 50)
    print("       WELCOME TO THE ADVENTURE GAME!")
    print("=" * 50)
    print("\nYou wake up in a mysterious land with two paths ahead.")
    print("One leads to a dark, ancient forest.")
    print("The other leads to a mysterious cave entrance.")
    print("\n" + "-" * 50)
    
    # Ask for player's name
    player_name = input("What is your name, adventurer? ")
    print(f"\nWelcome, {player_name}! Your journey begins now...")
    print("-" * 50)
    
    # Provide initial choice
    print("\nChoose your path:")
    print("1. Explore the dark forest")
    print("2. Enter the mysterious cave")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ")
        if choice == "1":
            print("\nYou venture into the dark forest...")
            return "forest"
        elif choice == "2":
            print("\nYou enter the mysterious cave...")
            return "cave"
        else:
            print("Invalid choice. Please enter 1 or 2.")


def forest_path():
    """Handle the forest scenario with player choices."""
    print("\n" + "=" * 50)
    print("          THE DARK FOREST")
    print("=" * 50)
    print("\nYou enter the dark, ancient forest.")
    print("Tall trees block out most of the sunlight.")
    print("You hear the sound of running water nearby.")
    print("\nSuddenly, you come to a fork in the path!")
    print("-" * 50)
    
    # Provide choices
    print("\nYou have two options:")
    print("1. Follow the sound of the river")
    print("2. Climb a tall tree to get a better view")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ")
        
        if choice == "1":
            print("\nYou follow the sound of the river...")
            print("You find a beautiful stream with sparkling water!")
            print("Along the bank, you discover a small boat.")
            print("\nCongratulations! You found a safe way through the forest.")
            return "river"
        elif choice == "2":
            print("\nYou climb the tall tree...")
            print("From the top, you see a nest with golden eggs!")
            print("But the branch starts to crack under your weight...")
            print("\nYou quickly climb down and take the golden eggs!")
            print("Congratulations! You found treasure in the forest!")
            return "tree"
        else:
            print("Invalid choice. Please enter 1 or 2.")


def cave_path():
    """Handle the cave scenario with player choices."""
    print("\n" + "=" * 50)
    print("          THE MYSTERIOUS CAVE")
    print("=" * 50)
    print("\nYou enter the mysterious cave.")
    print("It's dark and cold. Water drips from the ceiling.")
    print("You can barely see ahead of you.")
    print("\nYou feel something on the ground near your feet...")
    print("-" * 50)
    
    # Provide choices
    print("\nYou have two options:")
    print("1. Light a torch and see what's around you")
    print("2. Proceed carefully in the dark")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ")
        
        if choice == "1":
            print("\nYou light a torch...")
            print("The flame illuminates the cave!")
            print("You see ancient paintings on the walls!")
            print("And there's a treasure chest in the corner!")
            print("\nCongratulations! You discovered ancient treasure!")
            return "torch"
        elif choice == "2":
            print("\nYou proceed carefully in the dark...")
            print("You stumble but keep moving forward.")
            print("Suddenly, you feel a cool breeze ahead!")
            print("You find an exit that leads to a beautiful garden!")
            print("\nCongratulations! You found your way out safely!")
            return "dark"
        else:
            print("Invalid choice. Please enter 1 or 2.")


def main():
    """Main game loop to run the adventure game."""
    while True:
        # Start the game
        choice = start_game()
        
        if choice == "forest":
            forest_path()
        elif choice == "cave":
            cave_path()
        
        # Ask if player wants to restart
        print("\n" + "=" * 50)
        restart = input("Would you like to play again? (yes/no): ").strip().lower()
        
        if restart != "yes" and restart != "y":
            print("\nThank you for playing! Goodbye!")
            print("=" * 50)
            break


# Start the game
if __name__ == "__main__":
    main()
