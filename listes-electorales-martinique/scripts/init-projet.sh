$projectName = $args[0]
if (-not $projectName) { Write-Host "Erreur : nom manquant" -ForegroundColor Red; exit }
New-Item -ItemType Directory -Path "$projectName/src", "$projectName/tests", "$projectName/docs" -Force
New-Item -ItemType File -Path "$projectName/README.md", "$projectName/.gitignore" -Force
Write-Host "Projet '$projectName' créé !" -ForegroundColor Green
