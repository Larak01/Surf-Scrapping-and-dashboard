# 🏄‍♂️ Surf Dashboard : Lacanau Real-Time Monitoring

Ce projet propose un outil d'aide à la décision haut de gamme pour surveiller les conditions de surf à **Lacanau** en temps réel. Il automatise l'ensemble du pipeline de données, de l'extraction (scraping) à la visualisation interactive.

---

## ⚙️ Architecture du Projet

Le système utilise une approche hybride combinant la puissance de **Python** et de **R** :

* **surf_scrap.py** : Moteur de scraping personnalisé ciblant surf-report.com. Il extrait les données directement depuis les objets JSON JavaScript internes.
* **Projet_Surf.Rmd** : Le cœur de l'application (Flexdashboard) qui orchestre le workflow, appelle les scripts Python et génère l'interface.
* **main.py** : Script de contrôle principal pour l'exécution des processus Python.
* **data_surf.csv** : Le flux de données généré après traitement, servant de base aux visualisations.

---

## 📊 Pipeline de Données & Logique KPI

Le tableau de bord transforme les données brutes en indicateurs exploitables :

### 1. Nettoyage des Métriques
Les valeurs numériques sont isolées des chaînes de caractères complexes (unités comme km/h ou m) via une logique de parsing automatique.

### 2. Algorithme "Sea Quality Grade"
Une jauge de qualité de la mer est calculée sur une échelle de **100 points** selon les critères suivants :
* **+40** si la hauteur de vagues $\ge 1.0m$.
* **+30** si la vitesse du vent $\le 50km/h$.
* **+30** si la direction du vent contient "North".

---

## 🎨 Design de l'Interface

L'interface utilisateur a été conçue pour être immersive et moderne :

* **Thème Dark Mode** : Utilisation du code couleur `#001219` (Deep Ocean) pour le confort visuel.
* **Glassmorphism** : Effets de flou (`backdrop-blur`) sur des calques translucides pour une lisibilité optimale.
* **Visualisation Dynamique** : Intégration de **Plotly** pour explorer l'historique et les prévisions sur 7 jours.

---

## 🚀 Installation et Utilisation

Pour lancer le dashboard sur votre machine :

1.  Clonez le dépôt et assurez-vous que tous les fichiers (`.Rmd`, `.py`, `.csv`) se trouvent dans le même dossier.
2.  Ouvrez **Projet_Surf.Rmd** dans RStudio.
3.  Exécutez la commande **Knit** pour générer le dashboard interactif au format HTML.

---

**Développeurs :** Rim BOUAOUISS & Lara AL KHATIB  
**Date :** Janvier 2026
