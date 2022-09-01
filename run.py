def start_selection(mode):
    """
    request for user to select either rules to play the game, or to star the the game.
    """
    try:
        if mode.lower() == "play":
            return True
        elif mode.lower() == "rules":
            print("rules to be displayed here")
            return False
        elif mode.lower() != "play" or "rules":
            raise KeyError
    except KeyError:
        print(f"your entry of '{mode}' is not recognised, please type either 'play','rules' or 'exit'")
        return False

def get_difficulty():
    """
    Allows the user to select the difficulty of the game they are starting.
    """
    print(f"Enter your difficulty setting,\n"
        f"1 for Easy \n"
        f"2 for Medium \n" 
        f"3 for Hard \n")
    while True:
        setting = input()
        difficulty = ""
        try:
            if int(setting) == 1:
                difficulty = "easy"
            elif int(setting) == 2:
                difficulty = "medium"
            elif int(setting) == 3:
                difficulty = "hard"
            elif setting != 1 or 2 or 3:
                raise AttributeError
            return difficulty
        except AttributeError:
            print(f"{setting} is an invalid reference, please enter play/rules/exit")
            return False

def create_puzzle():
    """
    Reads the difficulty setting selected, then creates the grid.
    """

    difficulty = get_difficulty()
    print("Creating template....")
    print("Scribbling down the answers...")
    print(f"{difficulty} has been selected\n")

    pull_puzzle = f"sudoku_"+difficulty+"_display"
    pull_answer = f"sudoku_"+difficulty+"_answer"

    with open(pull_puzzle+".txt") as f:
        puzzle = f.readlines()
    print("Your puzzle is as follows:")
    for line in range(len(puzzle)):
        print(puzzle[line])

    with open(pull_answer+".txt") as a:
        answer = a.readlines()

    

def intro():
    """
    Greets the user and starts the Sudoku application
    """
    print("Welcome to my Sodoku Challenge application!\n")
    user = input("Enter your name\n")
    print(f"\nThank you {user.capitalize()},\n"
          f"Type 'rules' if you wish for me to explain how to play\n"
          f"Or type 'play' if you wish to start playing")
    

    while True:
        mode = input()

        if start_selection(mode):
            print("\nStarting the game now...")
            break

def run():
    """
    Generating order of processes for the game
    """
    intro()
    create_puzzle()
run()