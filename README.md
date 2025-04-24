# VeilleTechno

Prérequis
✅Visual Studio Code installé

✅Extension Python installée dans VS Code

✅Python 3.10+ installé sur votre système : https://www.python.org/downloads/

---

🐍 Mise en place de l'environnement Python:
1. Création de l’environnement de travail Python
    
    ```bash
    python -m venv venv
    ```
    
2. Activation de l’environnement de travail virtuel Python pour le dossier racine
    
    ```bash
    .\venv\Scripts\activate
    ```
    
3. Installation des dépendances
    
    ```bash
    pip install -r api/requirements.txt
    ```
---

 
🧠 Entraînement du modèle de classification
1. Exécuter le script pour entraîner le modèle
    
    ```bash
    python model/train_model.py
    ```
---

    
🚀 Démarrage de l’API FastAPI
1. Création de l’environnement de travail Python
    
    ```bash
    pip install fastapi[all]
    ```
    
2. Activation de l’environnement de travail Python pour le dossier racine
    
    ```bash
    uvicorn api.app:app --reload
    ```
      
   Puis visite pour accéder à l'interface Swagger : 📍 http://127.0.0.1:8000/docs
---


❌ Quitter l’environnement virtuel

    ```bash
    deactivate
    ```
