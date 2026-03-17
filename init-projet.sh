#!/bin/bash

if [ -z "$1" ]; then
  echo -e "\033[31m[ERREUR] Aucun nom de projet fourni.\033[0m"
  echo "Usage : ./init-projet.sh <nom-du-projet>"
  exit 1
fi

NOM_PROJET="$1"
DATE_CREATION=$(date "+%d/%m/%Y à %H:%M")
AUTEUR="GOUYER Samuel"

mkdir -p "$NOM_PROJET"/{src,tests,docs}

cat > "$NOM_PROJET/README.md" << EOF
# $NOM_PROJET

- Date de création : $DATE_CREATION
- Auteur : $AUTEUR
EOF

cat > "$NOM_PROJET/.gitignore" << EOF
__pycache__/
*.pyc
.env
node_modules/
EOF

echo -e "\033[32mProjet '$NOM_PROJET' créé avec succès !\033[0m"
