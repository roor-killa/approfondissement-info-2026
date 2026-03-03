#!/bin/bash

# Bonus : Vérification de l'argument
if [ -z "$1" ]; then
    echo -e "\033[31mErreur : Tu dois fournir un nom de projet.\033[0m"
    exit 1
fi

PROJET=$1

# Création des dossiers
mkdir -p "$PROJET/src" "$PROJET/tests" "$PROJET/docs"

# Création du README
echo "# $PROJET" > "$PROJET/README.md"
echo "Date : $(date)" >> "$PROJET/README.md"
echo "Auteur : Tyron Jourdan" >> "$PROJET/README.md"

# Création du .gitignore
echo -e "__pycache__/\n*.pyc\n.env\nnode_modules/" > "$PROJET/.gitignore"

# Message de succès en vert
echo -e "\033[32mLe projet '$PROJET' a ete cree avec succes !\033[0m"