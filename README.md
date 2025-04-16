# VeilleTechno

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
    
4. Exécuter le script
    
    ```bash
    python model/train_model.py
    ```
    
5. Sortir de l’environnement de travail

      ```bash
    deactivate
    ```

Lancement de l'API:

      uvicorn api.app:app --reload

Puis visite : 📍 http://127.0.0.1:8000/docs
