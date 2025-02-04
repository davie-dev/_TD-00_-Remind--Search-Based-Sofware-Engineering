
from collections import deque

# Classe pour représenter un graphe
class Graphe:
    def __init__(self):
        # Dictionnaire pour stocker le graphe, où les clés sont des nœuds et les valeurs sont des listes de voisins
        self.graph = {}

    def ajouter_noeud(self, noeud):
        # Ajoute un nœud au graphe s'il n'existe pas déjà
        if noeud not in self.graph:
            self.graph[noeud] = []

    def ajouter_arete(self, u, v):
        # Ajoute une arête entre deux nœuds u et v
        self.ajouter_noeud(u)  # Assure que u est un nœud
        self.ajouter_noeud(v)  # Assure que v est un nœud
        self.graph[u].append(v)  # Ajoute v comme voisin de u
        self.graph[v].append(u)  # Ajoute u comme voisin de v (graphe non orienté)

    def bfs(self, start):
        # Méthode pour effectuer la recherche en largeur (BFS)
        visited = set()  # Ensemble pour garder une trace des nœuds visités
        queue = deque([start])  # File d'attente pour gérer les nœuds à explorer
        resultat = []  # Liste pour stocker l'ordre de visite des nœuds

        while queue:
            noeud = queue.popleft()  # Récupère le nœud en tête de la file
            if noeud not in visited:
                visited.add(noeud)  # Marque le nœud comme visité
                resultat.append(noeud)  # Ajoute le nœud à la liste des résultats
                # Ajoute les voisins non visités à la file d'attente
                queue.extend(neighbour for neighbour in self.graph[noeud] if neighbour not in visited)

        return resultat  # Renvoie l'ordre de visite des nœuds

    def dfs(self, start):
        # Méthode pour effectuer la recherche en profondeur (DFS)
        visited = set()  # Ensemble pour garder une trace des nœuds visités
        resultat = []  # Liste pour stocker l'ordre de visite des nœuds

        def dfs_recursive(noeud):
            visited.add(noeud)  # Marque le nœud comme visité
            resultat.append(noeud)  # Ajoute le nœud à la liste des résultats
            # Explore chaque voisin non visité
            for neighbour in self.graph[noeud]:
                if neighbour not in visited:
                    dfs_recursive(neighbour)  # Appel récursif pour le voisin

        dfs_recursive(start)  # Démarre la recherche à partir du nœud de départ
        return resultat  # Renvoie l'ordre de visite des nœuds

    def sont_connectés(self, u, v):
        # Méthode pour vérifier si deux nœuds sont connectés
        return v in self.bfs(u)  # Utilise BFS pour vérifier la connectivité

    def chemin_le_plus_court(self, start, end):
        # Méthode pour trouver le chemin le plus court entre deux nœuds
        visited = set()  # Ensemble pour garder une trace des nœuds visités
        queue = deque([(start, [start])])  # File d'attente pour gérer les nœuds et le chemin

        while queue:
            noeud, chemin = queue.popleft()  # Récupère le nœud et le chemin associé
            if noeud == end:  # Si le nœud courant est le nœud de destination
                return chemin  # Renvoie le chemin trouvé
            if noeud not in visited:
                visited.add(noeud)  # Marque le nœud comme visité
                # Ajoute les voisins non visités à la file avec le chemin mis à jour
                for neighbour in self.graph[noeud]:
                    queue.append((neighbour, chemin + [neighbour]))

        return None  # Renvoie None si aucun chemin n'est trouvé

# Exemple d'utilisation
graphe = Graphe()  # Crée une instance de Graphe
# Ajoute des arêtes pour créer le graphe
graphe.ajouter_arete(1, 2)
graphe.ajouter_arete(1, 3)
graphe.ajouter_arete(2, 4)
graphe.ajouter_arete(3, 5)
graphe.ajouter_arete(4, 5)
graphe.ajouter_arete(6, 7)  # Création de deux composants connectés

# Tests de BFS et DFS
print("Parcours BFS à partir du nœud 1 :", graphe.bfs(1))  # Affiche l'ordre de visite en BFS
print("Parcours DFS à partir du nœud 1 :", graphe.dfs(1))  # Affiche l'ordre de visite en DFS

# Vérification de connectivité entre les nœuds
print("Les nœuds 1 et 5 sont connectés :", graphe.sont_connectés(1, 5))
print("Les nœuds 1 et 6 sont connectés :", graphe.sont_connectés(1, 6))

# Chemin le plus court entre deux nœuds
print("Chemin le plus court de 1 à 5 :", graphe.chemin_le_plus_court(1, 5))
print("Chemin le plus court de 1 à 6 :", graphe.chemin_le_plus_court(1, 6))
