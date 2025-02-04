def somme_maximale_sous_tableau(tab):
    # Initialisation des variables
    max_somme = float('-inf')  # Pour stocker la somme maximale trouvée
    somme_actuelle = 0  # Pour suivre la somme actuelle du sous-tableau

    for nombre in tab:
        somme_actuelle += nombre  # Ajoute le nombre courant à la somme actuelle
        
        # Met à jour la somme maximale si la somme actuelle est supérieure
        if somme_actuelle > max_somme:
            max_somme = somme_actuelle
            
        # Réinitialise la somme actuelle si elle devient négative
        if somme_actuelle < 0:
            somme_actuelle = 0
            
    return max_somme  # Retourne la somme maximale trouvée

# Exemple d'utilisation et tests
tableaux = [
    [1, -2, 3, 4, -1, 2, 1, -5, 4],  # Cas mixte
    [-2, -3, -1, -5],                # Tous les nombres négatifs
    [2, 3, -2, 1, -1, 4],            # Cas mixte
    [5, 4, -1, 7, 8],                # Tous positifs avec un négatif
]

for idx, tableau in enumerate(tableaux):
    resultat = somme_maximale_sous_tableau(tableau)
    print(f"Tableau {idx + 1}: {tableau} => Somme maximale: {resultat}")