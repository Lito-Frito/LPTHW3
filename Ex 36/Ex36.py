# -*- coding: utf-8 -*-
# ^ this is for foreign text.
from sys import exit
import sys
from playsound import playsound as play

def ascii_art_prank(): #Done
    input('Hello, press Enter to start game or CTRL Z at any point to terminate the game.')
    print("""                       __        __   /\\/
                      /==\\      /  \\_/\\/
                    /======\\    \\/\\__ \\__
                  /==/\\  /\\==\\    /\\_|__ \\
               /==/    ||    \\=\\ / / / /_/
             /=/    /\\ || /\\   \\=\\/ /
          /===/   /   \\||/   \\   \\===\\
        /===/   /_________________ \\===\\
     /====/   / |                /  \\====\\
   /====/   /   |  _________    /  \\   \\===\\    THE LEGEND OF
   /==/   /     | /   /  \\ / / /  __________\\_____      ______       ___
  |===| /       |/   /____/ / /   \\   _____ |\\   /      \\   _ \\      \\  \\
   \\==\\             /\\   / / /     | |  /= \\| | |        | | \\ \\     / _ \\
   \\===\\__    \\    /  \\ / / /   /  | | /===/  | |        | |  \\ \\   / / \\ \\
     \\==\\ \\    \\  /____/   /_\\ //  | |_____/| | |        | |   | | / /___\\ \\
     \\===\\ \\   \\\\\\\\\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |
       \\==\\/     \\\\\\\\/ / //////   \\| |/==/ \\| | |        | |   | | | /   \\ |
       \\==\\     _ \\/ / /////     _ | |==/     | |        | |  / /  | |   | |
         \\==\\  / \\ / / ///      /|\\| |_____/| | |_____/| | |_/ /   | |   | |
         \\==\\ /   / / /________/ |/_________|/_________|/_____/   /___\\ /___\\
           \\==\\  /               | /==/
           \\=\\  /________________|/=/    OCARINA OF TIME
             \\==\\     _____     /==/
            / \\===\\   \\   /   /===/
           / / /\\===\\  \\_/  /===/
          / / /   \\====\ /====/
         / / /      \\===|===/
         |/_/         \\===/
                        =""")
    play('prank.wav')
    input()
    print("Jk. I'm not that fancy with Python.")
    print("Press 'Enter' again to start the actual game.")
    input()

def welcome_screen():
    """Welcomes player to game.
Also passes player's name to future functions."""
    input("""\n\n\n\n\n\n      __    __   __   __   __   __   __   __    __   __    __   __   __
     _\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
     \\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/
\t  __    __   __   __   __   __   __   __    __   __    __   __   __
\t _\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
\t \\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/
      __  __                 _   _             _
     |  \\/  |           /\\  | | | |           | |
     | \\  / |_   _     /  \\ | |_| |_ __ _  ___| | __   ___  _ __
     | |\\/| | | | |   / /\\ \\| __| __/ _` |/ __| |/ /  / _ \\| '_ \\
     | |  | | |_| |  / ____ \\ |_| || (_| | (__|   <  | (_) | | | |
     |_|  |_|\\__, | /_/    \\_\\__|\\__\\__,_|\\___|_|\\_\\  \\___/|_| |_|
       _____  __/ |                  _____      _       _   _
      / ____||___/                  |  __ \\    (_)     | | (_)
     | (___  _   _ _ __   ___ _ __  | |__) |_ _ _ _ __ | |_ _ _ __   __ _ ___
      \\___ \\| | | | '_ \\ / _ \\ '__| |  ___/ _` | | '_ \\| __| | '_ \\ / _` / __|
      ____) | |_| | |_) |  __/ |    | |  | (_| | | | | | |_| | | | | (_| \\__ \\
     |_____/ \\__,_| .__/ \\___|_|    |_|   \\__,_|_|_| |_|\\__|_|_| |_|\\__, |___/
                  | |                                                __/ |
                  |_|                                               |___/
      _    _  _  ____  ____  ___  ____  _____  _  _    ___     ___     _
     / )  ( \\/ )( ___)(  _ \\/ __)(_  _)(  _  )( \\( )  (__ \\   / _ \\   ( \\
    ( (    \\  /  )__)  )   /\\__ \\ _)(_  )(_)(  )  (    / _/  ( (_) )   ) )
     \\_)    \\/  (____)(_)\\_)(___/(____)(_____)(_)\\_)  (____)()\\___/   (_/

     __    __   __   __   __   __   __   __    __   __    __   __   __
    _\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
    \\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/
\t  __    __   __   __   __   __   __   __    __   __    __   __   __
\t _\\/_  _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_ _\\/_  _\\/_ _\\/_  _\\/_ _\\/_ _\\/_
\t \\/\\/  \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/ \\/\\/  \\/\\/ \\/\\/  \\/\\/ \\/\\/ \\/\\/""")

    print("\nWelcome to My Attack on Super Paintings! (Python 3 version)")
    play("intro.wav")
    input()
    print(f"Or as the creator of this game calls it, '{sys.argv[0]}' script")
    input()
    player_Name = input("First, what's your name?\n>")
    print(f"""\nNice! Glad to meet you {player_Name}.
Let's get started.""")
    input()
    print("Oh, and make sure you have your volume turned on 🔊")
    input()
    return player_Name

