#pygatchi

import random

#Define class Creature
class Creature():
    def __init__(self, name):
        """Initialize attributes"""
        self.name = name.title()

        #attributes to track playing game (0-10) 
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2    #food inventory
        self.is_sleeping = False   #is bool 
        self.is_alive = True    #is bool

#Defining the class methods
    def eat(self):
        """Creature will eat if it has food"""
        #eat food
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print("\n" + self.name + " has had a great meal!")
        else:
            print("\n" + self.name + " doesn't have any food to eat....")
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        """Creature will play a game with the player to help boredom"""
        #play game with user
        number = random.randint(0,2)
        print("\n" + self.name + " wants to play a game.")
        print(self.name + " is thinking of a number 0, 1, or 2")
        guess = int(input("What number is " + self.name + " thinking of: "))
        if guess == number:
            print("\nWell done, you guessed what number " + self.name + " is thinking of.")
            self.boredom -= 3
        else:
            print("\nooooh, sorry, that wasn't the correct number. " + self.name + " was thinking of " + str(number))
            self.boredom -=1
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        """Creature will sleep if it is tired"""
        #put creeture to sleep
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print("\n" + self.name + " is sleeping.")
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0
        
    def awake(self):
        """check if creature is alseep or not"""
        #sleeping
        number = random.randint(0,2)
        if number == 0:
            print("\n" + self.name + " just woke up.")
            self.is_sleeping = False
            self.tiredness = 0
        else:
            print("\n" + self.name + " won't wake up.")
            self.sleep()

    def clean(self):
        """Clean the creature and reset dirtiness to 0"""
        #clean creature
        self.dirtiness = 0
        print("\n" + self.name + " took a bath.")
    
    def forage(self):
        """creature will forage for food but increase dirtiness too"""
        #get food
        food_found = random.randint(0,4)
        self.food += food_found

        #gets dirty
        self.dirtiness += 2
        print("\n" + self.name + " has found " + str(food_found) + " pieces of food.")
    
    def show_values(self):
        """Show the different values the creature has"""
        #show info about creature
        print("\nCreature name: " + self.name)
        print("Hunger (0-10): " + str(self.hunger))
        print("Boredom (0-10): " + str(self.boredom))
        print("Tiredness (0-10): " + str(self.tiredness))
        print("Dirtiness (0-10): " + str(self.dirtiness))
        print("Pieces of food in inventory: " + str(self.food))

        #Show current sleeping status
        if self.is_sleeping:
            print("current status: Sleeping")
        else:
            print("Current status: Awake")
    
    def incriment_values(self, level):
        """Setting the difficulty level to start the game"""
        #difficult level setting
        self.hunger += random.randint(0, level)
        self.dirtiness += random.randint(0, level)
        if self.is_sleeping == False:
            self.boredom += random.randint(0,level)
            self.tiredness += random.randint(0,level)
        
    def kill(self):
        """different conditions where the creature will die or fall asleep"""
        #creature can die
        if self.hunger >= 10:
            print(self.name + " has starved to death.")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print(self.name + " suffered an infection and died.")
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print(self.name + " is bored and falling asleep.")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(self.name + " is sleepy and falling asleep.")
            self.is_sleeping = True

#Defining the functions
def show_menu(creature):
    """Player chooses what actions they wish to perform"""
    if creature.is_sleeping:
        action = input("\nPress 6 to wake them up: ")
        action = "6"
    else:
        print("\nEnter 1 to eat")
        print("Enter 2 to play")
        print("Enter 3 to sleep")
        print("Enter 4 to take a bath")
        print("Enter 5 to forage for food")
        action = input("What do you want to do: ")
        
    return action

def call_action(creature, choice):
    """perform method the player chooses"""
    #Call chosen method
    if choice == "1":
        creature.eat()
    elif choice == "2":
        creature.play()
    elif choice == "3":
        creature.sleep()
    elif choice == "4":
        creature.clean()
    elif choice == "5":
        creature.forage()
    elif choice == "6":
        creature.awake()
    else:
        print("Invalid option")

#main code

print("Welcome to the pygatchi simulation app")

#set difficulty level
difficulty = int(input("\nWhat difficulty would you like to play (1-5): "))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1

#main game loop
playing = True
while playing:
    #user input for name and create creature
    name = input("\nWhat is the name of your Pygatchi? ")
    player = Creature(name)
    rounds = 1
    #game loop that simulates 1 round
    #this will run as long as creature is alive

    while player.is_alive:
        print("\n-------------------------------------------------")
        print("\nRound #" + str(rounds))

#each round shows values, gets next move, and calls chosen method
        player.show_values()
        round_move = show_menu(player)
        call_action(player, round_move)

        print("\nRound # " + str(rounds) + " Summary: ")

        #summary of last round
        player.show_values()
        input("\nPress Enter to continue.....")

        #incriment values and check for death
        player.incriment_values(difficulty)
        player.kill()

        #round is over
        rounds += 1

#creature dies
    print("Your Pygatchi has died, you're a terrible owner.")
    print(player.name + " survived for " + str(rounds) + " rounds.")
    
    
#ask to play again
    again = input("Would you like to play again (y/n): ").lower()
    if again != "y":
        playing = False
        print("\nThankyou for playing")



