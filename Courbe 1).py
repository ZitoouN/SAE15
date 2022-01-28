#On importe les librairies nécessaires

import pandas as pd
import csv
import matplotlib.pyplot as plt

x = []    #listes vides
y = []

with open('dataframe.csv', "r") as csvfile:    #Permet d'ouvrir notre fusion csv tout en prenant compte du ;
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(str(row[5]))      #Ajouter les variables que nous voulons dans les listes vides
        y.append(str(row[18]))

df = pd.read_csv('dataframe.csv')    #Lire notre fusion


l=[]
for i in range(len(x)):    #Pour la variables région nous allons le filtrer pour prendre que la haut-rhin
    if x[i]=="Haut-Rhin":
        l.append(y[i])

y=[i for i in range(len(l))]

plt.xlabel('Effectif dans le Haut-Rhin', fontsize=10)   #Evolution de l'effectif dans le haut-rhin
plt.ylabel('Dates', fontsize=10)          #dates des vaccinés
plt.title('Evolution de vaccinés dans le Haut-Rhin pour ceux avec un schéma à un rappel', fontsize=30)    #Titre pour le graphique
plt.plot(y,l)

plt.show()