def start_room(): # THIS FUNCTION IS PERFECT NOW
    """This is the story that starts the game and offers you what world to explore.
Also returns a list of your inventory."""
    items = []
    print("You wake up alone in a strange room...")
    input()

    print("""The walls are made of white, dull stones.
You are at the intersection of three hallways.
There's a hallway to your left, right, and ahead of you.
Down each hallway is a red carpet with a giant painting at the end.""")

    input()
    print("""There's also a strange painting on the ceiling above you.
It looks like it's a painting of the room you're in.
It's reachable if you jump off the wall.""")
    input()

    print("""The more you look, the more you're convinced it's a mirror of this room.
Except, there's no glare and you don't see yourself in the reflection.
It's unlike any mirror you've ever seen before.""")
    input()
    return items

def painting_descriptions(): #Done
    """This describes each of the paintings, minus the ceiling"""
    print("""\nYou look at the painting ahead of you (#1).
It looks like a snowy, winter scene from Tokyo (東京).
You don't have snow boots, but you notice a pair under the painting.""")
    input()

    print("""There's some humanoid looking giant of titan-size attacking the city.
Some hero seems to be battling it. The hero is normal sized.
You guess that the hero might lose, given the size difference.""")

    input()
    print("""\nYou look at the painting towards your right (#2).
It shows modern day Seoul (서울), the Hyehwa (혜화) area.
You see people in brightly colored uniforms fighting during a hot, summer day.
Their hairstyles are only slightly less ridiculous than their clothing.""")

    input()
    print("""You can't tell who's winning or losing.
Or who's good or evil (because what does good/evil even look like?).
All you can see is that the city looks empty and only partially destroyed.""")

    input()
    print("""\nYou look the painting to your left (#3).
It shows some kind of castle standing tall and alone in the background.
It's spring and cherry blossoms seem to be falling slowly.
There's a path leading to it making the castle easily accesible.""")

    input()

