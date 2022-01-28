import csv
import re
header = "date_reference,semaine_injection,region_residence,libelle_region,departement_residence,libelle_departement,population_insee,classe_age,libelle_classe_age,type_vaccin,effectif_1_inj,effectif_termine,effectif_cumu_1_inj,effectif_cumu_termine,taux_1_inj,taux_termine,taux_cumu_1_inj,taux_cumu_termine,date,effectif_rappel,effectif_cumu_rappel,effectif_rappel_parmi_eligible,effectif_eligible_au_rappel,taux_rappel,taux_cumu_rappel,taux_cumu_rappeleli".split(",")

dico = {}
liste_dico=[]

with open('dataframe.csv',"r") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        liste_dico.append(row)

def search_by(arg,liste):
    l = []
    for i in liste:
        l.append(i[arg])
    return l

def missing_val(data):
    missing=0
    for i in data:
        if i=="":
            missing+=1
    return missing


def date_reference(date):
    date=date.replace(",","")
    date = date.replace("-","/")
    date = date.split("/")
    if len(date)==3 and len(date[1])==len(date[2])==2 and 0<int(date[1])<13:
        if 2022>=int(date[0])>=2020:
            return True
    return False

def semaine_inj(sem):
    sem = sem.split("-")
    if len(sem[0])==4 and len(sem[1])==2:
        if 2022>=int(sem[0])>=2020:
            if 64>=int(sem[1])>=0:
                return True
    return False


#for i in header:
   #print(missing_val(search_by(i,liste_dico,)))

for i in search_by("date_reference",liste_dico):
    if not date_reference(i):
        print("Voici les dates abbérantes :",i)
for i in search_by("semaine_injection", liste_dico):
    if not semaine_inj(i):
        print("Voici les semaines abbérantes :", i)





