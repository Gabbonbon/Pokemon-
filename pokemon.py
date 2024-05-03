import random
battle_catch = ""
xp = 0
money = 1000
catch_system = random.randint(1,2)
pokeball = 0
potion = 0
party_size = 0
hp = 100
catch_system = ""
pokedex = []
old_amber = 0
badges = 0
box_ans = ""
pokemon_put_into_box = []
def pc_box():
   print("The boox is capable of putting already caught pokemon into a box just in case. You can also easily take them out if you want to train or use them.") 
   box_ans = input("Would you like to put a pokemon into the box")
   if box_ans == "yes":
         pokemon_put_into_box = input("What pokemon would you like to put into the box")
         pokemon_put_into_box = pokemon_put_into_box
         print ("You have added" +  str(pokemon_put_into_box))
         pokemon_put_into_box.append(pokemon_put_into_box)
   else:
      
      print("You do not put a pokemoon into the box")
if money < 1000:
   print("You don't have enough money, you cannot spend")
   money = money - 1000
   print("You now have " + str(money) + " money")
if money > 10000:
    print("Your bank is full, spend some money")
if party_size > 6:
  print("You can't have more than 6 pokemon in your party")
if hp < 100:
   print("Game over")
   exit()
def gym_1():
      print("Trainer 1: Stop right there, kid! You're still light years from facing BROCK!")
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
         print("Trainer 1: Darn! Light years isn't time! It measures distance!")
         xp = xp + 10
         print(xp)
         money = money + 1000
         print("You got 1000 pokedollars")
         print(money)
      elif battle_result == "no":
         print("Trainer 1: I'm sorry, but you're too far away!")
         print("You lost 1000 pokedollars")
         pokedollars = pokedollars - 1000
         hp = hp - 30
      print("Brock: I'm BROCK! I'm PEWTER's GYM LEADER! I believe in rock hard defense and determination! That's why my POKEMON are all the rock-type! Do you still want to challenge me? Fine then! Show me your best!")
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
         print("Brock: I took you for granted. As proof of your victory, here's the BOULDERBADGE! That's an official POKEMON LEAGUE BADGE Its bearer's POKEMON become more powerful!")
         badges = badges + 1
         print("Brock: There are all kinds of trainers in the world! You appear to be very gifted as a POKENON trainer! Go to the GYM in CERULEAN and test your abilities!")
      else:
         print("You Lost!")
         exit()
def potion():
  potion_use = input("Do you use a potion?")
  if potion_use == "yes":
     print("You use a potion!")
     potion = potion - 1
     hp = hp + 35
     print("You now have " + str(hp) + " hp")






def battle():
  xp = 0
  player_choice = input("Do you attack")  
  damage_amount = random.randint(1,10)
  enemy_damage_amount = random.randint(1,10)
  if player_choice == "yes":
    print("You attacked the pokemon and dealt " + str(damage_amount) + " damage")
    print("The wild pokemon attacked you and dealt"+ str(enemy_damage_amount) + " damage")
    if damage_amount < enemy_damage_amount:
      print("You lost")
    else:
      print("You won")
      xp = xp + 10
  if player_choice == "no":
     print("Game over")
     exit()

print("In this text based pokemon game using the pokemon yellow version script with some minor changes and improvements the battle system is way more different then what pokemon games have used before, this is to simpillify and have the game be more fun and enjoyable for the player. ")

print("----------------------------------------------")

print("An image of a man in a labcoat appears")
print("Oak: Hello there! Welcome to the world of POKEMON! My name is OAK! People call me the POKEMON PROF!")
print("An image of Nidorino appears")
print("Oak: This world is inhabited by creatures called POKEMON! For some people, POKEMON are pets. Others use them for fights. Myself...I study POKEMON as a profession")

gender = input("Are you a girl or a boy?")
if gender == "boy":
    print("A image of a boy appears")
else:
    print("A image of a girl appears")

player_name = input("Oak: First, what is your name?")
print("So your name is " + player_name)
print("An image of a different boy appears")
print("Oak: This is my grandson. He's been your rival since you were a baby. ")

rival_name = input("...Erm, what is his name again?")

print("Oak: Right! So his name is " + rival_name)
print(rival_name + "'s image appears")

print("Oak:" + player_name + "! Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!")

