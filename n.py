import csv
import re
import glob
from tqdm import tqdm
import os

def charger_abreviations(fichier):
    abreviations = set()
    with open(fichier, 'r', encoding='utf-8-sig') as file:
        for line in file:
            abreviations.add(line.strip())
    return abreviations

def extraire_donnees(fichier_abreviations, fichier_csv):
    abreviations = charger_abreviations(fichier_abreviations)
    donnees = []

    input_files = glob.glob("input/*.txt")
    if len(input_files) == 0:
        print("Aucun fichier texte trouvé dans le dossier 'input'.")
        return

    fichier = input_files[0]  # Prendre le premier fichier trouvé

    with open(fichier, 'r', encoding='utf-8-sig') as file:
        lines = file.read().split('\n')  # Lecture de lignes individuelles

        paragraphes = []
        paragraphe = ""
        for line in lines:
            if line.strip():  # Si la ligne n'est pas vide
                paragraphe += line + " "
            else:
                paragraphes.append(paragraphe.strip())
                paragraphe = ""

        if paragraphe:  # Ajouter le dernier paragraphe s'il n'est pas vide
            paragraphes.append(paragraphe.strip())

        total_paragraphes = len(paragraphes)
        paragraphes_traites = 0

        with tqdm(range(total_paragraphes), desc="Traitement en cours") as pbar:
            for i in pbar:
                paragraphe = paragraphes[i]
                mots = paragraphe.split(' ')

                # Vérifier si le premier mot est en majuscule
                if not mots[0].isupper():
                    continue

                # Ignorer les mots spécifiques sans abréviation associée
                if mots[0] in ['BIQ', 'BIS'] and mots[0] not in abreviations:
                    continue

                # Recherche d'abréviations
                abreviations_trouvees = []
                majuscules_trouvees = []
                for j, mot in enumerate(mots):
                    if mot in abreviations:
                        abreviations_trouvees.append(mot)
                    elif mot.isupper() and j < len(mots) - 1 and mots[j + 1] not in abreviations:
                        continue  # Ignorer le mot en majuscule s'il n'est pas suivi d'une abréviation
                    elif mot.isupper():
                        majuscules_trouvees.append(mot)

                # Vérifier s'il y a une abréviation associée
                if not abreviations_trouvees:
                    continue

                # Recherche de la définition
                definition = ' '.join(mots[len(abreviations_trouvees) + len(majuscules_trouvees):])

                donnees.append((mots[0], ', '.join(abreviations_trouvees), definition))

                paragraphes_traites += 1
                pbar.set_postfix({'Traités': paragraphes_traites})

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    fichier_csv = os.path.join(output_dir, fichier_csv)

    # Écriture des données dans le fichier CSV avec l'encodage UTF-8 et le point-virgule comme séparateur
    with open(fichier_csv, 'w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Mot', 'Abréviation', 'Définition'])
        writer.writerows(donnees)

    print("Extraction des données terminée. Les données ont été enregistrées dans le fichier CSV.")

# Exemple d'utilisation
fichier_abreviations = 'listeprep.txt'
fichier_csv = 'donnees.csv'
extraire_donnees(fichier_abreviations, fichier_csv)
