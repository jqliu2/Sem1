#Johnny Liu
#11/21/24
#Pokemon Simulator

#Init
import random

#Global Variable
pokemon_level = 0
pokemon_name = "squirtle"
win = 0
losses = 0
#Functions
def draw_squirtle():
    print("""⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜
⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🏿⬛⬛⬜⬛🟦🟦🟦⬛🟦🟦⬛
⬛🟫🟦🟦🟦🟦🟦🟦🟦🟦🏿🟫🏿⬛🟦🟦🟦⬛🟦🟦🟦⬛
⬛🟦🟦🟦🟦⬜⬛🟦🟦🟦🏽🟫🟫🏿⬛🟦🟦⬛🟦🟦⬛⬜
⬛🟦🟦🟦🟦⬛🟫🟦🟦🟦⬜🟫🟫🟫⬛🟦⬛⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦⬛🟫🟦🟦🟦⬛⬜⬜🟫🟫⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦⬛⬛🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟦⬛⬛⬛⬛🟦🟦🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨⬛🟦🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨⬛⬛⬛⬛🏽🟫🟫⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟦⬛🟫🟨🟨🟨🟫⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛🟫🟫🟦⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def draw_wartortle():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🟦🟦🟦🟦🟪🟪⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜
⬜⬜⬛🟪🟦🟦🟦🟦🟦◼️⬜⬛⬜⬛⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜
⬜⬜⬛🟦🟦🟦🟦🟦🟦◼️⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜
⬜⬛🟦🟦🟦🟦🟦🟦⬛🟪⬛⬜⬜⬛🟨⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜
⬜⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦⬛⬛🟫🟨🟫⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛🟦🟦🟦⬛⬛⬜⬜🟦⬛⬜⬜🟫🟨⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛🟦🟦🟦🟦🟫⬜🟦🟪⬛⬛⬜🟫🟨🟨⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬛🟦⬛🟦🟪🟦🟦🟦⬛⬛🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬛⬜🟦⬛⬛⬛⬛⬛🟨⬛🟦🟦🟦⬜🟫🟨⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬜⬛⬜🟨🟨⬛⬜🟦🟦⬛⬜🟫🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨⬛🟦⬜⬛⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟦⬛⬛🟨⬛⬛🟨⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟦🟦⬛⬛🟨🟨⬛🟦⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟪🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def draw_blastoise():
    print("""⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜🏽🏽⬛⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜⬛⬜🟫🟫🟫🟫⬛⬛⬛🏽🏽⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟦⬛⬛🟫🟫🟫🟫🟫🟫⬛⬜⬛⬛🏽⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟦🟦🟦⬛⬛🟫⬛⬛🟫⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜
⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛🟦⬛🟫⬜🏽🏽🏽⬛⬜⬜⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟫🟫🏽🏽⬛🟫⬛⬜⬜⬜⬜
⬜⬛🟦🟦🟦🟦🟦⬛🟦🟦⬛🏽🏽🏽⬛⬛🟫🟫⬛⬜⬜⬜⬜
⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦🟦⬛⬛⬛⬛⬛🏽🟫🟫⬛⬛⬛⬛
⬛🟦🟦🟦🟦⬛⬛🟦🟦🟨🟦⬛⬛🟦🟦🟦⬛🏽🟫⬛🟦🟦⬛
⬛⬜🟦🟦🟦🟦🟦🟦🟨🟨⬛🏽⬛🟦🟦🟦⬛🏽🟫⬛🟦⬛⬜
⬜⬛🟨🟨🟦🟦🟨🟨🟨⬛🏽⬛🟦🟦🟦🟦⬛🏽🏽⬛⬛⬜⬜
⬜⬜⬛⬛⬜🟨🟨⬛⬛🟨⬛🟦🟦🟦🟦⬛🟦⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛⬛🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜⬛⬛⬛⬛🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨⬛🟨⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜🟦🟦⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
def draw():
    global pokemon_level
    global pokemon_name
    if pokemon_level < 16:
        draw_squirtle()
    if pokemon_level >= 16:
        draw_wartortle()
    if pokemon_level >= 36:
        draw_blastoise()
def evolve():
    global pokemon_name
    global pokemon_level
    if pokemon_level == 16:
        pokemon_name = "wartortle"
        print("squirtle evolved to wartortle!")
    if pokemon_level == 36:
        pokemon_name = "blastoise"
        print("wartortle evolved to blastoise!")
def train():
    global pokemon_level
    global pokemon_name
    pokemon_level = pokemon_level + 1
    level = str(pokemon_name) + " leveled up to " + str(pokemon_level)
    print(level)
    evolve()
def gym():
    global pokemon_name
    global pokemon_level
    global win
    global losses
    output = random.randint(1,2)
    if output == 1:
        pokemon_level = pokemon_level + 2
        gym_status = str(pokemon_name) + " won the battle!"
        print(gym_status)
        level = str(pokemon_name) + " leveled up to " + str(pokemon_level)
        print(level)
        win = win + 1
        if pokemon_level == 17:
            print("squirtle evolved to wartortle!")
        if pokemon_level == 37:
            print("wartortle evolved to blastoise!")
        evolve()
    elif output == 2:
        gym_status = str(pokemon_name) + " lost the battle!"
        losses = losses + 1
        print(gym_status)
    if pokemon_level > 40:
        print("You are ready to fight the final gym battle!")
        output = random.randint(1,4)
        if output >= 2:
            pokemon_level = pokemon_level + 2
            level = str(pokemon_name) + " leveled up to " + str(pokemon_level)
            print(level)
            win = win + 1
            print("You won the final gym battle! Thank you for playing.")
        elif output == 1:
            gym_status = str(pokemon_name) + " lost the battle!"
            losses = losses + 1
            print(gym_status)
            print("You lost the final gym battle! Thank you for playing.")
def rest():
    info = str(pokemon_name) + " is level " + str(pokemon_level) + ". " + str(pokemon_name) + " has won " + str(win) + " battles. " + str(pokemon_level) + ". " + str(pokemon_name) + " has lost " + str(losses) + " battles. "
    print(info)
    draw()
def pokemon_evolution():
    print("Welcome to Pokemon Evolution")
    while True:
        print("Choose today's activity: ")
        print("""1.Train
2.Gym Battle
3.Rest(Display info)
4.Quit""")
        activity = int(input("Activity: "))
        if activity == 1:
            train()
        if activity == 2:
            gym()
        if activity == 3:
            rest()
        if activity == 4:
            break

#Main
pokemon_evolution()
