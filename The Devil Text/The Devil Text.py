#Simple text based game test
The_End = False

print("Welcome to hell")
print("This will not be a fun experience. I will promise you that")
print("Although my life may be lived through these words, I will do everything in my power to end yours")
print("This is the story of how you died")
input("Press enter to continue")

print("Now tell me about yourself")
player_name = input("What is your name?  ")

print("Hmmm, such an interesting name")
start_confirmation = input(f"So {player_name}, are you ready to play?  ").lower() in ["y", "yes"]

if start_confirmation:
    good_start = True
    start_game = True
    print("Let's begin then")
else:
    bad_start = True
    start_game = True
    print("Somehow you're pissing me off already")
    print("Well you hve no choice either way. So let us begin")

if start_game:
    print("Well we need to start you off somewhere, so which of these woudld you prefer?")
    print("Option 1 is in a dungeon outside of a massive city, option 2 is in a forest in the middle of nowhere")
    player_start_spot = input("Which option would you like?  ")

try:
    player_start_number = float(player_start_spot)
except ValueError:
    print("The hell are doing? Alright you're going to the forest")
    player_start_number = 2

if player_start_number == 1:
    print("Yeah, that's not happening. I don't feel like world building that much")
    player_start_number = 2
    input("You're just going to have the other start, okay?  ")
    print("Not like you have a choice. Anyways...")
if player_start_number == 2:
    print("So there you where, sitting in the middle of the forest of uhh...")
    start_forest_name = input("What do you want it to be the forest of?  ")
    print(f"So there you where, in the forest of {start_forest_name}. For miles upon miles there was only trees in sight")
    print("And uh, ummm. Shit. Give me a second...")
    print("You uhh, you heard a sound in the distance, yeah.")
    check_out_the_sound = input("So do you want to check out the sound? Yes or no?  ").lower() in ["y", "yes"]

if check_out_the_sound:
    print("YES FINALLY. Uh, ahem.")
    go_to_noise = True
    check_out_the_sound_forced = False
else:
    print("What? Why the fuck not? Just let me kill you!")
    print("...I mean let me tell you your story")
    check_out_the_sound_forced = input("Soo, are you going to check out the noise?  ").lower() in ["y", "yes"]
    go_to_noise = False
    if check_out_the_sound_forced:
        print("Finally. Goddamn")
        go_to_noise_forced = True
    else:
        print("...")
        print("As you shout out your last act of defiance against god, a fire roars to life around you, burning you to death")
        input("You have died. Press enter to quit")

if go_to_noise or go_to_noise_forced:
    print("As you trek through the forest you come across an area with no trees")
    print("Inside the area is a wolf and inbetween you and the wolf is a sword stuck into the ground")
    go_for_sword = input("Do you want to attempt to grab the sword?  ").lower() in ["y", "yes"]

if go_for_sword:
    print("You carefully move to the sword, moving slowly to ensure you wont notify the wolf yo your precense")
    print("You carefully pry the sword from the ground when suddenly you have an idea")
    fight_SecondE_wolf = input("Should you attempt to kill the wolf?  ").lower() in ["y", "yes"]
    if fight_SecondE_wolf:
        print("You decide to kill the wolf")
        print("You slowly sneak up to the wolf when you step on a very inconveniently placed tree branch that snaps with a loud crack")
        print("You curse yourself for not leveling your sneak skill as the wolf rises onto it's paws and stares you down")
        kill_SecondE_wolf = input("As the wolf lunges at you, two ideas come to mind: slash at the wolf or stab at the wolf. Slash or stab?  ").lower() in ["stab"]
        if kill_SecondE_wolf:
                print("You stab at the wolf as it lunges towards you")
                print("The blade goes right into the wolfs heart, killing it instantly")
                print("You pull your sword from the wolf's body as it falls to the floor")
                SecondE_Sword = True
                survived_SecondE_wolf = True
        else:
                print("You slash at the wolf and it does next to nothing as the wolf tackles you to the ground")
                print("You flail about with the wolf, getting a few good slashes in, until eventually it swipes your neck with it's claws")
                print("You sit there feeling the blood run down what's left of your neck as you curse yourself for attempting to slash at the wolf")
                input("You have died. Press enter to quit")
                survived_SecondE_wolf = False
else:
    print("As you turn around to leave the area you realize the trees that where quite far apart just a minute ago are now trunk to trunk, forming a wall")
    print("While you sit there staring at the trees you hear a low growl behind you")
    print("You whip around to see the wolf has stood up and is not approaching you")
    grab_sword_from_wolf = input("You have two options, 1 fight the wolf barefisted, or 2 make a dash for the sword. What do you do?  ")
    try:
        SecondE_choice = float(grab_sword_from_wolf)
    except ValueError:
        print("I'm just going to assume you want to fight fist to paw")
        SecondE_choice = 1
        
    if SecondE_choice == 2:
        print("You sprint towards the sword, barely reaching it in time to pick it up and stab at the wolf with it")
        print("The wolf lunges at you, and straight into the point of your sword")
        print("You let go of the sword as the wolf falls to the ground. You try to pull the sword from the wolves body, but it's stuck so you're forced to leave the sword behind")
        survived_SecondE_wolf = True
    if SecondE_choice == 1:
        print("You sprint towards the wolf, fists raised, and looking like a dumbass")
        print("You throw a punch at the wolf as it lunges towards you, unsurprisingly your punch does litterally nothing to the wolf")
        print("The wolf tackles you to the ground, and you reflect on how stupid your plan was as the wolf tears out your throat and you bleed out on the ground")
        survived_SecondE_wolf = False
        input("You have died. Press enter to quit")

