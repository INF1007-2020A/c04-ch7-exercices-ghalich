import math
import turtle

def volume_masse_ellipsoide(a = 10 , b = 8, c = 6 , masse_volumique = 5 ): 
    volume = (4/3)*math.pi*a*b*c
    masse = volume * masse_volumique
    return (volume, masse)

highest_value_dict = lambda dictionaire: sorted(dictionaire, key = dictionaire.get)[-1]

def draw_tree():

    def draw_branches(angle = 35, longueur = 120, largeur = 6, nombre_branches = 7):
        
        turtle.pendown()
        turtle.pensize(largeur)
        turtle.left(angle)
        turtle.forward(longueur)

        if nombre_branches > 1:
            draw_branches(angle-5, longueur-20, largeur-1, nombre_branches -1)

        turtle.pensize(largeur)
        turtle.backward(longueur)
        turtle.right(angle*2)
        turtle.forward(longueur)

        
        if nombre_branches > 1:
            draw_branches(angle-5, longueur-20, largeur-1, nombre_branches -1)
        
        
        turtle.backward(longueur)
        turtle.left(angle)

        
    turtle.pensize(5)
    turtle.penup()
    turtle.setposition(0.00,-250)
    turtle.color("green")
    turtle.left(90)
    turtle.pendown()
    turtle.forward(140)

    draw_branches()

    while True:
        pass    

def DNA_sequence():

    def valid(sequence : str = None):
        
        if sequence is None or len(sequence) == 0:
            return False

        for char in sequence:
            if char != "a" and char != "t" and char != "g" and char != "c":
                return False

        return True
    
    def saisie(entree : str = "sequence"):
        done = False
        while not done:
            sequence = (input(f"Entrez la {entree} ou la chaine d'ADN ici : ")).lower()
            done = valid(sequence)
            if done == False:
                print(f"\nVeuillez entrer une {entree} valide !\n")
        return sequence
    
    proportion = lambda chaine, sequence: sequence.count(chaine)/len(sequence)

    sequence = saisie("sequence")
    chaine = saisie("chaine")

    print(f'Il y a {round(proportion(chaine, sequence)*100, 2)} % de "{chaine}".')        
    
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    dic = {"a": 5, "b" : 9, "c": 1, "d" : 15, "e" : 10 }
    print(f"La clé ayant la plus grande valeur de {dic} est {highest_value_dict(dic)}")
    draw_tree()
    #DNA_sequence()