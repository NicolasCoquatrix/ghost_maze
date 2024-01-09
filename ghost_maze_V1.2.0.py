##### GHOST MAZE #####

# Ghost Maze est un jeu créé durant mon parcours de formation en développement Web et Web mobile.

# La version 1.2.0 ajoute :
# - Amélioration du système de déplacement (plus besoin d'appayer sur la touche 'Entrée').


import os #os.system("cls")
import msvcrt #msvcrt.getch()

## DÉFINITION DES FONCTIONS ##
def get_user_input():
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8').lower()
            return char

## DÉFINITION DES VARIABLES DE BASE ##
title = "Le méga jeu du labyrinthe"
title_deco = "├"+"─"*int(20-(len(title)/2))+"┤"

program_deco_head = "\n"+"═"*45
program_deco_foot = "\n"+"═"*15+"╦"+"═"*13+"╦"+"═"*15+"\n"+" "*15+"╨ DÉPLACEMENT ╨"+" "*15+"\n"+" "*22+"▼"+" "*22
score_table = [" - 0 - "," - 1 - "," - 2 - "," - 3 - "," - 4 - "," - 5 - "," - 6 - "," - 7 - "," - 8 - "," - 9 - "," -1 0- "]
score = 0

## DÉFINITION DE L'ECRAN DU JEU ##
game_screen = program_deco_head + "\n" + title_deco + " " + title.upper() + " " + title_deco + program_deco_head + "\n  Pour vous déplacer, utilisez les touches :\n  Z = ⮝   |   S = ⮟   |   Q = ⮜   |   D = ⮞\n   Puis appuyez sur 'Entrée' pour valider.\n" + "\n" + " "*18 + "╭" + "─"*7 + "╮" + "\n" + " "*18 + "│ SCORE │\n"


## DÉFINITION DU LABYRINTHE ##
labyrinth = [[" ╔═","═══","═══","═══","═══","═══","═══","═══","═══","═══","═╦═","═══","═══","═══","═╗ "],
             [" ║ ","   ","   ","   ","   ","   ","   ","   ","   "," ⬪ "," ║ ","   ","   ","   "," ║ "],
             [" ║ ","   "," ╔═","═══","═╦═","═══","═╦═","═══","═╗ ","   "," ║ ","   "," ╔═","   ","═╣ "],
             [" ║ ","   "," ║ ","   "," ║ "," ⬪ ","   ","   "," ║ ","   ","   ","   "," ║ ","   "," ║ "],
             [" ║ ","   ","   ","   "," ║ "," ⬪ "," ║ ","   "," ╚═","═══","═╩═","═══","═╣ ","   "," ┆ "],
             [" ║ ","   "," ║ ","   "," ╚═","═══","═╣ ","   ","   ","   ","   "," ⬪ "," ║ ","   "," ║ "],
             [" ║ "," ⬪ "," ║ ","   ","   ","   "," ║ ","   "," ╔═","═══","═══","═══","═╩═","═══","═╣ "],
             [" ╠═","═══","═╬═","═══","═╗ ","   ","   ","   "," ║ "," ⬪ ","   ","   ","   ","   "," ║ "],
             [" ║ ","   ","   ","   "," ╚═","═══","═╣ ","   "," ╠═","═══","═══","═══","═══","   ","═╣ "],
             [" ║ ","   "," ║ ","   ","   ","   ","   ","   "," ║ ","   ","   ","   ","   ","   "," ║ "],
             [" ║ ","   "," ╚═","═╗ ","   "," ╔═","═╩═","═╦═","═╩═","   ","═══","═══","═╦═","═══","═╣ "],
             [" ║ ","   ","   "," ║ ","   ","   ","   "," ║ "," ⬪ ","   ","   ","   ","   ","   "," ║ "],
             [" ╠═","═══"," ⬪ ","═╣ ","   "," ║ ","   "," ╚═","═══","═══","═══","   ","═╣ ","   "," ║ "],
             [" ┆ "," ● ","   "," ║ "," ⬪ "," ║ ","   ","   ","   ","   ","   ","   "," ║ "," ⬪ "," ║ "],
             [" ╚═","═══","═══","═╩═","═══","═╩═","═══","═══","═══","═══","═══","═══","═╩═","═══","═╝ "]]

