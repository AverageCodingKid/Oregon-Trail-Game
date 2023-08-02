# Intro options
print("Oregon Trail Game")
chosen_intro = input("""Options:
1| Play the game
2| Learn About the creator
3| Source code
4| Feedback

Type here: """)

if chosen_intro == "2":
    print(""" Hello, I am Shea. 
I started computer programming at the age of 10. More coming soon...
--------------------------------------------------------------------
Social:
YouTube: @-Meme-Master-
GitHub: @AverageCodingKid
""")
     
    player1 = str(input("What would you like to name player 1 (You): "))
    name2 = str(input("What would you like to name player 2: "))
    name3 = str(input("What would you like to name player 3: "))
    name4 = str(input("What would you like to name player 4: "))
    
    # Players
    player2 = name2
    player3 = name3
    player4 = name4
    
    # Health
    player1_health = 100
    player2_health = 100
    player3_health = 100
    player4_health = 100
    
    # Total Health
    total_health = player1_health + player2_health + player3_health + player4_health
    
    # Food
    food = 100

    # Main plot
    print("")

    # Introduction
    if chosen_intro == "1":
        print("Oregon Trail")
        print("Welcome to the Oregon trail", player1, "!", "\nMake sure to check out my YouTube channel @-Meme-Master-")
        
        # Add condition here to break the loop
        
        # Test successful if this point is reached
        print("\nTest Complete...")
    



































    # Prompt user to choose an option again once game end
    chosen_intro = input("""Options:
1| Play the game again
2| Learn About the creator
3| Source code
4| Feedback

Type here: """)