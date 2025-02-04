def knapsack(valeurs, poids, limite):
    n = len(valeurs)  # Nombre d'éléments
    # Création d'un tableau 2D pour stocker les valeurs maximales
    dp = [[0 for _ in range(limite + 1)] for _ in range(n + 1)]

    # Remplissage du tableau dp
    for i in range(1, n + 1):
        for w in range(1, limite + 1):
            if poids[i - 1] <= w:  # Si le poids de l'élément est inférieur ou égal à la limite
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - poids[i - 1]] + valeurs[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # Si l'élément est trop lourd, on ne l'inclut pas

    # La valeur maximale est dans dp[n][limite]
    valeur_maximale = dp[n][limite]
    
    # Récupération des éléments inclus dans la solution optimale
    w = limite
    elements_inclus = []
    
    for i in range(n, 0, -1):
        if valeur_maximale != dp[i - 1][w]:  # Vérifie si l'élément i a été inclus
            elements_inclus.append((valeurs[i - 1], poids[i - 1]))  # Ajoute l'élément
            w -= poids[i - 1]  # Réduit le poids restant

    return valeur_maximale, elements_inclus

# Exemple d'utilisation
articles = [(60, 10), (100, 20), (120, 30),(134,40)]  # (valeur, poids)
poids_limite = 50

valeur_max, elements = knapsack([valeur for valeur, poids in articles], 
                                 [poids for valeur, poids in articles], 
                                 poids_limite)

print("Valeur maximale : ", valeur_max)
print("Éléments inclus : ", elements)