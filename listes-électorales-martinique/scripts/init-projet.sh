#!/bin/bash

# Vérification argument
if [ -z "$1" ]; then
    echo "Erreur : veuillez fournir un nom de projet."
    exit 1
fi

NOM_PROJET=$1

# Création structure
mkdir -p "$NOM_PROJET"/{src,tests,docs}
touch "$NOM_PROJET"/README.md
touch "$NOM_PROJET"/.gitignore

# README
echo "# $NOM_PROJET" > "$NOM_PROJET"/README.md
echo "Date de création : $(date)" >> "$NOM_PROJET"/README.md
echo "Auteur : TON_NOM" >> "$NOM_PROJET"/README.md

# .gitignore
echo "__pycache__/" > "$NOM_PROJET"/.gitignore
echo "*.pyc" >> "$NOM_PROJET"/.gitignore
echo ".env" >> "$NOM_PROJET"/.gitignore
echo "node_modules/" >> "$NOM_PROJET"/.gitignore

# Message succès
echo -e "\033[32mProjet $NOM_PROJET créé avec succès !\033[0m"
