📥 Script Python – Téléchargement Automatisé de Fichiers depuis KoboToolbox
🧾 Description

Ce script permet de télécharger automatiquement des fichiers (PDF, Word, images, etc.) stockés sur KoboToolbox à partir d’un fichier Excel contenant les liens. Il organise les fichiers téléchargés dans des dossiers par entreprise, et utilise une authentification HTTP basique pour accéder aux fichiers.
📁 Structure attendue du fichier Excel

Le fichier Excel doit contenir les colonnes suivantes :
Entreprise	Nom Fichier 1	URL Fichier 1	Nom Fichier 2	URL Fichier 2	...
ABC SARL	contrat.pdf	http://...	logo.png	http://...	
⚙️ Fonctionnement du script

    Charge un fichier Excel contenant les noms des entreprises et les liens de fichiers.

    Pour chaque entreprise :

        Crée un dossier dans le répertoire de travail.

        Parcourt les colonnes deux par deux pour récupérer les noms de fichiers et leurs URLs.

        Télécharge chaque fichier et l'enregistre dans le bon dossier.

    Affiche la progression via tqdm et gère les erreurs de téléchargement.

🔐 Authentification

Le script utilise l’authentification HTTP Basic (requests.auth.HTTPBasicAuth). Il te suffit de renseigner :

username = 'ton_nom_utilisateur'
password = 'ton_mot_de_passe'

📦 Dépendances

Installe les bibliothèques nécessaires avec :

pip install pandas requests tqdm openpyxl

🚀 Exécution

Place ton fichier Excel dans le dossier souhaité, puis exécute le script :

python telechargement_kobo.py

Les fichiers seront téléchargés dans un dossier nommé Téléchargements_KoboPrestataire_<DATE> dans ton répertoire de travail.
📌 Exemple de structure de dossiers créés

Téléchargements_KoboPrestataire_15042025/
│
├── ABC SARL/
│   ├── contrat.pdf
│   └── logo.png
├── XYZ Consulting/
│   └── rapport.docx

✅ Avantages

    Téléchargement par lot.

    Organisation automatique.

    Gestion des erreurs et affichage de progression.

📤 Tu peux l'utiliser pour :

    Collecter des documents justificatifs de bénéficiaires.

    Centraliser des rapports ou formulaires Kobo exportés.

    Gagner du temps en automatisant les tâches manuelles.