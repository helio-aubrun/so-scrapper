# SO Scraper

**SO Scraper** est un outil Python permettant de collecter et d’analyser automatiquement les questions récentes de Stack Overflow. Il propose deux modes :

- **Séquentiel** (`scrape_stackoverflow`) : collecte page par page avec une pause configurable.
- **Parallèle** (`scrape_stackoverflow_threaded`) : utilise un pool de threads (`ThreadPoolExecutor`) pour accélérer les requêtes.

---

## 📦 Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/<votre-utilisateur>/so-scrapper.git
   cd so-scrapper
   ```

2. **Créer et activer l’environnement** :
   ```bash
   # Avec venv
   python -m venv venv
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate      # Windows

   # Ou avec Conda
   conda create -n SoScraper python=3.8
   conda activate SoScraper
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

- **MongoDB** : lancer le service localement (`mongod`).
- **Variables d’environnement** : aucune clé API requise pour la version actuelle.

---

## 🚀 Utilisation

Le point d’entrée est le fichier `scraper.py`.

### 1. Version séquentielle

```bash
python scraper.py --mode sequential --pages 5 --delay 1
```

- `--mode sequential` : exécute `scrape_stackoverflow`
- `--pages N` : nombre de pages à scraper (par défaut : 1)
- `--delay S` : pause en secondes entre chaque page (par défaut : 1)

### 2. Version parallèle

```bash
python scraper.py --mode threaded --pages 10 --workers 5 --delay 0.5
```

- `--mode threaded` : exécute `scrape_stackoverflow_threaded`
- `--workers W` : nombre de threads simultanés (par défaut : 5)
- `--delay S` : pause après chaque parsing de page (par défaut : 1)

> **Exemple** : scrap de 10 pages avec 5 threads et 0.5s de pause :
> ```bash
> python scraper.py --mode threaded --pages 10 --workers 5 --delay 0.5
> ```

---

## 📂 Structure du projet

```text
so-scrapper/
├─ scraper.py             # code principal (séquentiel et threaded)
├─ bdd.py                 # insertion dans MongoDB
├─ analyse_so_scraper.ipynb # notebook d’analyse des données
├─ requirements.txt       # dépendances Python
├─ tests/                 # tests unitaires pytest
│  ├─ test_scraper.py
│  └─ test_bdd.py
└─ README.md              # documentation (ce fichier)
```

---

## 🧪 Tests unitaires

Lancer tous les tests :
```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## 📊 Analyse des données

Le notebook `analyse_so_scraper.ipynb` contient :
- Connexion à MongoDB
- Analyse des **tags** (Top 15)
- Analyse **NLP** des résumés (Top mots-clés)

---

## 📜 Licence & Crédits

MIT License. Développé par Ayoub Abderrahmane pour le projet SO Scraper.
