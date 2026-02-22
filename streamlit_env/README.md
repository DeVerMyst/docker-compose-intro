# Guide de configuration et déploiement Streamlit

## 1. Configuration des variables d'environnement

La gestion des paramètres s'effectue via un fichier local pour isoler la configuration du code source.

Créer un fichier nommé `.env` à la racine du projet :

```plaintext
PORT=9000
MA_VARIABLE=valeur
AUTRE_VARIABLE=autre_valeur

```

## 2. Validation en environnement de développement

Avant la conteneurisation, vérifiez le bon fonctionnement de l'application. L'option `runOnSave` permet de répercuter vos modifications en temps réel dans l'interface.

Exécuter la commande suivante :

```bash
streamlit run app.py --server.runOnSave true

```

## 3. Orchestration avec Docker Compose

Le fichier `docker-compose.yml` permet de builder l'image et de gérer l'exécution du conteneur de manière automatisée.

Lancer l'infrastructure :

```bash
docker-compose up

```

## 4. Accès à l'application

Le service est configuré pour rediriger le flux réseau vers le port défini dans votre configuration. Une fois le conteneur actif, l'interface est accessible à l'adresse suivante :

**URL :** [http://localhost:9000/](https://www.google.com/search?q=http://localhost:9000/)
