def recherche_binaire(liste, cible):
    gauche, droite = 0, len(liste) - 1
    
    while gauche <= droite:
        # determiner le milieu en garder la partie entier
        milieu = (gauche + droite) // 2
        
        # Vérifie si la cible est à la position milieu
        if liste[milieu] == cible:
            return milieu
        # Si la cible est plus grande, ignore la moitié gauche
        elif liste[milieu] < cible:
            gauche = milieu + 1
        # Si la cible est plus petite, ignore la moitié droite
        else:
            droite = milieu - 1
            
    # Cible non trouvée
    return -1

# Liste triée
liste_triée = [1, 3, 5, 7,8, 9, 11, 13, 15,]

# Tests
valeurs_de_test = [3, 10, 15, 1, 8,17]

for valeur in valeurs_de_test:
    index = recherche_binaire(liste_triée, valeur)
    if index != -1:
        print(f"La valeur {valeur} a été trouvée à l'index {index}.")
    else:
        print(f"La valeur {valeur} n'a pas été trouvée.")