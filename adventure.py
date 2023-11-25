import time
def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious land...")
    time.sleep(1)
    print("Your mission is to find the hidden treasure.")
    time.sleep(1)

def choose_path():
    print("Which path will you choose? Left or Right?")
    choice = input("Enter your choice: ").lower()
    if choice == "left":
        print("You encounter a ferocious dragon! Quick, find another way!")
        # Add more story or game logic based on choices
    elif choice == "right":
        print("You discover a hidden passage!")
        # Continue building the story based on different choices

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main ()
import time

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious land...")
    time.sleep(1)
    print("Your mission is to find the hidden treasure.")
    time.sleep(1)

def choose_path():
    print("Which path will you choose? Left or Right?")
    choice = input("Enter your choice: ").lower()
    if choice == "left":
        print("You encounter a ferocious dragon! Quick, find another way!")
        time.sleep(1)
        print("You backtrack and find a small cave.")
        explore_cave()
    elif choice == "right":
        print("You discover a hidden passage!")
        time.sleep(1)
        print("You follow the passage and reach a bridge.")
        cross_bridge()

def explore_cave():
    print("You enter the cave and see two tunnels.")
    time.sleep(1)
    print("Do you go through the 'dark tunnel' or the 'glowing tunnel'?")
    cave_choice = input("Enter your choice: ").lower()
    if cave_choice == "dark tunnel":
        print("You enter the dark tunnel and find a treasure chest!")
        time.sleep(1)
        print("Congratulations! You found the hidden treasure!")
    elif cave_choice == "glowing tunnel":
        print("You follow the glowing tunnel and encounter a giant spider!")
        fight_or_flee()

def cross_bridge():
    print("As you approach the bridge, a troll appears!")
    time.sleep(1)
    print("The troll challenges you to a riddle.")
    time.sleep(1)
    print("What has keys but can't open locks?")
    riddle_answer = input("Your answer: ").lower()
    if riddle_answer == "keyboard":
        print("The troll is impressed and lets you pass.")
        time.sleep(1)
        print("You move ahead and find a treasure chest!")
        time.sleep(1)
        print("Congratulations! You found the hidden treasure!")
    else:
        print("The troll is angry! You must flee!")
        fight_or_flee()

def fight_or_flee():
    print("Will you 'fight' or 'flee'?")
    action = input("Enter your choice: ").lower()
    if action == "fight":
        print("You attempt to fight...")
        time.sleep(1)
        print("You defeat the enemy and continue your journey.")
        # Continue the game logic further
    elif action == "flee":
        print("You run away...")
        time.sleep(1)
        print("You manage to escape and find another path.")
        # Continue the game logic further

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def intro():
    print_slow("Welcome to the Adventure Game!")
    time.sleep(1)
    print_slow("You find yourself in a mysterious land...")
    time.sleep(1)
    print_slow("Your mission is to find the hidden treasure.")
    time.sleep(1)

def choose_path():
    print_slow("Which path will you choose? Left or Right?")
    choice = input("Enter your choice: ").lower()
    if choice == "left":
        print_slow("You encounter a ferocious dragon! Quick, find another way!")
        time.sleep(1)
        print_slow("You backtrack and find a small cave.")
        explore_cave()
    elif choice == "right":
        print_slow("You discover a hidden passage!")
        time.sleep(1)
        print_slow("You follow the passage and reach a bridge.")
        cross_bridge()

def explore_cave():
    print_slow("You enter the cave and see two tunnels.")
    time.sleep(1)
    print_slow("Do you go through the 'dark tunnel' or the 'glowing tunnel'?")
    cave_choice = input("Enter your choice: ").lower()
    if cave_choice == "dark tunnel":
        print_slow("You enter the dark tunnel and find a treasure chest!")
        time.sleep(1)
        print_slow("Congratulations! You found the hidden treasure!")
    elif cave_choice == "glowing tunnel":
        print_slow("You follow the glowing tunnel and encounter a giant spider!")
        fight_or_flee()

def cross_bridge():
    print_slow("As you approach the bridge, a troll appears!")
    time.sleep(1)
    print_slow("The troll challenges you to a riddle.")
    time.sleep(1)
    print_slow("What has keys but can't open locks?")
    riddle_answer = input("Your answer: ").lower()
    if riddle_answer == "keyboard":
        print_slow("The troll is impressed and lets you pass.")
        time.sleep(1)
        print_slow("You move ahead and find a treasure chest!")
        time.sleep(1)
        print_slow("Congratulations! You found the hidden treasure!")
    else:
        print_slow("The troll is angry! You must flee!")
        fight_or_flee()

def fight_or_flee():
    print_slow("Will you 'fight' or 'flee'?")
    action = input("Enter your choice: ").lower()
    if action == "fight":
        print_slow("You attempt to fight...")
        time.sleep(1)
        print_slow("You defeat the enemy and continue your journey.")
        # Continue the game logic further
    elif action == "flee":
        print_slow("You run away...")
        time.sleep(1)
        print_slow("You manage to escape and find another path.")
        # Continue the game logic further

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
import time

# Function to print text slowly for a dramatic effect
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Introduction to the game
def intro():
    print_slow("Welcome to the Adventure Game!")
    time.sleep(1)
    print_slow("You find yourself in a mysterious land...")
    time.sleep(1)
    print_slow("Your mission is to find the hidden treasure.")
    time.sleep(1)

# Function for choosing a path
def choose_path():
    print_slow("Which path will you choose? Left or Right?")
    choice = input("Enter your choice: ").lower()
    if choice == "left":
        print_slow("You encounter a ferocious dragon! Quick, find another way!")
        time.sleep(1)
        print_slow("You backtrack and find a small cave.")
        explore_cave()
    elif choice == "right":
        print_slow("You discover a hidden passage!")
        time.sleep(1)
        print_slow("You follow the passage and reach a bridge.")
        cross_bridge()

# Function for exploring the cave
def explore_cave():
    print_slow("You enter the cave and see two tunnels.")
    time.sleep(1)
    print_slow("Do you go through the 'dark tunnel' or the 'glowing tunnel'?")
    cave_choice = input("Enter your choice: ").lower()
    if cave_choice == "dark tunnel":
        print_slow("You enter the dark tunnel and find a treasure chest!")
        time.sleep(1)
        print_slow("Congratulations! You found the hidden treasure!")
    elif cave_choice == "glowing tunnel":
        print_slow("You follow the glowing tunnel and encounter a giant spider!")
        fight_or_flee()

# Function for crossing the bridge
def cross_bridge():
    print_slow("As you approach the bridge, a troll appears!")
    time.sleep(1)
    print_slow("The troll challenges you to a riddle.")
    time.sleep(1)
    print_slow("What has keys but can't open locks?")
    riddle_answer = input("Your answer: ").lower()
    if riddle_answer == "keyboard":
        print_slow("The troll is impressed and lets you pass.")
        time.sleep(1)
        print_slow("You move ahead and find a treasure chest!")
        time.sleep(1)
        print_slow("Congratulations! You found the hidden treasure!")
    else:
        print_slow("The troll is angry! You must flee!")
        fight_or_flee()

# Function for deciding to fight or flee
def fight_or_flee():
    print_slow("Will you 'fight' or 'flee'?")
    action = input("Enter your choice: ").lower()
    if action == "fight":
        print_slow("You attempt to fight...")
        time.sleep(1)
        print_slow("You defeat the enemy and continue your journey.")
        # Continue the game logic further
    elif action == "flee":
        print_slow("You run away...")
        time.sleep(1)
        print_slow("You manage to escape and find another path.")
        # Continue the game logic further

# Main function to initiate the game
def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