def what_direction(user_name, item_list, smudged_painting): #Done
    forward = ['forward', 'Foward', 'front', 'Front', 'F', 'f', '#1', '1', "pa'lante", 'adelante', 'pa lante']
    right = ['right', 'Right', 'r', 'R', '2', '#2', 'derecha']
    left = ['left', 'Left', 'l', 'L', '#3', '3', 'izquierda']
    up = ['jump', 'jump up', 'jump off wall', 'jump on wall', 'ceiling', '#4', '4', 'j', 'u', 'mirror', 'm']
    smudged_painting == False

    player_Choice = input(f"""So {user_name}, what do you want to do? \nWhat direction do you want to go in?
You can also try to touch the mirror if that's your thing.
>""")

    if player_Choice in forward: #This allows you to go to painting_1
        walking()
        painting_one(user_name, item_list)
        touch_painting_returned_val = touch_painting(user_name, item_list)

        if touch_painting_returned_val == 'no':
            input()
            what_direction(user_name, item_list, smudged_painting)
        elif touch_painting_returned_val == 'yes':
            sucked_in(user_name)
            AOT(user_name, item_list)
        else:
            print("Somehow you broke the game; congrats!")
            death()

    elif player_Choice in right: #This allows you to go to painting_2
        walking()
        painting_two(user_name, item_list)
        touch_painting_returned_val = touch_painting(user_name, item_list)

        if touch_painting_returned_val == 'no':
            input()
            what_direction(user_name, item_list, smudged_painting)
        elif touch_painting_returned_val == 'yes':
            sucked_in(user_name)
            my_hero(user_name, item_list)
        else:
            print("Somehow you broke the game; congrats!")
            death()

    elif player_Choice in left: #This allows you to go to painting_3 and returns smudged_painting as TRUE
        walking()
        painting_three(user_name, item_list)
        touch_painting_returned_val = touch_painting(user_name, item_list)

        while True:
            if touch_painting_returned_val == 'no':
                input()
                what_direction(user_name, item_list, smudged_painting)
                break
            elif touch_painting_returned_val == 'yes'  and smudged_painting == False:
                print("""\nYou touching the painting smudged it.
You have ruined the painting.
You are filled with shame ☹ .""")
                play("shame.wav")
                input()

                print("""You quickly look around to see if anyone saw what you did.
No one did because you remembered when the game that said, 'you wake up alone'.
You quickly walk back to the middle of the room after this faux pas.""")
                smudged_painting = True
                input()
                what_direction(user_name, item_list, smudged_painting)
            elif touch_painting_returned_val == 'yes'  and smudged_painting == True:
                print("""\nYou reach out to touch the painting, but immediately notice your past mistake.
You are filled with shame again and wonder why you tried this painting again.
You scurry back to the center room, hopefully remembering your choices.""")
                input()
                what_direction(user_name, item_list, smudged_painting)
            else:
                print("Somehow you broke the game; congrats!")
                death()
    elif player_Choice in up:
        print("""\nYou get a running start and make towards a blank part of the wall.
As you approach the wall, you push off the ground as hard as you can and jump.
You say \"yahoo!\" for some reason and notice you jump higher than usual.""" )
        play("yahoo.wav")
        input()

        print("""You hit the mid-point of the wall and you immediately push off it.
You realize you'll have enough force to reach the ceiling/mirror.
You reach out to touch it, your fingers basically scraping it.""")
        input()

        touch_mirror(user_name)

        print("""You land, hard back on the carpeted floor in the middle of the first room.
You see your familar surroundings and stand up again, taking in the new info.
You realize the ceiling isn't an exit, so maybe picking a painting is.""")

        input()
        what_direction(user_name, item_list, smudged_painting)
    else:
        learn_to_type(user_name, item_list)
        return what_direction(user_name, item_list, smudged_painting)

def touch_painting(user_name, item_list):#Done
    Yes = ['Y', 'y', 'Yes', 'yes']
    No = {'N', 'n', 'No', 'no'}
    print("While gazing at the picture, you find yourself wanting to touch it. \nDo you?\n")

    touch = input(f"Press either Y or N {user_name}:\n> ")
    if touch in Yes:
        return "yes"
    elif touch in No:
        print(f"\nOk {user_name}. \nYou walk back the main room.")
        return 'no'
    else:
        learn_to_type(user_name, item_list)
        return touch_painting(user_name, item_list)

def sucked_in(user_name):#Done
    """This is the text for when you touch a painting"""
    input(f"\nGood choice {user_name}.")

    print(f"""\nYou defy every sign you've ever seen at a museum and touch the painting.
As soon as you do, you feel slingshot into the painting.""")
    play("painting.wav")
    input()

def touch_mirror(user_name):#Done
    input(f"Interesting choice {user_name}.")

    print(f"""\nAs your fingers touch the ceiling/mirror, it feels like a liquid.
As soon as you do, you feel slingshot into the ceiling/mirror.""")
    play("painting.wav")
    input()

def walking():#Done
    """Just prints the walking strings"""
    print("\nYou walk towards the painting.")
    input()
    print("Upon further examination, you see more details.")
    input()

