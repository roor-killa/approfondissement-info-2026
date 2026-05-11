# Projet Webhook n8n vers Telegram

## Objectif du projet

Le but du projet est de connecter un site web à un workflow n8n afin d’envoyer automatiquement des messages sur Telegram.

Lorsqu’un utilisateur clique sur un bouton du site web, une requête HTTP POST est envoyée vers un Webhook n8n.  
Le workflow récupère ensuite les données et les transmet automatiquement à un bot Telegram.

---

## Fonctionnement du projet

### 1. Site web

Le site utilise JavaScript et la fonction `fetch()` pour envoyer des données vers un Webhook n8n.

Exemple :

```javascript
fetch(webhookUrl, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(dataToSend)
})