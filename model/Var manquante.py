import csv#Importer des librairies
import re
header = "date_reference,semaine_injection,region_residence,libelle_region,departement_residence,libelle_departement,population_insee,classe_age,libelle_classe_age,type_vaccin,effectif_1_inj,effectif_termine,effectif_cumu_1_inj,effectif_cumu_termine,taux_1_inj,taux_termine,taux_cumu_1_inj,taux_cumu_termine,date,effectif_rappel,effectif_cumu_rappel,effectif_rappel_parmi_eligible,effectif_eligible_au_rappel,taux_rappel,taux_cumu_rappel,taux_cumu_rappeleli".split(",")#Toute les variables de notre sujet dans une chaine de caractère avec un split pour prendre en compte la virgule.

dico = {}   #Dictionnaire vide
liste_dico=[]    #liste vide

with open('dataframe.csv',"r") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")   # Permet d'ouvrir notre fusion tout en prenant compte de notre ;
    for row in reader:
        liste_dico.append(row)    #ajouter notre fusion dans notre liste vide

def search_by(arg,liste):
    l = []
    for i in liste:
        l.append(i[arg])
    return l

def missing_val(data):   #Permet de trouver les valeurs manquantes dans l'ordre de notre chaine de caratctère (soit header)
    missing=0
    for i in data:
        if i=="":
            missing+=1
    return missing


def date_reference(date):   #Permet de trouver les valeurs abbérantes des dates
    date = date.replace(",","")
    date = date.replace("-","/")
    date = date.split("/")
    if len(date) == 3 and len(date[1])==len(date[2])==2 and 0<int(date[1])<13:
        if 2022>=int(date[0]) >= 2020:
            return True
    return False

def semaine_inj(sem):    #Permet de trouver les valeurs abbérantes de semaines d'injection
    sem = sem.split("-")
    if len(sem[0]) == 4 and len(sem[1]) == 2:
        if 2022>= int(sem[0]) >= 2020:
            if 64>=int(sem[1]) >= 0:
                return True
    return False


def region_residence(reg):         #Permet de trouver les régions abbérantes
    if int(reg) < 1 or int(reg) > 101:
       return False
    return True

def libelle_region(name_reg):          #Permet de trouver les nom régions abbérantes
    region = ["Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne", "Centre-Val de Loire", "Corse",
              "Grand Est", "Hauts-de-France", "Ile-de-France", "Normandie", "Nouvelle-Aquitaine", "Occitanie",
              "Pays de la Loire", "Provence-Alpes-Côte d’Azur", "Guadeloupe", "Martinique", "Guyane", "La Réunion",
              "Mayotte"]
    if region != name_reg:
        return True
    return False

def classe_age(age):        #Permet de trouver les ages abbérantes par rapport au vaccin
    age = age.split("-")
    if len(age[0]) == 2 and len(age[1]) == 2:
        if 100>=int(age[0])>=0:
            if 100>=int(age[1])>=0:
                if int(age[0]) == 0 and int(age[1]) == 11:
                    if int(age[0]) == 75:
                        return True
                    return False
                return True
    return False


for i in header:    #Permet d'afficher toute nos valeurs manquantes et nos valeurs abbérantes
   print(missing_val(search_by(i,liste_dico,)))

for i in search_by("date_reference",liste_dico):
    if not date_reference(i):
        print("Voici les dates abbérantes :",i)
else:
    print("Il y'a pas de valeurs abbérentes")
for i in search_by("semaine_injection", liste_dico):
    if not semaine_inj(i):
        print("Voici les semaines abbérantes :", i)
else:
    print("Il y'a pas de valeurs abbérentes")
for i in search_by("region_residence", liste_dico):
    if not region_residence(i):
        print("Voici les régions abbérentes:", i)
else:
    print("Il y'a pas de valeurs abbérentes")
for i in search_by("libelle_region", liste_dico):
    if not libelle_region(i):
        print("Voici les régions abbérentes:", i)
else:
    print("Il y'a pas de valeurs abbérentes")
for i in search_by("classe_age", liste_dico):
    if not classe_age(i):
      print("Voici les classes d'ages abbérentes:", i)
else:
    print("Il y'a pas de classes d'ages abbérentes")