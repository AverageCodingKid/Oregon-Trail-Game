print("Oregon Trail Game")
chosen_intro = input("""\nOptions:

1| Play the game
2| Learn About the creator
3| Source code
4| Feedback
                        Type here: """)

if chosen_intro == "2":
    print("""Hello, I am Shea. 
I started computer programming at the age of 10. More coming soon...
--------------------------------------------------------------------
Social:
YouTube: @-Meme-Master-
GitHub: @AverageCodingKid
""")
elif chosen_intro == "1":
    # Health
    player1_health = 100
    player2_health = 100
    player3_health = 100
    player4_health = 100    
    # Food
    food = 100
    total_health = player1_health + player2_health + player3_health + player4_health

    print("\nWelcome to the Oregon trail!", "\n\nMake sure to check out my YouTube channel @-Meme-Master-")

    # Players
    name1 = input("\nWhat would you like to name player 1 (You): ")
    name2 = input("What would you like to name player 2: ")
    name3 = input("What would you like to name player 3: ")
    name4 = input("What would you like to name player 4: ")        

    player1 = name1    
    player2 = name2
    player3 = name3
    player4 = name4

    trail_start_screen = input("""Select an option
1| Begin journey
2| Purchase items
3| Quit game
                        Type here: """)

    if trail_start_screen == "2":
        store = input("""\n\n\nWhat would you like to purchase?
         
1| Food
2| Water
3| Ox
4| Clothes
5| HP
6| Wagon Wheels
                        Type here: """)






elif chosen_intro == "3":
    print("\nYou may find the source code here: https://raw.githubusercontent.com/AverageCodingKid/Oregon-Trail-Game/main/maingame.py\n")
elif chosen_intro == "4":
    print("\nYou may submit feedback here: https://docs.google.com/forms/d/1r7coffgHkjaSxmx5NR1jm5iR57ZGhlicuafjfvuwcx0")

else:
    print("Character", chosen_intro, "Invalid")