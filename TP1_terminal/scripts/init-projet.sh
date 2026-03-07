#!/bin/bash

# Vérification : argument obligatoire
if [ -z "$1" ]; then
    echo "Erreur : vous devez fournir un nom de projet."
    exit 1
fi

PROJET=$1

# Création de la structure
mkdir -p "$PROJET"/{src,tests,docs}
touch "$PROJET"/README.md
touch "$PROJET"/.gitignore

# Écriture dans README.md
echo "# $PROJET" > "$PROJET"/README.md
echo "" >> "$PROJET"/README.md
echo "Date de création : $(date)" >> "$PROJET"/README.md
echo "Auteur : nniasme" >> "$PROJET"/README.md

# Écriture dans .gitignore
echo "__pycache__/" > "$PROJET"/.gitignore
echo "*.pyc" >> "$PROJET"/.gitignore
echo ".env" >> "$PROJET"/.gitignore
echo "node_modules/" >> "$PROJET"/.gitignore

# Message de succès en vert
echo -e "\033[32mProjet $PROJET créé avec succès !\033[0m"
