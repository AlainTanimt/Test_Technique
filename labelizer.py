import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

class Labeliseur:
    def __init__(self, n_clusters=3, n_components=5, scaler=None):
        """
        Initialisation du Labeliseur avec ACP et KMeans.
        :param n_clusters: Nombre de clusters pour KMeans.
        :param n_components: Nombre de composantes principales pour l'ACP.
        :param scaler: StandardScaler pour normaliser les données (par défaut StandardScaler).
        """
        self.n_clusters = n_clusters
        self.n_components = n_components
        self.scaler = scaler if scaler else StandardScaler()
        self.kmeans_model = KMeans(n_clusters=n_clusters)
        self.pca_model = PCA(n_components=n_components)

    @staticmethod
    def filtrer_dataframe(df):
        """
        Filtre les données inutiles d'un DataFrame.
        :param df: DataFrame d'entrée.
        :return: DataFrame filtré.
        """
        # Supprimer les lignes avec 'layout' égal à 'v'
        df = df[df['layout'] != 'v']

        # Supprimer les textes avec des occurrences élevées
        occurence_texte = df['text'].value_counts()
        df = df[df['text'].isin(occurence_texte[occurence_texte < 10].index)]

        # Supprimer les lignes où le texte est un nombre
        indices_a_supprimer = pd.to_numeric(df['text'], errors='coerce', downcast='integer').notna()
        df = df[~indices_a_supprimer]

        return df

    def appliquer_k_means(self, df, features):
        """
        Applique une ACP suivie de KMeans sur les données filtrées.
        :param df: DataFrame contenant les données.
        :param features: Liste des colonnes à utiliser pour le clustering.
        :return: DataFrame avec labels mis à jour.
        """
        # Normaliser les données
        df_scaled = self.scaler.fit_transform(df[features])

        # Réaliser l'ACP
        principal_components = self.pca_model.fit_transform(df_scaled)
        pca_columns = [f'PC{i + 1}' for i in range(self.n_components)]
        df_pca = pd.DataFrame(principal_components, columns=pca_columns)

        # Appliquer KMeans sur les composantes principales
        df['label'] = self.kmeans_model.fit_predict(df_pca)

        # Analyser les centroides
        centroid_df = pd.DataFrame(self.kmeans_model.cluster_centers_, columns=pca_columns)
        variances = centroid_df.var()
        most_separating_component = variances.idxmax()
        centroid_values = centroid_df[most_separating_component].values

        # Trier les indices des centroides
        sorted_indices = np.argsort(centroid_values)

        # Assigner les labels lisibles
        label_mapping = {
            sorted_indices[2]: 'Paragraphe',
            sorted_indices[0]: 'Inutile',
            sorted_indices[1]: 'Titre',
        }
        df['label'] = df['label'].map(label_mapping)

        return df

    def labeliser(self, df, features):
        """
        Exécute le processus complet de filtrage, ACP et labélisation.
        :param df: DataFrame d'entrée.
        :param features: Liste des colonnes à utiliser pour le clustering.
        :return: DataFrame final avec les labels.
        """
        df = df.reset_index()
        df_filtre = self.filtrer_dataframe(df.copy())
        df_filtre = self.appliquer_k_means(df_filtre, features)
        df.to_csv("testeLabeliseur/df.csv", index=False)
        df_filtre.to_csv("testeLabeliseur/df_filtre.csv", index=False)
        df = pd.merge(df, df_filtre[['index','label']], how='left')
        df['label'] = df['label'].fillna('Inutile')
        return df
