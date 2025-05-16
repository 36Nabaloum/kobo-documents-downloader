import os
import pandas as pd
import requests
from tqdm import tqdm  # Pour afficher la progression des téléchargements
from requests.auth import HTTPBasicAuth  # Importer l'authentification de base

# 📌 Charger le fichier Excel
fichier_excel = "C:\\Users\\User\\Downloads\\Dbase.xlsx"  # 🔄 Remplace par le chemin de ton fichier Excel
df = pd.read_excel(fichier_excel, sheet_name="Feuil1")  # 🔄 Remplace "Feuil5" par le bon nom de feuille

# 📂 Définir le dossier principal pour les téléchargements
chemin_base = os.path.join(os.getcwd(), "Téléchargements_KoboPrestataire_15042025")

# 📌 Vérifier et créer le dossier principal si nécessaire
if not os.path.exists(chemin_base):
    os.makedirs(chemin_base)

# 🏢 Ajouter votre nom d'utilisateur et mot de passe
username = 'username'  # Remplacez par votre vrai nom d'utilisateur
password = 'mots de passe'  # Remplacez par votre vrai mot de passe

# 🏢 Boucle pour traiter chaque entreprise
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Téléchargements en cours"):
    entreprise = str(row.iloc[0]).strip()  # 🏢 Nom de l'entreprise (1ère colonne)

    if entreprise:  # Vérifier si le nom de l'entreprise est valide
        dossier_entreprise = os.path.join(chemin_base, entreprise)

        # 📂 Créer le dossier de l'entreprise s'il n'existe pas
        if not os.path.exists(dossier_entreprise):
            os.makedirs(dossier_entreprise)

        # 🔄 Boucle sur les paires (Nom du fichier - URL)
        for j in range(1, len(row) - 1, 2):  # Parcourt les colonnes 2, 4, 6, etc.
            nom_fichier = str(row.iloc[j]).strip()
            url = str(row.iloc[j + 1]).strip()

            if nom_fichier and url.startswith("http"):  # Vérifie que l'URL est valide
                chemin_fichier = os.path.join(dossier_entreprise, nom_fichier)

                try:
                    # 📥 Télécharger le fichier avec authentification
                    response = requests.get(url, auth=HTTPBasicAuth(username, password), stream=True)
                    response.raise_for_status()  # Vérifier les erreurs HTTP

                    # 💾 Sauvegarder le fichier téléchargé
                    with open(chemin_fichier, "wb") as fichier:
                        for chunk in response.iter_content(chunk_size=8192):
                            fichier.write(chunk)

                except Exception as e:
                    print(f"❌ Erreur lors du téléchargement de {nom_fichier} : {e}")

print("✅ Téléchargement terminé avec succès !")