# Define a Fighter class to represent each fighter
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name  # Fighter's name
        self.health = health  # Fighter's starting health
        self.damage_per_attack = damage_per_attack  # How much damage they do per attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__  # Ensures printing the object shows useful info


# Create two fighter instances
fighter1 = Fighter("Harald", 20, 5)
fighter2 = Fighter("Harry", 5, 4)


# Function to simulate the fight and return the winner's name
def declare_winner(fighter1, fighter2, first_attacker):
    # Decide who will attack first based on the name passed
    attacker = fighter1 if first_attacker == fighter1.name else fighter2
    # The other fighter becomes the defender
    defender = fighter2 if attacker == fighter1 else fighter1

    # Loop continues until one fighter dies (health <= 0)
    while True:
        # Attacker hits the defender, reducing their health
        defender.health -= attacker.damage_per_attack

        # Print the result of the attack for clarity
        print(f"{attacker.name} attacks {defender.name} -> {defender.name}'s health: {defender.health}")

        # If defender's health is 0 or less, attacker wins
        if defender.health <= 0:
            print(f"{defender.name} is dead. {attacker.name} wins")
            return attacker.name  # Return the winner's name (important for test cases)

        # Swap roles: now the defender attacks, and the attacker defends
        attacker, defender = defender, attacker


# Start the fight with "Harry" attacking first
declare_winner(fighter1, fighter2, "Harry")