print("You awake in your home.")
print("Mother: " + player_name + "! Wake up! Time to go to the lab! Go to "+ rival_name + "'s home first to pick him up, today is the day you get your first POKEMON")
print("You go to "+ rival_name + "'s home")
print("You see "+ rival_name + "'s sister and a map")
print(rival_name + "sister: Hi, my big bro is out at Grandpa's lab.")
map_1 = input("Do you want to take the map?")
if map_1 == "yes":
  print("It's a big map! This is useful! You take the map")
else:
  print("You don't take the map")
print("You go to the PROF.OAK's lab")

print(rival_name + ": Yo, gramps isn't around, i'm pretty sure he is outside")
print("You go outside and walk to the grassy path")
print("Oak: Hey! Wait! Don't go out!")
print("Oak approaches you")
print("Oak: It's unsafe! Wild POKEMON live in tall grass! You need your own POKEMON for your protection. I know! Here, come with me!")
print("He takes you to his laboratory. They approach a table upon which three Poke Balls have been placed, and next to which" + rival_name + " is present")
print(rival_name + "Gramps! I'm fed up with waiting!")
print("Oak: Let me think... Oh, that's right, I told you to come! Just wait!")
print("Here, There are 3 POKEMON here! Haha! They are inside the POKE BALLS. When I was young, I was a serious POKEMON trainer. In my old age, I have only 3 left, but you can have one! Choose!")
print(rival_name + "Hey! Gramps! What about me?")
print("Oak: Be patient! " + rival_name + "! you can have one too!")
print("Now" + player_name + "! It's time to choose your first POKEMON!")
print("The three available Pokemon are Bulbasaur, Charmander, and Squirtle.")


starter = input("Which Pokemon will you choose?").lower()

if starter == "bulbasaur":
  print("You chose Bulbasaur")
  print(rival_name + ": I choose you, Charmander!")
  party_size = party_size + 1
  hp = 100
  pokedex.append("Bulbasaur")
elif starter == "charmander":
  print("You chose Charmander")
  print(rival_name + ": I choose you, Squirtle!")
  party_size = party_size + 1
  hp = 100
  pokedex.append("Charmander")
else:
  print("You chose squirtle")
  print(rival_name + ": I choose you, Bulbasaur!")
  party_size = party_size + 1
  hp = 100
  pokedex.append("Squirtle")

print("Oak: If a wild POKEMON appears, your POKEMON can fight against it!")
print(rival_name + ": My POKEMON looks a lot stronger.")
print("You look at the third pokeball")
print("3rd Ball: That's PROF.OAK's last POKEMON!")
print( rival_name + "Let's check out our POKEMON! Come on, I'll take you on in our first pokemon battle!")
battle()
battle_result = input("Did you win?")
if battle_result == "yes":
  print(rival_name + ": WHAT? Unbelievable! I picked the wrong POKEMON!")
  xp = xp + 10
  print(xp)
  money = money + 1000
  print("You got 1000 pokedollars") 
else:
  print(rival_name + ": Yeah! Am I great or what?")
  hp = hp - 30
  print("You lost 30 hp")
print(rival_name + ": Okay! I'll make my POKEMON fight to toughen it up! " + player_name + "! Gramps! Smell you later!")
print(rival_name + "takes his leave from the labatory and town.")
print("As you leave Oak says...")
print("Oak: " + player_name + "train your pokemon to be the best they can be! by fighting.")
print("You go back home to say goodbye to your mother.")
print("Mother:" + player_name + "You should take a quick rest.Oh good! You and your POKEMON are looking great! Take care now!")
print("You go to route one to start your journey by catching pokemon. ")
print("You see tall grass to catch a pokemon and a pokemart")



place_1 = input("Where do you want to go?")
if place_1 == "pokemart":
  print("You go to the pokemart")
  print("Seller: Hello! Welcome to the pokemart!")
  print("Seller:  Hi! I work at a POKEMON MART. It's a convenient shop, so please visit us in VIRIDIAN CITY. I know, I'll give you a sample! Here you go!")
  print("You get 3 potions and 3 pokeballs")
  potion = potion + 3
  pokeball = pokeball + 3
  print("Customer: See those ledges along the road? It's a bit scary, but you can jump from them. You can get back to PALLET TOWN quicker that way.")
  pokemart_1 = input("Would you like to buy a potion or a pokeball?")
  if pokemart_1 == "potion":
    print("You spend 100 pokedollars on a potion")
    money = money - 100
    print(money)
    potion = potion = 1
    print("You exit the pokemart and head to Viridian city")
  elif pokemart_1 == "pokeball":
    print("You spend 100 pokedollars on a pokeball")
    money = money - 100
    print(money)
    pokeball = pokeball + 1
    print("You exit the pokemart and head to Viridian city")

