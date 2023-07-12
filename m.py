import re

def charger_abreviations(fichier):
    abreviations = set()
    with open(fichier, 'r') as file:
        for line in file:
            abreviations.add(line.strip())
    return abreviations

def extraire_donnees(fichier, fichier_abreviations):
    abreviations = charger_abreviations(fichier_abreviations)
    donnees = []
    with open(fichier, 'r') as file:
        lines = file.read().split('\n\n')  # Séparation des paragraphes

        for line in lines:
            mots = line.split(' ')

            # Vérifier si le premier mot est en majuscule
            if not mots[0].isupper():
                continue

            # Recherche d'abréviations
            abreviations_trouvees = []
            majuscules_trouvees = []
            for mot in mots:
                if mot in abreviations:
                    abreviations_trouvees.append(mot)
                elif mot.isupper():
                    majuscules_trouvees.append(mot)

            # Recherche de la définition
            definition = ' '.join(mots[len(abreviations_trouvees) + len(majuscules_trouvees):])

            donnees.append((abreviations_trouvees, majuscules_trouvees, definition))

    return donnees

# Exemple d'utilisation
fichier = 'fichier.txt'
fichier_abreviations = 'listeprep.txt'
donnees = extraire_donnees(fichier, fichier_abreviations)

for abreviations, majuscules, definition in donnees:
    print("Abréviations:", ' '.join(abreviations))
    print("Mots en majuscule:", ' '.join(majuscules))
    print("Définition:", definition)
    print()