def painting_one(user_name, item_list):#Done
    """This is the path for painting #1 i.e the AoT painting"""
    print("The monster seems to be eating something human looking.")
    input()
    print("""The hero also looks like they've unresolved childhood trauma.
You look at a particular subject of the painting.
It looks like some beast-looking, titan-sized monster.""")
    input()

    print("""


                  ,   .-'"'=;_  ,
                  |\\.'-~`-.`-`;/|
                  \\.` '.'~-.` './
                  (\\`,__=-'__,'/)
               _.-'-.( d\_/b ).-'-._
             /'.-'   ' .---. '   '-.`\\
           /'  .' (=    (_)    =) '.  `\\
          /'  .',  `-.__.-.__.-'  ,'.  `\\
         (     .'.   V       V  ; '.     )
         (    |::  `-,__.-.__,-'  ::|    )
         |   /|`:.               .:'|\\   |
         |  / | `:.              :' |`\\  |
         | |  (  :.             .:  )  | |
         | |   ( `:.            :' )   | |
         | |    \\ :.           .: /    | |
         | |     \\`:.         .:'/     | |
         ) (      `\\`:.     .:'/'      ) (
         (  `)_     ) `:._.:' (     _(`  )
         \\  ' _)  .'           `.  (_ `  /
          \\  '_) /   .'"```"'.   \\ (_`  /
           `'"`  \  (         )  /  `"'`
       ___        `.`.       .'.'        ___
     .`   ``\"\"\"\'\'\'--`_)     (_'--'\'\'\"\"\"``   `.
    (_(_(___...--'"'`         `'"'--...___)_)_)
    """)

    input()

    boots = "Snow Boots"
    while True:
        if boots not in item_list:
            print("""You also look at the snow boots.
They're very fashionable and seem practical.
You decide to take them.""")
            item_list.append(boots)
            input()

            print("\nYou got Spumoni boots!")
            play("item.wav")

            input(f"\nItems:\n{item_list}")
            input()
            break
        else:
            break

def AOT(user_name, item_list): #Done
    """This is if the user decides to touch P1; They are now in the AOT world"""
    Yes = ['Y', 'y', 'Yes', 'yes']
    No = ['N', 'n', 'No', 'no']

    print("""You land hard on concrete.
Dazed, you look around as you feel a rhythmic thundering.
The sharp, cold air only adds to your frustration.""")

    input()
    print("""There's snow everywhere.
You decide to put on your new, stylish yet practical snow boots.
They provide a lot more grip than your old shoes.""")

    input()
    print("""You now see the cause of all the thundering.
The Jaw Titan, I mean monster is smashing his way through the city.
It roars, striking terror in your heart.""")

    input()
    print("""        _______________
       /               \\
      /                 \\
    //                   \\/\\
    \\|   XXXX     XXXX   | /
     |   XXXX     XXXX   |/
     |   XXX       XXX   |
     |                   |
     \\__      XXX      __/
       |\     XXX     /|
       | |           | |
       | I I I I I I I |
       |  I I I I I I  |
       \\_             _/
         \\_         _/
           \\_______/""")
    play("roar.wav")

    input()
    print(f"""You also see some humans zipping around, using some kind of mechanical device.
There's one next to you, with a sticky note that says 'VME'.""")
    while True:
        grab = input(f"Do you want to grab it {user_name}? \n\n>")

        if grab in Yes:
            VME = 'VME ⚙ '
            item_list.append(VME)
            print("\nYou got the Vertical Maneuvering Equipment (VME)!")
            play("item.wav")

            input()
            print(f"Items:\n{item_list}")

            input()
            print("""You also see a pair of distinctive looking swords.
You think they look cool.
You decide to grab them as well.""")

            input()
            print("You added 'Flesh Pairing Swords' to your items too!")
            play("item.wav")
            swords = 'Flesh Pairing Swords ⚔ '
            item_list.append(swords)

            input()
            print(f"Items:\n{item_list}")

            input()
            print(f"Nice {user_name}!")

            input()
            print("""You're feeling prepared to help fight the titan, so you go towards the fight.
As you get there, the hero tells you how to take down a titan.
Given how new you are, you decide you can't fight and will distract the titan.""")

            input()
            print("""The titan sees you and starts charging at you.
You use the VME to quickly navigate away, around the corner of some buildings.
The titan is quickly gaining on you and you notice the hero is no longer around.
You start to worry...""")

            input()
            print("""You continue turning corners as sharp as possible, trying to shake the titan.
On your last turn, the titan's hand falls upon you.
It barely missed you because you used your swords to parry.
However, the heavy attack has shattered your swords.""")

            input()
            item_list.pop(2)
            print(f"Items:\n{item_list}")

            input()
            print("""You start to panic because now you're defenseless.
But suddenly, you see blood, the titan stops, and then starts to fall.
You see Levi, I mean the hero, standing on the nape of its neck.""")

            input()
            print("""The hero nods in thanks and acknowledgement.
You nod back, thinking that they def should work on their timing.
Your VME is also out of gas, so you decide to discard it.""")

            input()
            item_list.pop(1)
            print(f"Items:\n{item_list}")

            input()
            print("""All of a sudden, you hear a ringing sound.
You wake up...it dawns on you that this was a dream.
You realize you're going to be late for school, so you get out of bed.""")

            input()
            print("""But then you notice, you're wearing those dope Spumoni boots.
You take a second to think about what that means....
Your second alarm goes off!
You head out for school, you'll think about all this later.""")

            return true_ending(user_name, item_list)

        elif grab in No:
            print("""
You realize this is outside your capabilities.
You see the titan suddenly swat the hero...it doesn't look good.
The titan then turns to face you; you immediately run away.""")

            input()
            print("""The titan gives chase and you start to panic.
It reaches out with one hand.
You instinctively duck out in a nearby, partially destoryed building.""")

            input()
            print("""Its thundering steps are only getting closer.
Its other hand starts coming for you.
Your mind goes blank, the shadow from its palm closes in on you.""")

            input()
            print("""Just then, you hear an increduibly loud ringing sound.
It's your alarm...
You wake up...you realize it was all a dream.
You also realize you're late!""")

            input()
            item_list[:] = []

            print("You check if you still have the Spumoni boots.")

            input()

            print(f"Items: \n{item_list}")

            input()
            print("""You do not....sadness.
You arrive late to school"
Your homeroom teacher gives you detention.
For life...""")
            input()

            return death(item_list, user_name)

        else:
            learn_to_type(user_name, item_list)
            continue