elif place_1 == "tall grass":
    print("You go to the tall grass")
    print("You see a pidgey")
    battle_catch = input("Do you want to catch or battle it")
    if battle_catch == "catch":
        print("You throw a pokeball at the pidgey")
        def catch():
         catch_system 
        catch_system = random.randint(1,2)
        catch()
        if catch_system == 1:
            party_size = party_size + 1
            print("You caught the pidgey")
            print("You spend 1 pokeball on the pidgey")
            pokedex.append("Pidgey")
            
        elif catch_system == 2:
            print("the pidgey ran away") 


    if battle_catch == "battle": 
        battle()
        battle_result = input("Did you win?")
        if battle_result == "yes":
            xp = xp + 10
            print(xp)
            money = money + 1000
            print("You got 1000 pokedollars")
            print(money)
        elif battle_result == "no":
            xp = xp + 5
            print(xp)
            money = money + 500
            print("You got 500 pokedollars")
            print(money)
            hp = hp - 30
            
            print("You lost 30 hp")
            potion()

    item_search_route1 = input("Would you like to search the grass?")
    if item_search_route1 == "yes":
        print("You search the grass")
        print("You find a potion")
        potion = potion + 1
        print(potion)
        print("You don't search the grass and continue your journey towads VIRIDIAN CITY")

    else:
        print("You don't search the grass and continue your journey towads VIRIDIAN CITY")
        print("You go to VIRIDIAN CITY")
        print("Viridian city the eternally green paradise")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("An old man is lying in the middle of a path; his granddaughter is standing next to him")
print("Girl: Oh Grandpa! Don't be so mean! He hasn't had his coffee yet.")
print("Grandpa: You can't go through here! This is private property!")
print("Grandpa: Oh! You are a POKEMON trainer! Go to the pokemon center!.")
print("You go to the pokemon center")
print("You see three people")
print("Guy: There's a POKEMON CENTER in every town ahead. They don't charge any money either!")
print("Buisness woman: POKEMON CENTERS heal your tired, hurt or fainted POKEMON!")
def pokemon_center():
  pokemon_center = input("Do you heal your pokemon?")
  if pokemon_center == "yes":
    global hp 
    hp = hp + 60
    print("You heal your pokemon" + str(hp))
  else:
    print("You don't heal your pokemon")
    print(hp)
    pc_box()
pokemon_center()
print("You exit the pokemon center and head to the pokemart")
print("Clerk: Hey! You came from PALLET TOWN? You know PROF.OAK, right? His order came in. Will you take it to him?")
print("He gives you Oak's parcel")
print("Clerk: Okay! Say hi to PROF.OAK for me!")
print("To make sure the parcel gets delivered quickly,you go the faster route back to pallet town that the nice customer told you about")
print("You enter Oak's lab")
print("Oak: Oh! " + player_name + "How is my old POKEMON? Well, it seems to like you a lot. You must be talented as a POKEMON trainer! What? You have something for me?")
print("You give the parcel to Oak")
print("Oak: Ah! this is the custom pokeball I ordered thank you")
print(rival_name + "enters the building.")
print(rival_name + "Gramps! What did you call me for?")
print("Oh right! I have a request of you two. On the desk there is my invention, POKEDEX! It automatically records data on POKEMON you've seen or caught! It's a hi-tech encyclopedia!")
print("You and " + rival_name + " obtain the pokedex")
print("You look in the pokedex")
print(pokedex)
print("Oak: To make a complete guide on all the POKEMON in the world... That was my dream! But, I'm too old! I can't do it! So, I want you two to fulfill my dream for me! Get moving, you two! This is a great undertaking in POKEMON history!")
print(rival_name + ":Alright Gramps! Leave it all to me! I know! I'll borrow a TOWN MAP from my sis!")
print(rival_name + "leaves the labatory")
print("You leave the labatory, but see a pokemon gym and walk up to it")
print("A man is standing by a pokemon gym.")
print("Man: This pokemon gym is always closed. I wonder who the leader is?")
print("You try to enter the gym")
print("Gym doors: The gym is always locked.")
print("Man: If you ever want to challenge a gym you should catch more pokemon, the more you have the easier it is to fight")
print("You go to Route 2 to continue your journey to pewter city ")
print("Bug Catcher: Hey! You are a POKEMON trainer! Lets battle.")
battle()
battle_result = input("Did you win?")
if battle_result == "yes":
    xp = xp + 10
    print(xp)
    money = money + 1000
    print("You got 1000 pokedollars")
    print(money)
    print("Bug Catcher: I give! You're good at this!")
