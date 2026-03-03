#!/bin/bash

# Vérifie qu'un nom de projet est fourni
if [ -z "$1" ]; then
  echo "Usage: ./init-projet.sh nom-du-projet"
  exit 1
fi

PROJECT_NAME="$1"

# Vérifie si le dossier existe déjà
if [ -d "$PROJECT_NAME" ]; then
  echo "Le dossier '$PROJECT_NAME' existe déjà."
  exit 1
fi

# Création de la structure
mkdir -p "$PROJECT_NAME"/src
mkdir -p "$PROJECT_NAME"/tests
mkdir -p "$PROJECT_NAME"/docs

# Création du README.md
cat > "$PROJECT_NAME"/README.md <<EOF
# $PROJECT_NAME

Date de création : $(date)

Auteur : Matthias
EOF

# Création du .gitignore
cat > "$PROJECT_NAME"/.gitignore <<EOF
__pycache__/
*.pyc
.env
node_modules/
EOF

echo "Projet '$PROJECT_NAME' créé avec succès !"