def painting_two(user_name, item_list): #Done
    print("""The disfigured man has on some kind of coat or suit.
He also has a mask on that has valves or exhausts coming out of it.
You observe the name of the creepy man is actually written below.""")
    input()

    print("""                       _.._
                    .'      '
                   _;.-\"\"\"-.;_
               _.-' _..-.-.._ '-._
              ';--.-----------.--;'
              \\\\     #     #     //
               \\\\_   _______    //
                \\\\  | || || |  //
            _.-'`;\\\\| || || | //   ;'-.
          .' :  /   | || || |   \\     '.
         /   : /__  \\ _____ / __\\ :      `.
        /    |   /  '._/_\\_.'  \\   :       `\\
      /      |      |()    ()      |         \\
    |         |                        |     /
    \\     \\   |][     |   |    ][ |   /     /
     \\     \\ ;=""====='\"\"\"'====""==; /     /
      |/`\\  \\/      |()    ()      \\/  /`\\|
       |_/.-';      |              |`-.\\_|
         /   |      ;              :   \\
         |__.|      |              |.__|
             ;      |              |
             '-._   ;           _.-'
                 `;"--.....--";`
                  |    | |    |
                  |    | |    |
             _..._L____J L____J _..._
           .` "-. `%   | |    %` .-" `.
          /      \\    .: :.     /      \\
          '-..___|_..=:` `-:=.._|___..-'
                  (ALL FOR ONE)""")
    input()
    print("""You notice the other person in the painting.
They're wearing a red and blue suit.
Their eyes are sunken, and he looks skeletal.""")
    input()

