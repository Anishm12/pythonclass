print('It is the year 2345. There is a zombie apocolypse and you are stuck in the middle of Boston. You must escape safely without getting eaten by zombies. Good luck!')
choice = input('you can hear zombies coming. Will you: \n\
                1. get in a car you see down the street, or \n\
                2. Hide in a garbage can you see')
if choice == '1':
    choice2 = input('You run to the car, but it is locked. You see 3 possible escape routes. Will you:\n\
           1. climb up a ladder to get on the roof of a building, or\n\
           2. run for a motorcycle you see near you, or\n\
           3. Grab a massive wooden stick you see and try to fight the zombies from on top of the car')
    if choice2 == '1':
        choice4 = input('You made it up onto the roof! You see zombies following you though. Will you: \n\
                         1.Use a zipline that goes to the harbor(no one knows why its there, but its a shortcut to the harbor), or \n\
                         2.Run across the rooftops to get to the helipad')
        if choice4 == '1':
            choice7 = input('You make it to the harbor successfully! There are two escape routes, which will you take:\n\
                            1.Yacht\n\
                            2.Jetskis')
        elif choice4 == '2':
            print('You were overwhelmed by zombies on the way to the helipad.\n\
                  YOU DIED')
    elif choice2 == '2':
        choice5 = input('You get on the motorcycle and start mowing down zombies. You soon realize you have to escape. Will you drive to: \n\
                         1.The harbor\n\
                         2.The helipad')
    elif choice2 == '3':
        print('You grab the stick and hop on the car. You smack some zombies, but there are too much, and you finally get dragged down into the crowd.\n\
                        YOU DIED')
if choice == '2':
    choice3 = input('It worked! A horde of zombies walked right by you! On the bad side, you now smell terrible. You know you need to escape somehow. Will you: \n\
                    1. get to a motorcycle you see near you to get to the harbor as fast as possible, or \n\
                    2. grab a metal bar you see and try to fight your way to the helipad')
    if choice3 == '1':
        choice5 = input('You get on the motorcycle and start mowing down zombies. You soon realize you have to escape. Will you drive to: \n\
                         1.The harbor\n\
                         2.The helipad')
        if choice5 == '1':
            choice7 = input('You make it to the harbor successfully! There are two escape routes, which will you take:\n\
                            1.Yacht\n\
                            2.Jetskis')
            if choice7 == '1':
                print('It looks like you escaped, but the ship is zombie infested! They corner you and throw you in the ocean\n\
                YOU DIED')
            if choice7 == '2':
                print('You jetski your way all the way across the ocean! The problem is that you are very damaged from the zombies. You escaped, but not in very good condition\n\
                 YOU WON(kind of')


        elif choice5 == '2':
            print('You got overwhelmed by zombies on the way\n\
                  YOU DIED')
    elif choice3 == '2':
        choice6 = input('You grab the metal bar and eventually fight your way to the helipad. You can see the helicopter, ready for flight, but there are also zombies you see. Will you:\n\
                        1. hide in a dark shadow you see, or\n\
                        2. Make a run for the helicopter')
        if choice6 == '1':
            print('You hide in the corner, but the zombies pick up your scent and get you(remember that time I told you you smelled terrible\n\
                    YOU DIED')
        elif choice6 == '2':
            print('You make it to the helicopter and fly away safely across the ocean\n\
                  YOU ESCAPED')