else:
   xp = xp + 10
   print(xp)
   money = money + 500
   print("You got 500 pokedollars")
   print(money)
   print(" Bug Catcher: Ssh! You'll scare the bugs away")
print("You see another pokemon trainer")
print("DJ: Yo! You can't jam out if you're a POKEMON trainer!")
battle()
battle_result = input("Did you win?")
if battle_result == "yes":
    xp = xp + 10
    print(xp)
    money = money + 1000
    print("You got 1000 pokedollars")
    print(money)
    print("DJ: Huh! I ran out of pokemon")
else:
   xp = xp + 10
   print(xp)
   money = money + 500
   print("You got 500 pokedollars")
   print(money)
   print("Use the music to guide you")
potion()
print("You see a Caterpie and a Rattata")
route_2_catch = input("Do you want to try the rattata or caterpie first?")
if route_2_catch == "rattata":
   print("You go to the rattata")
   battle_catch = input("Do you want to catch or battle it")
   if battle_catch == "catch":
       print("You throw a pokeball at the rattata")
       def catch():
        catch_system 
       catch_system = random.randint(1,2)
       catch()
       if catch_system == 1:
           party_size = party_size + 1
           print("You caught the rattata")
           print("You spend 1 pokeball on the rattata")
           pokeball = pokeball - 1
           pokedex.append("Rattata")
           print(pokedex)
       elif catch_system == 2:
           print("the rattata ran away")
   elif battle_catch == "battle":
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
            xp = xp + 10
            print(xp)
            money = money + 1000
            print("You got 1000 pokedollars")
            print(money)
      elif battle_result == "no":
            xp = xp + 5
            print(xp)
            money = money + 500
            print("You got 500 pokedollars")
            print(money)
            hp = hp - 30
            
            print("You lost 30 hp")

else:
   print("You go to the caterpie")
   battle_catch = input("Do you want to catch or battle it")
   if battle_catch == "catch":
       print("You throw a pokeball at the caterpie")
       def catch():
        catch_system 
       catch_system = random.randint(1,2)
       catch()
       if catch_system == 1:
           party_size = party_size + 1
           print("You caught the caterpie")
           print("You spend 1 pokeball on the caterpie")
           pokeball = pokeball - 1
           pokedex.append("caterpie")
           print(pokedex)
       elif catch_system == 2:
           print("the caterpie ran away")
   elif battle_catch == "battle":
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
            xp = xp + 10
            print(xp + "Xp")
            money = money + 1000
            print("You got 1000 pokedollars")
            print(money)
      elif battle_result == "no":
            xp = xp + 5
            print(xp + "Xp")
            money = money + 500
            print("You got 500 pokedollars")
            print(money)
            hp = hp - 30
            print("You lost 30 hp")
print("You make it to the pewter city")
print("Pewter City, A stone gray city")
print("Signpost: In the rock solid Pewter city, there is the world famous museum,pokemon center, pokemart and the pokemon gym")
print("Signpost: Thieves have been stealing POKEMON fossils at MT.MOON! Please call PEWTER POLICE with any info!")
print("You see a a man coming to talk to you")
museum = input("Man: Did you check out the museum?")
if museum == "yes":
    print("Man: Weren't those fossils from MT.MOON amazing?")
else:
   print("Man: Really? you aboulutley have to check out the museum")
print("He takes you to the museum")
print("It's right here! You have to pay to get in but it's worth is see you around!")
museum = input("Do you want to pay for the museum?")
if museum == "yes":
    money = money - 1000
    print("You paid 1000 pokedollars")
    print(money)
    print("You enter the museum")
    print("The museum is full of POKEMON fossils")
    print("Sorry, we just got some fossils in, we can't let you in, but I will give you something for your troubles")
    print("The person gives you 3 pokeballs")
    pokeball = pokeball + 3


