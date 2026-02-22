#### Les commandes importantes:

`docker-compose up --build` : build and run
`docker-compose up --build -d` : build and run en détaché
`docker-compose logs -f` : pour voir le log de votre conteneur détaché
`docker-compose down` : arrêter les conteneurs
`docker-compose down --rmi all` : arrêter les conteneurs et les supprimer

**Pour l'exemple le `.env` est donné mais ne faites pas cela dans vos projets**

## Transfert de Variables d'Environnement avec Docker Compose

Ce dépôt contient plusieurs exemples illustrant comment transférer des variables d'environnement vers différents types de conteneurs en utilisant Docker Compose.

### Exemples

1.  **Variables d'Environnement vers une Base de Données (DB)**
    * Cet exemple montre comment configurer une base de données (par exemple, PostgreSQL ou MySQL) avec des variables d'environnement pour des informations telles que le port, le mot de passe admin et le nom de la base de données.
    * Le fichier `.env` contiendra les informations de connexions.
    * Le `docker-compose.yml` utilisera `env_file` et `environment` afin de paramétrer le conteneur de base de données.

2.  **Variables d'Environnement vers un Stack DB, Apache, phpMyAdmin**
    * Cet exemple montre comment configurer une pile complète (base de données, serveur web Apache, phpMyAdmin) en utilisant des variables d'environnement.
    * Les variables seront utilisées pour configurer les informations de connexion à la base de données, les paramètres de phpMyAdmin et les options du serveur web.
    * Le fichier `.env` contiendra les informations de connexions.
    * Le `docker-compose.yml` utilisera `env_file` et `environment` afin de paramétrer chacun des conteneurs.

3.  **Variables d'Environnement vers FastAPI**
    * Cet exemple démontre comment passer des variables d'environnement à une application FastAPI exécutée dans un conteneur Docker.
    * Les variables seront utilisées pour configurer l'URL et le port de l'API.
    * Le fichier `.env` contiendra les informations de connexions.
    * Le `docker-compose.yml` utilisera `env_file` et `environment` afin de paramétrer le conteneur de l'api.
    * Le `Dockerfile` contiendra les informations minimales afin de construire l'image.

### Utilisation

1.  **Cloner le dépôt :**

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
```

2.  **Construire et exécuter les conteneurs :**

```bash
docker-compose up --build
```

* `--build` : Construit les images et démarre les conteneurs.

3.  **Exécuter en mode détaché (arrière-plan) :**

```bash
docker-compose up --build -d
```

* `-d` : Démarre les conteneurs en mode détaché.

4.  **Afficher les logs des conteneurs :**

```bash
docker-compose logs -f
```

* `-f` : Suit les logs en temps réel.

5.  **Arrêter les conteneurs :**

```bash
docker-compose down
```

6.  **Arrêter et supprimer les conteneurs et les images :**

```bash
docker-compose down --rmi all
```

* `--rmi all` : Supprime toutes les images créées par Docker Compose.

### Fichier `.env`

Chaque exemple utilise un fichier `.env` pour stocker les variables d'environnement. Assurez-vous de créer ce fichier dans le même répertoire que votre fichier `docker-compose.yml` et de le remplir avec les valeurs appropriées.

### Structure du dépôt

```
├── db/
│   ├── docker-compose.yml
│   └── .env
├── fastapi_env/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── pyproject.toml    
│   ├── uv.lock
│   ├── README.md
│   ├── monapi.py
│   ├── .dockerignore
│   └── .env
├── stack/
│   ├── docker-compose.yml
│   └── .env
├── streamlit_env/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── pyproject.toml    
│   ├── uv.lock
│   ├── README.md
│   ├── app.py
│   ├── .dockerignore    
│   └── .env    
├── README.md
└── .gitignore
```

## Notes importantes

* N'incluez jamais d'informations sensibles (mots de passe, clés API) directement dans votre code source ou dans les images Docker.
* Utilisez `.gitignore` pour exclure le fichier `.env` du versionnement.
* Utilisez `.dockerignore` pour exclure les fichiers lourd de l'image (`.venv` etc...).
* Adaptez les exemples à vos besoins spécifiques en modifiant les fichiers `.env` et `docker-compose.yml`.
* Utilisez l'option `--no-cache` lors de la construction pour forcer la mise à jour des images. Exemple : `docker-compose build --no-cache`.