def my_hero(user_name, item_list): #Done
    """This is the path for painting #2, i.e. the My Hero Academia painting"""
    Yes = ['Y', 'y', 'Yes', 'yes']
    No = {'N', 'n', 'No', 'no'}

    print("""You land face first.
You stand up and compose yourself.""")

    input()
    print("On the floor, you also notice a bag of money.")

    input()
    print("""──────────────────██████────────────────
─────────────────████████─█─────────────
─────────────██████████████─────────────
─────────────█████████████──────────────
──────────────███████████───────────────
───────────────██████████───────────────
────────────────████████────────────────
────────────────▐██████─────────────────
────────────────▐██████─────────────────
──────────────── ▌─────▌────────────────
────────────────███─█████───────────────
────────────████████████████────────────
──────────████████████████████──────────
────────████████████─────███████────────
──────███████████─────────███████───────
─────████████████───██─███████████──────
────██████████████──────────████████────
───████████████████─────█───█████████───
──█████████████████████─██───█████████──
──█████████████████████──██──██████████─
─███████████████████████─██───██████████
████████████████████████──────██████████
███████████████████──────────███████████
─██████████████████───────██████████████
─███████████████████████──█████████████─
──█████████████████████████████████████─
───██████████████████████████████████───
───────██████████████████████████████───
───────██████████████████████████───────
─────────────███████████████────────────""")

    input()
    print("There's a sign next to it that says 'Free Gift!'")

    money = "100,000 ₩ (KRW)"
    while True:
        print(f"Do you pick it up {user_name}?")
        pick_up_money = input(">")

        if pick_up_money in Yes:
            input(f"\nGood choice {user_name}.")
            item_list.append(money)
            print("\nYou got some money (KRW)!")
            play("item.wav")
            input(f"\nItems:\n{item_list}")
            input()
            break
        elif pick_up_money in No:
            print("\nYou decide to leave it there because you aren't sure if it's a trap.")
            input()
            break
        else:
            learn_to_type(user_name, item_list)

    print("""You suddenly hear yelling.
You scan the area and see the person with a disfigured face.
They are being blown away by the punch of a person with a disfigured arm.
You instantly put together that this is All Might defeating All For One.""")
    play("smash.wav")

    input()
    print("""As you realize what's happening, you're blown away from the shockwave.
You find your fall broken by some trash bags under a small building.
You decide to let the rest of the chapter from the manga play out.""")

    input()
    print("""You look at the sign of the building that you landed near.
It says "PURIE" and there's a pleasant smell coming from it.
You decide to go in since the fight outside is settled.""")

    input()
    print("""You are greeted by the nicest family of sisters.
You see that they sell jams and perfumes.
It seems business is slow today, probably due to the fight.""")


    input()
    print("They offer to sell you some jam at a discount.")
    input()

    while True:
        if money in item_list:
            jam = input(f"Do you want to buy some {user_name}?\n>")
            if jam in Yes:
                input(f"\nGood choice {user_name}.")
                item_list.pop()

                coco = 'Coconut Jam'
                rose = "Rose Jam"
                wine = "Wine Jam"
                mango = "Mango Jam"

                print(f"""You sample a few different jams, for free!
You buy your favorites and some as a gift for those back home.
It comes out to exactly {money}, nice!""")
                item_list.extend((coco, rose, wine, mango))

                input()
                print("\nYou got some amazing jams!")
                play("item.wav")
                input(f"\nItems:\n{item_list}")

                print("""\nThe Jam Fam thanks you for your patronage.
They give you a gift as 'service'.
Apparently, they've connects in the airline industry."
It's a flight ticket home!""")

                input()
                print(f"Nice!\nYou instantly go home {user_name} ✈ !")
                return true_ending(user_name, item_list)

            elif jam in No:
                print("""\nYou decide to be greedy and hoard your money.
Not only does this have a negative effect on the economy, you also are hungry!
You leave the cozy store in search of food and a way back home.""")

                item_list[:] = []
                input()
                print("You never find a way back home and eventually starve to death.")
                input()
                return death(item_list, user_name)

            else:
                learn_to_type(user_name, item_list)
        elif money not in item_list:
            jam = input(f"Do you want to buy some {user_name}?\n>")
            if jam in Yes:
                print("""
You check your pockets...you don't have any money!
You realized you should've grabbed that free money...
The staff smiles, they are so nice.
They give you a few free samples before you leave.""")

                item_list[:] = []
                input()
                print("You wander around and never find a way back home and eventually starve to death.")
                input()
                return death(item_list, user_name)
            elif jam in No:
                print("""\nYou know you don't have money, so you decline to save face.
Before leaving, the Jam Fam offers you some free samples.
They are so nice!""")

                item_list[:] = []
                input()
                print("You wander around and never find a way back home and eventually starve to death.")
                input()
                return death(item_list, user_name)
            else:
                learn_to_type(user_name, item_list)
        else:
            print("Somehow you broke the game; congrats!")
            death()

