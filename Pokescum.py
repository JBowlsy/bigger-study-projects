#Elements = drunk, grease, tank   drunk > grease > tank > drunk

import random

#Parent class
class Pokescum():
    """Model of pokescum charater (Parent class)"""

    def __init__(self, name, element, health, speed):
        """attributes"""
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True
    
    def light_attack(self, enemy_pokescum):
        """a light attack that will always cause some damage, set at index 0"""
        damage = random.randint(15, 25)
        print("\n" + self.name + " used " + self.moves[0] + "!")
        print("\nIt does " + str(damage) + " damage.")
        enemy_pokescum.current_health -= damage

    def heavy_attack(self, enemy_pokescum):
        """a heavy attack that could potentially miss, set at index 1"""
        damage = random.randint(0, 50)
        print("\n" + self.name + " used " + self.moves[1] + "!")
        
        #dealing 0 damage
        if damage < 10:
            print("\nOh no, " + self.name + "'s " + self.moves[1] + " missed!")
        else:
            print("\n" + str(damage) + " damage was inflicted.")
            enemy_pokescum.current_health -= damage

    def restore(self):
        """players pokescum does nothing but recovers a portion of their health instead, set at index 2"""
        heal = random.randint(15, 25)
        print("\n" + self.name + " consumed " + self.moves[2] + ".")
        print(self.name + " recovered " + str(heal) + " health points.")
        
        #heal self
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        
    def faint(self):
        """pokescum loses all health points and faints"""
        if self.current_health <= 0:
            self.is_alive = False
            print("\n" + self.name + " fainted.")
            input("\nPress Enter to continue")

    def show_stats(self):
        """Show the stats of the pokescum"""
        print("\nName: " + self.name)
        print("Element: " + self.element)
        print("Health: " + str(self.current_health) + "/" + str(self.max_health))
        print("Speed: " + str(self.speed))

#child classes
class Drunk(Pokescum):
    """first element 'Drunk' in the pokescum (child class)"""
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Can Toss','Headbutt', 'Smeg', 'Tongue biter'] #light attack, heavy attack, recover, special move

    def special_attack(self, enemy_pokescum):
        """high damage against grease, minimal against tank, normal against drunk"""
        print("\n" + self.name + " uses " + self.moves[3] + "!")

        #cause damage based on element
        if enemy_pokescum.element == 'GREASE':
            print("\nThe attack was super effective!")
            damage = random.randint(35, 50)
        elif enemy_pokescum.element == 'TANK':
            print("\nThe attack was not very effective...")
            damage = random.randint(2, 10)
        else:
            damage = random.randint(10, 30)

        print("\nThe attack dealt " + str(damage) + " hit points.")
        enemy_pokescum.current_health -= damage

    def move_info(self):
        """Show pokescum moves information"""
        print("\n" + self.name + "'s move list.")
        print("Can Toss: light attack (15-25: hit points)")
        print("Headbutt: heavy attack (0-50: hit points)")
        print("Smeg: Recovery (15-25: health points)")
        print("Tongue Biter: Special attack (?: hit points)")

class Grease(Pokescum):
    """second element 'Grease' in the pokescum (child class)"""
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Flying fox', 'Big Badger', 'Urinal Cakes', 'Suck'] #light attack, heavy attack recover, special move

    def special_attack(self, enemy_pokescum):
        """high damage against Tank, minimal against Drunk, normal against Grease"""
        print("\n" + self.name + " uses " + self.moves[3])
        if enemy_pokescum.element == 'TANK':
            print("\nThe attack was super effective!")
            damage = random.randint(35, 50)
        elif enemy_pokescum.element == 'DRUNK':
            print("\nThe attack was not very effective...")
            damage = random.randint(2, 10)
        else:
            damage = random.randint(10, 30)
        print("\nThe attack dealt " + str(damage) + " hit points.")
        enemy_pokescum.current_health -= damage

    def move_info(self):
        """Show moves information"""
        print("\n" + self.name + "'s move list.")
        print("Flying Fox: light attack (15-25: hit points)")
        print("Big Bagder: heavy attack (0-50: hit points)")
        print("Urinal Cakes: Recovery (15-25: health points)")
        print("Suck: Special attack (?: hit points)")