## PROGRAMME ##
# Affichage de l'écran du jeu au démarrage
player_skin = [" ● "," ❶ "," ❷ "," ❸ "," ❹ "," ❺ "," ❻ "," ❼ "," ➑ "," ➒ "," ➓ "]
current_skin = 0
score_table = [" - 0 - "," - 1 - "," - 2 - "," - 3 - "," - 4 - "," - 5 - "," - 6 - "," - 7 - "," - 8 - "," - 9 - "," -1 0- "]
score = 0
os.system("cls")
print(game_screen  + " "*18 + f"│" + score_table[score] + "│\n" + " "*18 + "╰" + "─"*7 + "╯")
for i in range (len(labyrinth)) :
    line = ""
    for j in range (len(labyrinth[i])) :
        line += labyrinth[i][j]
    print(line)
print(program_deco_foot + "\n" + " "*22, end='')

# Déplacements
win = False
while win == False :
    shift = get_user_input()
    line = 0
    box = 0
    # Selection du personnage
    while labyrinth[line][box] not in player_skin :
        for i in range (len(labyrinth)-1) :
            if labyrinth[line][box] not in player_skin :
                if box < len(labyrinth[0]) :
                    box +=1
            else :
                break
        if labyrinth[line][box] not in player_skin :
            if line < len(labyrinth[0]) :
                line +=1
            box = 0
                
    # Déplacement avant
    if shift == "z" :
        if labyrinth[line-1][box] == "   " :
            labyrinth[line-1][box] = player_skin[current_skin]
            labyrinth[line][box] = "   "
        elif labyrinth[line-1][box] == " ⬪ " :
            current_skin += 1
            labyrinth[line-1][box] = player_skin[current_skin]
            labyrinth[line][box] = "   "
            score +=1
        elif labyrinth[line-1][box] == " ★ " :
            labyrinth[line-1][box] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen  + " "*18 + f"│" + score_table[score] + "│\n" + " "*18 + "╰" + "─"*7 + "╯")
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot + "\n" + " "*22, end='')

    # Déplacement arrière
    elif shift == "s" :
        if labyrinth[line+1][box] == "   " :
            labyrinth[line+1][box] = player_skin[current_skin]
            labyrinth[line][box] = "   "
        elif labyrinth[line+1][box] == " ⬪ " :
            current_skin += 1
            labyrinth[line+1][box] = player_skin[current_skin]
            labyrinth[line][box] = "   "
            score +=1
        elif labyrinth[line+1][box] == " ★ " :
            labyrinth[line+1][box] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen  + " "*18 + f"│" + score_table[score] + "│\n" + " "*18 + "╰" + "─"*7 + "╯")
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot + "\n" + " "*22, end='')

    # Déplacement gauche
    elif shift == "q" :
        if labyrinth[line][box-1] == "   " :
            labyrinth[line][box-1] = player_skin[current_skin]
            labyrinth[line][box] = "   "
        elif labyrinth[line][box-1] == " ⬪ " :
            current_skin += 1
            labyrinth[line][box-1] = player_skin[current_skin]
            labyrinth[line][box] = "   "
            score +=1
        elif labyrinth[line][box-1] == " ★ " :
            labyrinth[line][box-1] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen  + " "*18 + f"│" + score_table[score] + "│\n" + " "*18 + "╰" + "─"*7 + "╯")
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot + "\n" + " "*22, end='')
    
    # Déplacement droite
    elif shift == "d" :
        if labyrinth[line][box+1] == "   " :
            labyrinth[line][box+1] = player_skin[current_skin]
            labyrinth[line][box] = "   "
        elif labyrinth[line][box+1] == " ⬪ " :
            current_skin += 1
            labyrinth[line][box+1] = player_skin[current_skin]
            labyrinth[line][box] = "   "
            score +=1
        elif labyrinth[line][box+1] == " ★ " :
            if labyrinth[line][box] == player_skin[10] :
                labyrinth[line][box+1] = " ✪ "
                labyrinth[line][box] = "   "
                program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
                win = True
        os.system("cls")
        print(game_screen  + " "*18 + f"│" + score_table[score] + "│\n" + " "*18 + "╰" + "─"*7 + "╯")
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot + "\n" + " "*22, end='')

    # Mauvaise saisie
    else :
        os.system("cls")
        print(game_screen  + " "*18 + f"│" + score_table[score] + "│\n" + " "*18 + "╰" + "─"*7 + "╯")
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot + "\n" + " "*22, end='')
    
    # Ouverture porte de fin
    if current_skin == 10 :
        labyrinth[3][14] = " ╙┘"
        labyrinth[4][14] = " ★ "
        labyrinth[5][14] = " ╓┐"



# Développé par Nicolas Coquatrix