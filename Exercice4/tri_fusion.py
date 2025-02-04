def fusionner_intervalles(intervalles):
    # Étape 1 : Trier les intervalles par heure de début
    intervalles.sort(key=lambda x: x[0])
    
    # Étape 2 : Initialiser une liste pour stocker les intervalles fusionnés
    fusionnes = []
    
    for intervalle in intervalles:
        # Si la liste est vide ou si l'intervalle actuel ne chevauche pas le dernier intervalle fusionné
        if not fusionnes or fusionnes[-1][1] < intervalle[0]:
            fusionnes.append(intervalle)  # Ajouter l'intervalle actuel
        else:
            # Il y a chevauchement, fusionner les intervalles
            fusionnes[-1] = (fusionnes[-1][0], max(fusionnes[-1][1], intervalle[1]))

    return fusionnes  # Retourner la liste des intervalles fusionnés

# Exemple d'utilisation
intervalles = [(1, 3), (2, 4), (5, 7), (4, 7), (9, 10)]
intervalles_fusionnes = fusionner_intervalles(intervalles)

print("Intervalles fusionnés :", intervalles_fusionnes)