if survived_SecondE_wolf:
    print("After your near death experience with the wolf, you decide to go back into the forest")
    ThirdE_direction = False

ThirdE_direction_correct = False
while not ThirdE_direction_correct:    
    ThirdE_direction = input("So, left, straight, or right?  ").lower() in ["straight"]
    if ThirdE_direction:
        ThirdE_direction_correct = True
    else:
        print("You walk into a tree and end back at the your starting point")

if ThirdE_direction:
    print("You go straight")
    print("After walking for what felt like hours you come across a small cabin nestled into the trees")
    FourthE_into_cabin = input("Do you want to go into the cabin?  ").lower() in ["y", "yes"]

if FourthE_into_cabin:
    print("You walk up to the cabin and open the door")
    print("As you step inside, the door closes behind you")
    print("You turn around to open the door, but it's stuck fast")
    FourthE_in_cabin = True
else:
    print("Y'know what")
    print("Fine")
    if bad_start:
        print("Do you have something for ruining what i'm trying to do?")
        print("I mean, I try to further the plot, I try to do anything, and you just go against me")
        print("YOU DIDNT EVEN WANT TO START THE DAMN GAME")
        print("I'm... i'm just done with you")
        input("Leave. Just go. Press enter and leave me.")
        input("I truly just don't want you here. Just leave.")
        input("JUST GO.")
    else:
        print("You turn around and an arrow suddenly sprouts from your chest")
        print("You should've just went into the damn cabin")
        print("But now you're laying there, bleeding out on the floor")
        print("Slowly. Until you die")
        input("You have died. Press enter to exit")

if FourthE_in_cabin:
    print("Now you're stuck inside the cabin")
    print("I said you'd die eventually")
    print("Welcome to the final chapter")
    Cabin_Floor1 = True

##REDO ALL OF THIS WITH DICTIONARIES AND FUNCTIONS##
                    ##OR DONT##

basement_key = False
finish_game = False
while not finish_game:
    if Cabin_Floor1:
        print("You're on the base floor")
        print("You have three things you can do")
        print("1, Investigate the floor you're on")
        print("2, Go up to the second floor")
        print("3, Go down to the basement")
        Cabin_Floor1_WhatDo = float(input("Which option do you choose?  "))
        Cabin_Floor1 = False
        if Cabin_Floor1_WhatDo == 1:
            print("You investiage around the floor and find nothing")
            input("Press enter to continue")
            Cabin_Floor1 = True
            Cabin_Floor2 = False
            Cabin_Floor3 = False
        if Cabin_Floor1_WhatDo == 2:
            Cabin_Floor1 = False
            Cabin_Floor2 = True
            Cabin_Floor3 = False
        if Cabin_Floor1_WhatDo == 3:
            Cabin_Floor1 = False
            Cabin_Floor2 = False
            Cabin_Floor3 = True
    
    if Cabin_Floor2:
        print("You're on the second floor")
        print("You have two things you can do")
        print("1, Investigate the floor you're on")
        print("2, Go to the base level")
        Cabin_Floor2_WhatDo = float(input("Which option do you choose?  "))
        Cabin_Floor2 = False
        if Cabin_Floor2_WhatDo == 1:
            if basement_key:
                print("You look around and find nothing")
                Cabin_Floor2 = True
            else:
                print("You look around the floor and find a key")
                basement_key = True
                Cabin_Floor2 = True
        if Cabin_Floor2_WhatDo == 2:
            Cabin_Floor1 = True
    
    if Cabin_Floor3:
        if basement_key:
            print("The door creeks open")
            print("Inside all you can see is darkness, and descending steps")
            print("You slowly start making your way into the void")
            print("Eventually you reach the bottom")
            finish_game = True
        else:
            print("You try to go into the basement and smack your head against the door that didn't open")
            print("It seems you need a key to enter the basement")
            Cabin_Floor3 = False
            Cabin_Floor1 = True
            
if finish_game:
    print("As you take your last step onto the floor, candles all around the room light up")
    print("In the middle of  the room is humanoid figure with horns")
    print("The demon opens it's glowing red eyes")
    if SecondE_Sword:
        print("You pull out a sword?")
        print("WHAT")
        print("HOW DO YOU STILL HAVE THAT?")
        print("YOU SHOULDN'T HAVE BEEN ABLE TO GRAB THAT")
        print("Look, just put the sword down")
        Drop_Sword = input("put it down, please?  ").lower() in ["n", "no"]
        if Drop_Sword:
            print("WHAT? YOU DARE DEFY ME?")
            print("KILL THEM MY CHILD")
            input("...")
            print("I'm speechless")
            print("That damn holy blade")
            print("I should've never led you to it")
            input("This is the end. Your final chapter has concluded. I hope you don't get a sequal")
            The_End = True
        else:
            print("YOU FOOL")
            print("KILL THE DAMN FOOL MY CHILD")
            print("You damned fool. Now you'll lay there, and in your last seconds you'll know, I kept good on my promise")
            input("Your book has closed. You're dead. There's no coming back for you.")
            The_End = True
    else:
        print("With no means to defend yourself, you'll die")
        print("As the demon rips you to shreds, as the light fades from your eyes...")
        input("Your book closes forever. You will get no sequal")
        The_End = True

if The_End:
    print("")
    print("Thank you for playing")
    print("-LKDS")
    print("")
    print("This was a single dev project from Systematically Flawed")
    input("Your book as a player has closed. Now press enter to close this book")