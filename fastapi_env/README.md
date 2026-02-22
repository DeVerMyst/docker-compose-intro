# Guide de configuration et déploiement FastAPI

## 1. Configuration des variables d'environnement

La gestion des paramètres et des secrets s'effectue via un fichier local pour isoler la configuration du code source.

Créer un fichier nommé `.env` à la racine du projet :

```plaintext
PORT=9000
MA_VARIABLE=valeur
AUTRE_VARIABLE=autre_valeur

```

## 2. Validation en environnement de développement

Avant la conteneurisation, vérifiez le bon fonctionnement de l'API. L'utilisation du mode `reload` permet de redémarrer automatiquement le serveur à chaque modification du code, tandis que le niveau `debug` affiche les journaux détaillés.

Exécuter la commande suivante :

```bash
uvicorn monapi:app --reload --log-level debug

```

## 3. Orchestration avec Docker Compose

Le fichier `docker-compose.yml` automatise la construction de l'image (build) et la gestion de l'exécution du conteneur (run) en une seule étape.

Lancer l'infrastructure :

```bash
docker-compose up

```

## 4. Accès à l'application et à la documentation

Le service est configuré pour rediriger le trafic réseau vers le port 9000. Une fois le conteneur opérationnel, l'API et sa documentation interactive sont disponibles aux adresses suivantes :

* **Interface API :** [http://localhost:9000/](https://www.google.com/search?q=http://localhost:9000/)
* **Documentation Swagger UI :** [http://localhost:9000/docs](https://www.google.com/search?q=http://localhost:9000/docs)

