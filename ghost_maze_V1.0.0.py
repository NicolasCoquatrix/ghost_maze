##### GHOST MAZE #####

# Ghost Maze est un jeu créé durant mon parcours de formation en développement Web et Web mobile.

# La version 1.0.0 intègre :
# - Création d'un labyrinthe,
# - Déplacement avec Z Q S D.


import os #os.system("cls")

## DÉFINITION DES VARIABLES DE BASE ##
title = "Le méga jeu du labyrinthe"
title_deco = "├"+"─"*int(20-(len(title)/2))+"┤"

program_deco_head = "\n"+"═"*45
program_deco_foot = "\n"+"═"*15+"╦"+"═"*13+"╦"+"═"*15+"\n"+" "*15+"╨ DÉPLACEMENT ╨"+" "*15+"\n"+" "*22+"▼"+" "*22

## DÉFINITION DE L'ECRAN DU JEU ##
game_screen = program_deco_head + "\n" + title_deco + " " +title.upper() + " " + title_deco + program_deco_head + "\n  Pour vous déplacer, utilisez les touches :\n  Z = ⮝   |   S = ⮟   |   Q = ⮜   |   D = ⮞\n   Puis appuyez sur 'Entrée' pour valider.\n"


## DÉFINITION DU LABYRINTHE ##
labyrinth = [[" ╔═","═══","═══","═══","═══","═══","═══","═══","═══","═══","═╦═","═══","═══","═══","═╗ "],
             [" ║ ","   ","   ","   ","   ","   ","   ","   ","   ","   "," ║ ","   ","   ","   "," ║ "],
             [" ║ ","   "," ╔═","═══","═╦═","═══","═╦═","═══","═╗ ","   "," ║ ","   "," ╔═","   ","═╣ "],
             [" ║ ","   "," ║ ","   "," ║ ","   ","   ","   "," ║ ","   ","   ","   "," ║ ","   "," ╚╛"],
             [" ║ ","   ","   ","   "," ║ ","   "," ║ ","   "," ╚═","═══","═╩═","═══","═╣ ","   "," ★ "],
             [" ║ ","   "," ║ ","   "," ╚═","═══","═╣ ","   ","   ","   ","   ","   "," ║ ","   "," ╔╕"],
             [" ║ ","   "," ║ ","   ","   ","   "," ║ ","   "," ╔═","═══","═══","═══","═╩═","═══","═╣ "],
             [" ╠═","═══","═╬═","═══","═╗ ","   ","   ","   "," ║ ","   ","   ","   ","   ","   "," ║ "],
             [" ║ ","   ","   ","   "," ╚═","═══","═╣ ","   "," ╠═","═══","═══","═══","═══","   ","═╣ "],
             [" ║ ","   "," ║ ","   ","   ","   ","   ","   "," ║ ","   ","   ","   ","   ","   "," ║ "],
             [" ║ ","   "," ╚═","═╗ ","   "," ╔═","═╩═","═╦═","═╩═","   ","═══","═══","═╦═","═══","═╣ "],
             [" ║ ","   ","   "," ║ ","   ","   ","   "," ║ ","   ","   ","   ","   ","   ","   "," ║ "],
             ["╘╬═","═══","   ","═╣ ","   "," ║ ","   "," ╚═","═══","═══","═══","   ","═╣ ","   "," ║ "],
             [" ┆ "," ● ","   "," ║ ","   "," ║ ","   ","   ","   ","   ","   ","   "," ║ ","   "," ║ "],
             ["╒╩═","═══","═══","═╩═","═══","═╩═","═══","═══","═══","═══","═══","═══","═╩═","═══","═╝ "]]

## PROGRAMME ##
# Affichage de l'écran du jeu au démarrage
os.system("cls")
print(game_screen)
for i in range (len(labyrinth)) :
    line = ""
    for j in range (len(labyrinth[i])) :
        line += labyrinth[i][j]
    print(line)
print(program_deco_foot)

# Déplacements
win = False
while win == False :
    shift = input("                      ").lower()
    line = 0
    box = 0
    while labyrinth[line][box] != " ● " :
        for i in range (14) :
            if labyrinth[line][box] != " ● " :
                if box < 15 :
                    box +=1
            else :
                break
        if labyrinth[line][box] != " ● " :
            if line < 15 :
                line +=1
            box = 0
                
    # Déplacement avant
    if shift == "z" :
        if labyrinth[line-1][box] == "   " :
            labyrinth[line-1][box] = " ● "
            labyrinth[line][box] = "   "
        elif labyrinth[line-1][box] == " ★ " :
            labyrinth[line-1][box] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen)
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot)

    # Déplacement arrière
    elif shift == "s" :
        if labyrinth[line+1][box] == "   " :
            labyrinth[line+1][box] = " ● "
            labyrinth[line][box] = "   "
        elif labyrinth[line+1][box] == " ★ " :
            labyrinth[line+1][box] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen)
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot)

    # Déplacement gauche
    elif shift == "q" :
        if labyrinth[line][box-1] == "   " :
            labyrinth[line][box-1] = " ● "
            labyrinth[line][box] = "   "
        elif labyrinth[line][box-1] == " ★ " :
            labyrinth[line][box-1] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╦"+"═"*23+"╦"+"═"*10+"\n"+" "*10+"║ BRAVO, C'EST GAGNÉ !! ║"+" "*10+"\n"+" "*10+"╚"+"═"*23+"╝"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen)
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot)
    
    # Déplacement droite
    elif shift == "d" :
        if labyrinth[line][box+1] == "   " :
            labyrinth[line][box+1] = " ● "
            labyrinth[line][box] = "   "
        elif labyrinth[line][box+1] == " ★ " :
            labyrinth[line][box+1] = " ✪ "
            labyrinth[line][box] = "   "
            program_deco_foot = "\n"+"═"*10+"╤"+"═"*23+"╤"+"═"*10+"\n"+" "*10+"│ BRAVO, C'EST GAGNÉ !! │"+" "*10+"\n"+" "*10+"└"+"─"*23+"┘"+" "*10+"\n\n\n"
            win = True
        os.system("cls")
        print(game_screen)
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot)

    # Mauvaise saisie
    else :
        os.system("cls")
        print(game_screen)
        for i in range (len(labyrinth)) :
            line = ""
            for j in range (len(labyrinth[i])) :
                line += labyrinth[i][j]
            print(line)
        print(program_deco_foot)



# Développé par Nicolas Coquatrix