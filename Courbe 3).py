#On importe les librairies nécessaires

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('dataframe.csv')

specified = df.loc[df['libelle_departement'] == 'Haut-Rhin']
x = specified['libelle_departement']
y = specified['effectif_rappel']

plt.xlabel('Haut-Rhin', fontsize=10)
plt.ylabel('Injection de rappel', fontsize=10)
plt.scatter(x, y)

plt.show()