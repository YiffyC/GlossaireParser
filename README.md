# GlossaireParser

## Description
Mon Programme est un script Python conçu pour extraire des mots, des abréviations et leurs définitions à partir d'un fichier texte. Il utilise une liste d'abréviations préparée dans un fichier séparé pour effectuer la recherche et génère un fichier CSV contenant les abréviations, les mots associés et les définitions correspondantes.

## Fonctionnalités
- Recherche et extraction d'abréviations à partir d'un fichier texte
- Ignorance des mots spécifiques non suivis d'une abréviation
- Génération d'un fichier CSV contenant les abréviations, les mots associés et les définitions
- Barre de progression dynamique indiquant le pourcentage de traitement du fichier texte
- Gestion des fichiers d'entrée et de sortie dans les dossiers appropriés

## Utilisation
1. Placez votre fichier texte à traiter dans le dossier "input".
2. Assurez-vous d'avoir un fichier contenant la liste d'abréviations préparée dans le format approprié. Nommez-le "listeprep.txt" et placez-le dans le même répertoire que le script Python.
3. Exécutez le script Python `n.py`.
4. Le script lira le fichier texte, effectuera la recherche d'abréviations et générera un fichier CSV dans le dossier "output" avec le nom "donnees.csv".
5. Le fichier CSV contiendra les colonnes "Mot", "Abréviation" et "Définition" pour chaque abréviation trouvée.

## Configuration requise
- Python 3.x
- Bibliothèques Python : csv, re, glob, tqdm (`pip install tqdm`)

## Exemple d'utilisation
```bash
python n.py
```