else:
   print("You didn't pay for the museum")
   print(str(money) + "Money")


print("A woman runs up to you")
print("Woman: You're a trainer right? BROCK's looking for new challengers! Follow me!")
print("She takes you to the pokemon gym")
prepare = input("Woman: If you have the right stuff go take on BROCK")
if prepare == "yes":
   print("You see a signpost")
   print("PEWTER CITY GYM, LEADER: BROCK, The rock solid POKEMON trainer")
   print("You enter the gym")
   def gym_1():
      print("Trainer 1: Stop right there, kid! You're still light years from facing BROCK!")
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
         print("Trainer 1: Darn! Light years isn't time! It measures distance!")
         xp = xp + 10
         print(xp)
         money = money + 1000
         print("You got 1000 pokedollars")
         print(money)
      elif battle_result == "no":
         print("Trainer 1: I'm sorry, but you're too far away!")
         print("You lost 1000 pokedollars")
         pokedollars = pokedollars - 1000
         hp = hp - 30
      potion()
      print("Brock: I'm BROCK! I'm PEWTER's GYM LEADER! I believe in rock hard defense and determination! That's why my POKEMON are all the rock-type! Do you still want to challenge me? Fine then! Show me your best!")
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
         print("Brock: I took you for granted. As proof of your victory, here's the BOULDERBADGE! That's an official POKEMON LEAGUE BADGE Its bearer's POKEMON become more powerful!")
         badges = badges + 1
         print("Brock: There are all kinds of trainers in the world! You appear to be very gifted as a POKENON trainer! Go to the GYM in CERULEAN and test your abilities!")
   gym_1()

else:
   print("You think the museum is probably open by now")
   place_1 = input("Do you go to the museum?, pokemart or pokemon center?")
   if place_1 == "museum":
      print("You go to the museum")
      print("Scientist: Here is your ticket, free of charge since you paid before")
      print("You enter the museum")
      print("Exhibit A: AERODACTYL Fossil. A primitive and rare POKEMON.")
      print("Exhibit B: KABUTOPS Fossil.A primitive and rare POKEMON.")
      print("Exhibit C: Meteorite that fell on MT.MOON. (MOON STONE?)")
      print("Woman: That is one magnificent fossil!")
      print("Man: MOON STONE? What's so special about it?")
      print("Scientist: Your a pokemon trainer. Shh, follow me!")
      amber = input("Scientist: Do you know what amber is?")
      if amber == "yes":
         print("Scientist: There's a lab somewhere trying to resurrect ancient POKEMON from AMBER.")
      elif amber == "no":
         print("Scientist: AMBER is fossilized tree sap")
      print("Scientist: Ssh! I think that this chunk of AMBER contains POKEMON DNA! It would be great if POKEMON could be resurrected from it! But, my colleagues just ignore me! So I have a favor to ask! Take this to a POKEMON LAB and get it examined!")
      print("You get the Old Amber")
      old_amber = old_amber + 1
      print("You exit the museum and head to the gym")
      print("You enter the gym")
      gym_1()

   elif place_1 == "pokemart":
      print("You go to the pokemart")
      print("Store Clerk: Sorry, our payment isn't working, but you can have this")
      pokeball = pokeball + 1
      print("You get 1 pokeball on the pokemart")
      print(pokeball)
      print("You exit the pokemart and head to the gym")
      print("You enter the gym")
      gym_1() 

   else:
      print("You enter the pokemon center")
      pokemon_center()
      print("You exit the pokemon center and head to the gym")
      print("You enter the gym")
      gym_1() 
          
print("You have completed your goal in Pewter City, so you continue to Route 3 to enter Mt.MOON")
print("Lass: You looked at me, didn't you?")
battle()
battle_result = input("Did you win?")
if battle_result == "yes":
   pokedollars = 1000
   print("Lass: You're mean!")
   print("You lost 1000 pokedollars")
   pokedollars = pokedollars + 1000
elif battle_result == "no":
   pokedollars = 1000
   pokedollars = pokedollars + 500
   print("Lass: Quit staring if you don't want to fight")
   print("You gained 500 pokedollars")
   print(pokedollars + "Pokedollars")
   hp = hp - 30
   print("You lost 30 hp")
   print(hp + "Hp")
