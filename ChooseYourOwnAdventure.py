print("Welcome to the space adventure!")
print('''
                                                888     d8b                 
                                                888     Y8P                 
                                                888                         
.d8888b 88888b.  8888b.  .d8888b .d88b. .d8888b 88888b. 88888888b. .d8888b  
88K     888 "88b    "88bd88P"   d8P  Y8b88K     888 "88b888888 "88b88K      
"Y8888b.888  888.d888888888     88888888"Y8888b.888  888888888  888"Y8888b. 
     X88888 d88P888  888Y88b.   Y8b.         X88888  888888888 d88P     X88 
 88888P'88888P" "Y888888 "Y8888P "Y8888  88888P'888  88888888888P"  88888P' 
        888                                                888              
        888                                                888              
        888                                                888   
''')
direction = input("You find yourself choosing between two destinations.  Do you want to go through the"
                  "milky way galaxy or explore deep space? (MW or DS)")
if direction.upper() == "MW":
    trial1 = input("Well done! you survived the first decision. Now do you want to explore the solar system or continue on"
                   "to different parts of the galaxy? (SS or CONT)")
    if trial1.upper() == "CONT":
        ending = input("This is the final test. There is an asteroid field near by, if you go through it you will "
                       "reach your destination quicker, but if you go around you will risk loosing your fuel supply."
                       "(THROUGH or AROUND)")
        if ending.upper() == "THROUGH":
            print("Your risk payed off. You found unimaginable riches!")
        else:
            print("You lost your fuel, and ended up loosing.")
    else:
        print("You ended up finding a nice planet and settling down.")
else:
    print("game over!!!")