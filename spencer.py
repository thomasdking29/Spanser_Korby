#!/usr/bin/env python3

def main():
    
    import random
    
    current_location = "bed"
    
    game_running = True
    
    in_bedroom = True
    
    date = 1
    
    poop_count = -2
    
    good_morning_spencer(date)
    
    while poop_count <5:
        where_is_spencer(current_location)
        
        new_location = bedroom_move(current_location, in_bedroom)
        current_location = new_location[0]
        in_bedroom = new_location[1]
        
        poop_count = (random_bedroom_event(poop_count))
        
        if current_location == "back door":
            print("After passing through the door, Spencer realizes \n that he has locked himself out. His bowels contort, \n and he knows this is the end.")
            poop_count += 100
            
        if current_location == "kitchen door":
            print("Spencer flings himself out the kitchen door and sprints for \n the toilet that he desperately needs, only \n to find that Ping has somehow locked herself \n in his bathroom to vomit. He pounds \n on the door to know avail, but resignation \n slowly seizes him as he realizes his time is coming.")
            poop_count += 100        
        
        poop_count += 1
        game_running = (poop_counter(poop_count, game_running))
        if game_running == False:
            print("***GAME OVER***")    
        
def good_morning_spencer(date):
    print("Good morning, Spencer!")
    print("Today is Day " + str(date))
    
def where_is_spencer(current_location):
    here_he_is = "Spencer's location: " + current_location
    print(here_he_is)

def poop_counter(poop_count, game_running):
    if poop_count <= 0:
            print("\n")
    if poop_count == 1:
            print("Spencer feels a slight rumbling deep within his bowels. \n He realizes he might want to make his way to a toilet.")
    if poop_count == 2:
            print("The pressure in Spencer's intestines increases. \n Some discomfort ensues, and Spencer's thoughts turn \n once again to his porcelain throne.")
    if poop_count == 3:
            print("A spasm passes through Spencer's midsection, \n almost as if he is going into labor. He gasps and staggers. \n He realizes that the situation is more dire than he thought, \n and he must make it to his toilet quickly.")
    if poop_count == 4:
            print("Sweat streams down Spencer's ruddy face as he clenches \n his mighty cheeks against the ruthless assault from within him, \n but he feels his strength beginning to fade. \n If he does not reach his toilet immediately, all hope is lost.")
    elif poop_count >= 5: 
            print("Tears of embarrassment mingle with the lake of sweat \n and pile of feces on Spencer's floor. \n Thanks to your mismanagement, he has been forced \n to soil himself. You lose.")
            game_running = False
            return game_running
    
def bedroom_move(current_location, in_bedroom):
        destination = input("Where would Spencer like to go? \n")
        if current_location in str(destination.split(" ")):
            print("You're already there, you lazy sack of shit")
            return current_location, in_bedroom
        else:
            if "bed" in destination:
                print("Spencer gets in bed")
                current_location = "bed"
                return current_location, in_bedroom
            if ("chair" or "couch" or "sofa") in destination:
                print("Spencer gets up and sits in his chair")
                current_location = "chair"
                return current_location, in_bedroom
            if ("floor") in destination:
                print("Spencer lies on the floor. It soothes him.")
                current_location = "floor"
                return current_location, in_bedroom        
            if ("closet") in destination:
                print("Spencer hides in his closet")
                current_location = "closet"
                return current_location, in_bedroom
            if "out" in destination or "door" in destination or "leave" in destination:
                door_choice = input("Go out the kitchen door or back door? \n")
                if "kitchen" in door_choice:
                    print("Spencer goes out the kitchen door")
                    current_location = "kitchen door"
                    in_bedroom = False
                    return current_location, in_bedroom     
                if "back" in door_choice:
                    print("Spencer goes out the back door")
                    current_location = "back door"
                    in_bedroom = False
                    return current_location, in_bedroom
                else:
                    print("That's not an option, stupid")
                    return current_location, in_bedroom
            else: 
                print("That's not an option, stupid")
                return current_location, in_bedroom

def random_bedroom_event(poop_count):
    import random
    mystery_number = random.randint(1,100)
    if mystery_number <= 20:
        print("Spencer lets out a tremendous fart. \n The pressure in his bowels decreases.")
        poop_count -= 1
        return poop_count
    if mystery_number > 20 and mystery_number <= 30:
        print("Spencer's feet become entangled in some of the \n extremely tight briefs he has strewn all aroud his bedroom. \n He crashes to the ground, and as a spike \n of agony shoots through his bowels, he realizes \n he has exacerbated his predicament.")
        poop_count += 1
        return poop_count
    if mystery_number > 30 and mystery_number <= 35:
        print("Spencer glimpses a silhouette crouching in the shadows \n under his bed. Instantly, he recognizes in its shape \n the austere Slavic form of Polina. \n He gasps and involuntarily clenches his muscles, \n and then curses as the squeezing causes his fecal occupants \n to batter at his insides with increased fury \n in their quest for freedom. Amassing all his courage, \n he peers under his bed, only to find that the \n lurking shadow was nothing more than an apparition \n caused by a mass of plaid scarves.")
        poop_count += 1
        return poop_count
    if mystery_number >35 and mystery_number <= 40:
        print("As Spencer minds his own business, Thomas and Sarah \n fling open his back door, having opened it with the illicit \n spare key they obviously possess. The shock causes Spencer \n to stand bold upright, sending a sickening spasm \n through his nether regions.")
        poop_count += 1
        return poop_count
    if mystery_number >40 and mystery_number <=45:
        print("Suddenly, Spencer spies a vast barrel of \n cheese balls sitting in a corner of his room. \n He throws himself upon them, entering a \n semiconscious fog as he tears into them. \n When he comes to his senses, the balls have been \n decimated and he is powdered with \n a dusting of orange crumbs. He realizes \n that this massive low-fiber, high-cheese binge \n has greatly alleviated his intestinal emergency.")
        poop_count -= 2
        return poop_count
    if mystery_number >45 and mystery_number <=50:
        print("Two arms decorated with polytene tattoo sleeves \n emerge from the dark depths of Spencer's closet. \n It is Sewelle! Spencer ceases to register \n the passage of time as he is locked in her embrace... \n that is, until a wrenching jolt in his bowels reminds him \n that he has neglected the urgent matter at hand.")
        poop_count += 2
        return poop_count
    else:
        return poop_count

main()
    