def painting_three(user_name, item_list): #THIS FUNCTION IS PERFECT NOW
    """This is the path for painting #3 i.e. the start of smudged_painting"""
    print("""You see the beautiful painting.
There's a small, mustached plumber fighting a giant turtle-monster.
You look further at the face of this chimera, noticing how ugly it is.""")
    input()
    print("""───────▄█──────────█─────────█▄───────
─────▐██──────▄█──███──█▄─────██▌─────
────▐██▀─────█████████████────▀██▌────
───▐██▌─────██████████████─────▐██▌───
───████────████████████████────████───
──▐█████──██████████████████──█████▌──
───████████████████████████████████───
────███████▀▀████████████▀▀███████────
─────█████▌──▄▄─▀████▀─▄▄──▐█████─────
───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───
──██████████████████████████████████──
─████████████████████████████████████─
▐██████──███████▀▄██▄▀███████──██████▌
▐█████────██████████████████────█████▌
▐█████─────██████▀──▀██████─────█████▌
─█████▄─────███────────███─────▄█████─
──██████─────█──────────█─────██████──
────█████────────────────────█████────
─────█████──────────────────█████─────
──────█████────────────────█████──────
───────████───▄────────▄───████───────
────────████─██────────██─████────────
────────████████─▄██▄─████████────────
───────████████████████████████───────
───────████████████████████████───────
────────▀█████████▀▀█████████▀────────
──────────▀███▀────────▀███▀──────────""")
    input()

def learn_to_type(user_name, item_list): #Done
    """Error message user gets for typing something nonsensical or erroneous"""
    print(f"\nI'm sorry {user_name}, I don't know what to do with that ☹ ")
    input()
    print("""Please type something that makes sense.
Or press 'CTRL Z' to end the game.
We'll only be a lil hurt if you do that (ಥ_ಥ) """)
    input()

def death(item_list, user_name): #Done
    """This is the message players get upon dying"""
    print("""
                     uuuuuuu
                 uu$$$$$$$$$$$uu
              uu$$$$$$$$$$$$$$$$$uu
             u$$$$$$$$$$$$$$$$$$$$$u
            u$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$"   "$$$"   "$$$$$$u
           "$$$$"      u$u       $$$$"
            $$$u       u$u       u$$$
            $$$u      u$$$u      u$$$
             "$$$$uu$$$   $$$uu$$$$"
              "$$$$$$$"   "$$$$$$$"
                u$$$$$$$u$$$$$$$u
                 u$"$"$"$"$"$"$u
      uuu        $$u$ $ $ $ $u$$       uuu
     u$$$$        $$$$$u$u$u$$$       u$$$$
      $$$$$uu      "$$$$$$$$$"     uu$$$$$$
    u$$$$$$$$$$$uu    \"\"\"\"\"    uuuu$$$$$$$$$$
    $$$$\"\"\"$$$$$$$$$$uuu   uu$$$$$$$$$\"\"\"$$$\"
     \"\"\"      \"\"$$$$$$$$$$$uu \"\"$\"\"\"
               uuuu \"\"$$$$$$$$$$uuu
      u$$$uuu$$$$$$$$$uu \"\"$$$$$$$$$$$uuu$$$
      $$$$$$$$$$\"\"\"\"           \"\"$$$$$$$$$$$\"
       \"$$$$$\"                      \"\"$$$$\"\"
         $$$"                         $$$$\"
    """)
    play("death.wav")
    input()

    print(f"""Oh no {user_name}!
You died! ⚰
Try playing the game again.
This time, try choosing something different, try choosing more wisely.""")
    exit(0)

def true_ending(user_name, item_list):#Done
    """This is the message you get for finding a true ending."""
    input()
    print(f"""Congrats on finding one of the true endings in the game {user_name} !
You made the right choices throughout the game and were able to end up here.
Clearly you showed empathy, courage, and altruism in this imaginary game.
Try playing the game again and discovering all 3 true endings!""")
    play("ending.wav")

    input()
    print("Thank you for playing!")
    exit(0)

def main(): #Done
    """Takes all the other functions and passes them in order; done to avoid global vars"""
    smudged_painting = False
    ascii_art_prank()
    return_name = welcome_screen() #Gives you player's name
    item_list = start_room() #Gives you your inventory as a list
    painting_descriptions() #Brief description of the player's environment
    what_direction(return_name, item_list, smudged_painting)#This is where the Player chooses their adventure

main()
exit(0)
