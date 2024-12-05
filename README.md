# Projet : Traitement et Labélisation de Contenu OCR des Rapports SFCR

## Introduction
Ceci est un projet de test technique conçu pour évaluer vos compétences en Python, en résolution de problémes, et en présentation de résultats. Ce projet vise à traiter et analyser des rapports SFCR extraits à l’aide de l’API Vision de Google Cloud Platform (GCP) et à produire une solution permettant de différencier le contenu utile du contenu indésirable.

## Contexte
Les rapports SFCR (« Solvency and Financial Condition Reports ») sont publiés par les compagnies d’assurance pour fournir des informations sur leur situation financière, leur solvabilité et leur gestion des risques. Ces documents contiennent souvent des éléments superflus (comme les bas de pages, hauts de pages, tableaux et graphiques), rendant leur analyse automatique complexe. L'objectif principal est d'extraire uniquement le contenu utile pour faciliter les traitements ultérieurs.

## Objectifs du Projet
1. **Nettoyage des rapports** : Identifier et exclure les contenus indésirables tels que les bas de pages, hauts de pages, tableaux et graphiques.
2. **Structure du texte** : Identifier les paragraphes et les grands titres des différentes sections.
3. **Labélisation automatique** : Ajouter une colonne « Label » au tableau produit par `produce_brut()`, avec les valeurs possibles :
   - **Inutile** : Contenu à exclure.
   - **Paragraphe** : Contenu textuel structurant.
   - **Titre** : Grands titres des sections du rapport.
4. **Généralisation** : Créer une solution applicable à d'autres rapports SFCR avec des structures similaires.

## Organisation des Fichiers
### Dossiers et Fichiers Fournis

- **`main.py`** :Script principal orchestrant l'exécution complète du pipeline de traitement des données, depuis le nettoyage et la transformation des DataFrames jusqu'à leur labélisation.
- **`helper.py`** : Script contenant la fonction `produce_brut()` qui transforme les fichiers JSON en DataFrame avec les blocs textuels et leurs caractéristiques.
- **`labelizer.py`** : Script contenant la classe `Labeliseur`, conçue pour effectuer un processus complet de traitement et de labélisation des données textuelles grâce à l'analyse en composantes principales (ACP) et au clustering K-Means.

#### Data
- **`data/labeled/`** : Contient les fichiers CSV des tableaux labelisés.
- **`data/pdfs/`** : Contient les fichiers PDF des rapports SFCR.
- **`data/ocr/`** : Contient les fichiers JSON produits par l'API Vision de GCP.

#### Removed
- **`removed/Layout_filter/`** : Contient les fichiers CSV des lignes supprimées après le 1er filtre.
- **`removed/Occurence_filter/`** : Contient les fichiers CSV des lignes supprimées après le 2em filtre.
- **`removed/Occurence/`** : Contient les fichiers CSV des occurrences destinés à analyse.
- **`removed/num_filter/`** : Contient les fichiers CSV des lignes supprimées après le 3em filtre.
- **`removed/filtered/`** : Contient les fichiers CSV l'ensemble des lignes filtrées.

#### code
- **`notebook.ipynb`** : Notebook Jupyter présentant toute la démarche, les explications et le code développé pour ce projet.
- **`.csv`** : Les différentes sorties de produce_brut.

#### output
- **`output/labeled_data.csv`** :Contient la sortie du main.py

## Installation et Exécution
### Prérequis
- Python 3.8+
- Librairies Python : pandas, numpy, scikit-learn

### Instructions
1. Clonez ce repository :
   ```bash
   git clone https://github.com/AlainTanimt/Teste_Technique_KPMG.git
   cd <nom-du-repo>
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Exécutez le script principal :
   ```bash
   python main.py data/ocr/allianz-1-to-94.json
   ```
