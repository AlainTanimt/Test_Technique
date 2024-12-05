import sys
import os
import pandas as pd
from labelizer import Labeliseur
from helper import produce_brut

def main():
    # Vérifier les arguments de la ligne de commande
    if len(sys.argv) != 2:
        print("Usage: python main.py /chemin/vers/data")
        sys.exit(1)

    # Récupérer le chemin des données
    data_dir = sys.argv[1]
    if not os.path.exists(data_dir):
        print(f"Erreur : Le répertoire {data_dir} n'existe pas.")
        sys.exit(1)

    # Charger les données avec produce_brut
    print("Chargement des données...")
    df = produce_brut(data_dir)
    # Caractéristiques pour la labélisation
    features = ['width', 'height', 'area', 'chars', 'char_size', 'pos_x', 'pos_y', 'aspect', 'x0', 'x1', 'y0', 'y1']

    # Initialiser le labeliseur
    labelizer = Labeliseur()

    # Labéliser les données
    print("Labélisation des données...")
    df_labeled = labelizer.labeliser(df, features)

    # Sauvegarder les résultats
    output_path = os.path.join("output", "labeled_data.csv")
    os.makedirs("output", exist_ok=True)
    df_labeled.to_csv(output_path, index=False)

    print(f"Labélisation terminée. Résultat sauvegardé dans {output_path}")

if __name__ == "__main__":
    main()
