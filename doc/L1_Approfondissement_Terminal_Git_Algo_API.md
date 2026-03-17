# L1 Approfondissement Informatique
## Modules : Terminal · Git Avancé · Algorithmique · APIs REST
> Université des Antilles — Département Informatique  
> Ratio : 30% CM / 70% TP — Contexte Caribbean-first 🌴

---

# MODULE 1 — Le Terminal & la ligne de commande

## CM 1 — Pourquoi le terminal est ton meilleur ami

### Objectifs pédagogiques
- Comprendre ce qu'est un shell et pourquoi les développeurs l'utilisent
- Naviguer dans un système de fichiers en ligne de commande
- Manipuler fichiers et dossiers sans interface graphique
- Automatiser des tâches répétitives avec des scripts

---

### 1.1 Le Shell, c'est quoi ?

Un **shell** est un interpréteur de commandes : tu écris une instruction en texte, le système l'exécute.

Il en existe plusieurs :
| Shell | Système | Description |
|-------|---------|-------------|
| `bash` | Linux / macOS | Le plus répandu |
| `zsh` | macOS (depuis 2019) | Plus moderne, très populaire |
| `fish` | Tous | Convivial, autocomplétion avancée |
| `PowerShell` | Windows | Shell Microsoft |

> 💡 **Pourquoi pas juste cliquer ?** Parce qu'on ne peut pas automatiser des clics. Le terminal permet d'écrire des scripts qui font en 1 seconde ce qu'on mettrait 10 minutes à faire à la souris.

---

### 1.2 Anatomie d'une commande

```
commande  [options]  [arguments]
   ls        -la      /home/etudiant
```

- **commande** : l'outil qu'on appelle
- **options** : modifient le comportement (commencent par `-` ou `--`)
- **arguments** : ce sur quoi la commande agit

---

### 1.3 Les commandes fondamentales

#### Navigation
```bash
pwd              # Print Working Directory — où suis-je ?
ls               # lister les fichiers
ls -la           # liste détaillée avec fichiers cachés
cd /chemin       # changer de dossier
cd ..            # remonter d'un niveau
cd ~             # aller dans le dossier personnel
```

#### Manipulation de fichiers
```bash
touch fichier.txt          # créer un fichier vide
mkdir mon-projet           # créer un dossier
mkdir -p a/b/c             # créer des dossiers imbriqués
cp source destination      # copier
mv source destination      # déplacer / renommer
rm fichier.txt             # supprimer un fichier
rm -rf dossier/            # supprimer un dossier (ATTENTION ⚠️)
cat fichier.txt            # afficher le contenu
less fichier.txt           # afficher page par page
```

#### Recherche et filtrage
```bash
grep "mot" fichier.txt          # chercher un mot dans un fichier
grep -r "mot" ./dossier/        # cherche récursivement
find . -name "*.py"             # trouver tous les fichiers .py
```

#### Les pipes `|` — l'outil le plus puissant
Le pipe envoie la sortie d'une commande vers l'entrée d'une autre.

```bash
ls -la | grep ".py"             # lister uniquement les .py
cat data.txt | sort | uniq      # trier et dédupliquer
cat log.txt | grep "ERROR" | wc -l   # compter les erreurs
```

---

### 1.4 Les redirections

```bash
echo "Bonjour" > fichier.txt    # écrit dans le fichier (écrase)
echo "Suite" >> fichier.txt     # ajoute à la fin du fichier
commande 2> erreurs.log         # redirige les erreurs
commande > out.txt 2>&1         # redirige tout (sortie + erreurs)
```

---

### 1.5 Variables et scripts bash

```bash
#!/bin/bash

# Déclarer une variable
NOM="Martinique"
echo "Bonjour depuis $NOM"

# Variable spéciale : $1 = premier argument du script
echo "Tu as passé : $1"

# Condition
if [ "$1" == "bonjour" ]; then
    echo "Bonjour à toi aussi !"
else
    echo "Je ne comprends pas ce mot."
fi

# Boucle
for i in 1 2 3 4 5; do
    echo "Itération $i"
done
```

Rendre un script exécutable :
```bash
chmod +x mon_script.sh
./mon_script.sh
```

---

### 1.6 Commandes utiles du développeur

```bash
which python3          # où est installé Python ?
echo $PATH             # les dossiers scannés pour trouver les commandes
history                # historique des commandes
!!                     # rejouer la dernière commande
ctrl + r               # rechercher dans l'historique
man ls                 # manuel d'une commande
```

---

## TP 1 — Le Terminal en pratique

**Durée : 2h | Niveau : débutant → intermédiaire**

### Contexte
Tu travailles pour une association qui recense les **listes electorales de Martinique**. Tu dois organiser leurs fichiers de données et créer un script d'initialisation de projet.

---

### Partie A — Navigation et manipulation (30 min)

1. Ouvre un terminal et affiche ton répertoire courant.

2. Crée l'arborescence suivante **en une seule commande** `mkdir -p` :
```
listes-electorales-martinique/
├── data/
│   ├── nord/
│   ├── sud/
│   └── centre/
├── scripts/
└── rapports/
```

3. Dans `data/nord/`, crée les fichiers suivants :
   - `grand-riviere.txt`
   - `trinite.txt`
   - `marigot.txt`

4. Ajoute dans chaque fichier le texte `"Villes du Nord de la Martinique"` via `echo` et `>`.

5. Affiche le contenu de tous les fichiers du dossier `nord/` en une seule commande utilisant un **pipe**.

---

### Partie B — Recherche et filtrage (30 min)

1. Crée un fichier `data/listes.csv` avec ce contenu à partir du document liste_candidat_municipales_2026.pdf :
```
commune,liste,ordre, nom, prenom
Fort-de-France, COMBAT OUVRIER, 1, JEAN-MARIE, Gabriel
Fort-de-France, COMBAT OUVRIER, 1, MARTHE-DITE-SURELLY, Marie-Hellen
Fort-de-France, DEMOCRATES ET PROGRESSISTES, 2, LAGUERRE, Didier
Fort-de-France, DEMOCRATES ET PROGRESSISTES, 2, CHANDEY, Annie
```

2. Utilise `grep` pour afficher uniquement les listes de type `Fort-de-France`.

3. Compte combien de listes sont sur `Fort-de-France`.

4. Affiche les plages triées alphabétiquement par nom (utilise `sort`).

5. Extrais uniquement la colonne `commune` (utilise `cut -d',' -f2`).

---

### Partie C — Script d'initialisation (60 min)

Crée un script `scripts/init-projet.sh` qui :

1. Prend en argument le **nom du projet** (`$1`)
2. Crée la structure de dossiers suivante :
```
{nom-projet}/
├── src/
├── tests/
├── docs/
├── README.md
└── .gitignore
```
3. Écrit dans `README.md` :
   - Le nom du projet
   - La date de création (utilise `date`)
   - Ton nom d'auteur
4. Écrit dans `.gitignore` les entrées classiques : `__pycache__/`, `*.pyc`, `.env`, `node_modules/`
5. Affiche un message de succès coloré (recherche `echo -e "\033[32m..."`)

**Bonus :** Ajoute une vérification — si aucun argument n'est passé, le script affiche un message d'erreur et s'arrête (`exit 1`).

---

### Rendu
- Fichier `init-projet.sh` fonctionnel
- Capture d'écran du terminal montrant l'exécution du script
- Réponses aux questions A et B dans un fichier `reponses.txt`

---
---

