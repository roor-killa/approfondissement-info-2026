#!/bin/bash

# --- Bonus : Vérification de l'argument ---
# Si le premier argument ($1) est vide (-z), on affiche une erreur et on arrête.
if [ -z "$1" ]; then
    echo -e "\033[31mErreur : Aucun nom de projet fourni.\033[0m"
    echo "Usage: $0 <nom-du-projet>"
    exit 1
fi

# Variables
NOM_PROJET=$1
DATE_DU_JOUR=$(date +"%d/%m/%Y")
AUTEUR="Gemini" # Remplace par ton nom si tu le souhaites

mkdir -p "$NOM_PROJET/src" "$NOM_PROJET/tests" "$NOM_PROJET/docs"

# On utilise 'cat' pour écrire plusieurs lignes proprement
cat << EOF > "$NOM_PROJET/README.md"
# $NOM_PROJET

- **Date de création** : $DATE_DU_JOUR
- **Auteur** : $AUTEUR
EOF

cat << EOF > "$NOM_PROJET/.gitignore"
__pycache__/
*.pyc
.env
node_modules/
EOF

# --- 4. Message de succès coloré ---
# \033[32m active le vert, \033[0m réinitialise la couleur
echo -e "\033[32m[Succès]\033[0m La structure du projet '$NOM_PROJET' a été créée avec succès !"