print("Bug Catcher: Hey! I met you in VIRIDIAN FOREST!")
battle()
battle_result = input("Did you win?")
if battle_result == "yes":
   pokedollars = 1000
   print("Bug Catcher: You beat me again!")
   print("You lost 1000 pokedollars")
   pokedollars = pokedollars + 1000
elif battle_result == "no":
   pokedollars = 1000
   pokedollars = pokedollars + 500
   print("Bug Catcher: There are other kinds of pokemon than those in the forest")
   print("You gained 500 pokedollars")
   print(pokedollars + "Pokedollars")
   hp = hp - 30
   print("You lost 30 hp")
   print(hp + "Hp")
potion()  
print("Youngster: Hi! I like shorts! They're comfy and easy to wear!")
battle()
if battle_result == "yes":
   pokedollars = 1000
   print("Youngster: I don't believe it!")
   print("You lost 1000 pokedollars")
   pokedollars = pokedollars + 1000
elif battle_result == "no":
   pokedollars = 1000
   pokedollars = pokedollars + 500
   print("Youngster: maybe you should try wearing shorts")
   print("You gained 500 pokedollars")
   print(pokedollars + "Pokedollars")
   hp = hp - 30
   print("You lost 30 hp")
   print(hp + "Hp")

print("Bug Catcher: Are you a trainer? Let's fight!")
battle()
if battle_result == "yes":
   pokedollars = 1000
   print("Bug Catcher: If I had a new pokemon I would've won!")
   print("You lost 1000 pokedollars")
   pokedollars = pokedollars + 1000
elif battle_result == "no":
   pokedollars = 1000
   pokedollars = pokedollars + 500
   print("Bug catcher: Maybe you should go catch a pokemon in the forest")
   print("You gained 500 pokedollars")
   print(pokedollars + "Pokedollars")
   hp = hp - 30
   print("You lost 30 hp")
   print(hp + "Hp")
print("You see a Jigglypuff and a Mankey")
route_3_catch  = input("Would you like to go and catch/battle the jigglypuff or a mankey").lower()  
if route_3_catch == "jigglypuff":
   print("You go to the jigglypuff")
   battle_catch = input("Do you want to catch or battle it")
   if battle_catch == "catch":
       print("You throw a pokeball at the jigglypuff")
       def catch():
        catch_system 
       catch_system = random.randint(1,2)
       catch()
       if catch_system == 1:
           party_size = party_size + 1
           print("You caught the jigglypuff")
           print("You spend 1 pokeball on the jigglypuff")
           pokeball = pokeball - 1
           pokedex.append("Jigglypuff")
           print(pokedex)
       elif catch_system == 2:
           print("the jigglypuff ran away")
   elif battle_catch == "battle":
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
            xp = xp + 10
            print(xp)
            money = money + 1000
            print("You got 1000 pokedollars")
            print(money)
      elif battle_result == "no":
            xp = xp + 5
            print(xp)
            money = money + 500
            print("You got 500 pokedollars")
            print(money)
            hp = hp - 30
            
            print("You lost 30 hp")

else:
   print("You go to the mankey")
   battle_catch = input("Do you want to catch or battle it")
   if battle_catch == "catch":
       print("You throw a pokeball at the mankey")
       def catch():
        catch_system 
       catch_system = random.randint(1,2)
       catch()
       if catch_system == 1:
           party_size = party_size + 1
           print("You caught the mankey")
           print("You spend 1 pokeball on the mankey")
           pokeball = pokeball - 1
           pokedex.append("Mankey")
           print(pokedex)
       elif catch_system == 2:
           print("the mankey ran away")
   elif battle_catch == "battle":
      battle()
      battle_result = input("Did you win?")
      if battle_result == "yes":
            xp = xp + 10
            print(xp + "Xp")
            money = money + 1000
            print("You got 1000 pokedollars")
            print(money)
      elif battle_result == "no":
            xp = xp + 5
            print(xp + "Xp")
            money = money + 500
            print("You got 500 pokedollars")
            print(money)
            hp = hp - 30
            print("You lost 30 hp")
print("You have reached the end of Route 3 and enter Mt.MOON")
print(pokedex + "pokemon entries in your pokedex file")
print(party_size + "Pokemon in your party")
qqqqq = 2
for i in range(qqqqq):
   print("hello")
