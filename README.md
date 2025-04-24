# VeilleTechno

Pour l'utilisation dans Visual Studio Code, installer l'extension pour Python.

Étapes pour exécuter le modèle:
1. Création de l’environnement de travail Python
    
    ```bash
    python -m venv venv
    ```
    
2. Activation de l’environnement de travail Python pour le dossier racine
    
    ```bash
    .\venv\Scripts\activate
    ```
    
3. Installation des dépendances
    
    ```bash
    pip install -r api/requirements.txt
    ```
    
4. Exécuter le script pour entraîner le modèle
    
    ```bash
    python model/train_model.py
    ```
    
Étapes pour le lancement de l'API:
1. Création de l’environnement de travail Python
    
    ```bash
    pip install fastapi[all]
    ```
    
2. Activation de l’environnement de travail Python pour le dossier racine
    
    ```bash
    uvicorn api.app:app --reload
    ```
      
   Puis visite pour accéder à l'interface Swagger : 📍 http://127.0.0.1:8000/docs

3. Sortir de l’environnement de travail

      ```bash
    deactivate
    ```
