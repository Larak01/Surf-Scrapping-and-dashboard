# 🏄‍♂️ Surf Dashboard : Lacanau Real-Time Monitoring

[cite_start]Ce projet propose un outil d'aide à la décision haut de gamme pour surveiller les conditions de surf à **Lacanau** en temps réel[cite: 5]. [cite_start]Il automatise l'ensemble du pipeline de données, de l'extraction au rendu visuel[cite: 6].

## ⚙️ Architecture du Projet

[cite_start]Le système utilise une approche hybride combinant la puissance de **Python** et de **R**[cite: 8]:

* [cite_start]**surf_scrap.py** : Moteur de scraping personnalisé ciblant *surf-report.com*[cite: 9]. [cite_start]Il extrait les données directement depuis les objets JSON JavaScript internes[cite: 10].
* [cite_start]**Projet_Surf.Rmd** : Le cœur de l'application (Flexdashboard) qui orchestre le workflow et génère l'interface[cite: 11, 12].
* **main.py** : Script de contrôle pour l'exécution des processus Python.
* [cite_start]**data_surf.csv** : Le flux de données généré servant de base aux visualisations[cite: 11].

## 📊 Pipeline de Données & Logique KPI

[cite_start]Le tableau de bord transforme les données brutes en indicateurs exploitables[cite: 14]:

1.  [cite_start]**Nettoyage des Métriques** : Les valeurs numériques sont isolées des chaînes de caractères complexes (unités comme km/h ou m)[cite: 18].
2.  [cite_start]**Algorithme "Sea Quality Grade"** : Une jauge de qualité sur **100 points** basée sur la hauteur des vagues, la vitesse et la direction du vent[cite: 21, 23].

## 🎨 Design de l'Interface

[cite_start]L'interface utilisateur a été conçue pour être immersive[cite: 26]:
* **Thème Dark Mode** : Utilisation du code couleur `#001219` (Deep Ocean)[cite: 27].
* [cite_start]**Glassmorphism** : Effets de flou sur des calques translucides pour une lisibilité optimale[cite: 28].
* [cite_start]**Visualisation Dynamique** : Intégration de **Plotly** pour explorer les prévisions sur 7 jours[cite: 29].

## 🚀 Installation et Utilisation

1.  [cite_start]Placez tous les fichiers dans le même répertoire[cite: 32].
2.  [cite_start]Ouvrez **Projet_Surf.Rmd** dans RStudio[cite: 33].
3.  [cite_start]Cliquez sur **Knit** pour générer le dashboard HTML[cite: 34].

---
[cite_start]**Auteurs :** Rim BOUAOUISS & Lara AL KHATIB [cite: 2]  
[cite_start]**Dernière mise à jour :** Janvier 2026 [cite: 4]