class Tank(Pokescum):
    """Third element 'Tank' in the pokescum (child class)"""
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Rat trap', 'Vomit', 'Piss', 'Poop throw'] #light attack, heavy attack recover, special move

    def special_attack(self, enemy_pokescum):
        """high damage against grease, minimal against tank, normal against drunk"""
        print("\n" + self.name + " uses " + self.moves[3])
        if enemy_pokescum.element == 'DRUNK':
            print("\nThe attack was super effective!")
            damage = random.randint(35, 50)
        elif enemy_pokescum.element == 'GREASE':
            print("\nThe attack was not very effective...")
            damage = random.randint(2, 10)
        else:
            damage = random.randint(10, 30)
        print("\nThe attack dealt " + str(damage) + " hit points.")
        enemy_pokescum.current_health -= damage

    def move_info(self):
        """shows information about the moves available to player"""
        print("\n" + self.name + "'s move list.")
        print("Rat trap: light attack (15-25: hit points)")
        print("Vomit: heavy attack (0-50: hit points)")
        print("Piss: Recovery (15-25: health points)")
        print("Poop throw: Special attack (?: hit points)")

#Game class
class Game():
    """Game object to create the game and control the flow"""

    def __init__(self):
        """attributes"""
        self.pokescum_elements = ['DRUNK', 'GREASE', 'TANK']
        self.pokescum_names = ['Folwell', 'Kamal', 'Walrus', 'Selwood', 'Hobo', 'Coyote', 'Phantom']
        self.battles_won = 0

    def create_pokescum(self):
        """randomly create the pokescum characteristics for the game"""
        health = random.randint(70, 100)
        speed = random.randint(1, 10)

        #randomly choose elemtn and name
        element = self.pokescum_elements[random.randint(0, len(self.pokescum_elements)-1)]
        name = self.pokescum_names[random.randint(0, len(self.pokescum_names)-1)]
        
        #create the correct pokescum
        if element == 'DRUNK':
            pokescum = Drunk(name, element, health, speed)
        elif element == 'GREASE':
            pokescum = Grease(name, element, health, speed)
        else:
            pokescum = Tank(name, element, health, speed)

        return pokescum

    def choose_pokescum(self):
        """a list holdng 3 starting pokescum"""
        starters = []
        while len(starters) < 3:
            pokescum = self.create_pokescum()

            """check it has unique characteristics"""
            valid_pokescum = True
            for starter in starters:
                if starter.name == pokescum.name or starter.element == pokescum.element:
                    valid_pokescum = False
            if valid_pokescum:
                starters.append(pokescum)

        for starter in starters:
            starter.show_stats()
            starter.move_info()
        
        print("\nProfessor Roadkill presents 3 Pokescum")
        print("(1) " + starters[0].name)
        print("(2) " + starters[1].name)
        print("(3) " + starters[2].name)

        choice = int(input("Which pokescum would you like to choose: "))
        pokescum = starters[choice-1]

        return pokescum

    def get_attack(self, pokescum):
        """get the players choice of move after giving the options"""
        print("\nMove options: ")
        print("(1) " + pokescum.moves[0])
        print("(2) " + pokescum.moves[1])
        print("(3) " + pokescum.moves[2])
        print("(4) " + pokescum.moves[3])
        choice = int(input("Select your move: "))
       
        print()

        print("-------------------------------------------------------")

        return choice

    def player_attack(self, move, player, computer):
        """Attack the computer"""
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        #check to see if computer died
        computer.faint()

    def computer_attack(self, player, computer):
        """Computer attacks player"""
        #randomly choose move for comp to do
        move = random.randint(1, 4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)

        #check to see if player died
        player.faint()

    def battle(self, player, computer):
        """faster pokescum goes first"""
        #get players move
        move = self.get_attack(player)

        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)

#main code
print("\nWelcome to your first Pokescum adventure.")
print("Professor Roadkill will let you choose your first Pokescum to fight with")
print("You will keep fighting until your pokescum dies.")
input("Press Enter to continue")

playing_main = True
while playing_main:
    #create game instance
    game = Game()

    #choose pokescum
    player = game.choose_pokescum()
    print("\nYou have chosen " + player.name + "!")
    input("Press Enter to begin your adventure")


    while player.is_alive:
        #choose pokescum for computer
        computer = game.create_pokescum()
        print("\nEurgh disgusting! A wild " + computer.name + " has crawled out of the bins!")
        computer.show_stats()

        #battle while both pokescum are alive
        while computer.is_alive and player.is_alive:
            game.battle(player, computer)

            #both are still alive after a roun, show stats
            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()

        print("------------------------------------------------")
            
            #player survives +battle, increment battles won
        if player.is_alive:
            game.battles_won += 1

    #players pokescum dies
    print("\nOh shit, " + player.name + " has died!")
    print("You have managed to defeat " + str(game.battles_won) + " pokescum!")

        #ask player to play again
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != 'y':
        playing_main = False
        print("Thankyou for playing Pokescum.\n")
