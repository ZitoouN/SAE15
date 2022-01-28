import os           #Importer des librairies
import pandas as pd
def ComputeMean(df):  #Calcule la valeur moyenne puis l'afficher
    df_vaccin = df['vaccin']
    mean = df_vaccin.mean()
    print("valeur moyenne :", mean)
    return mean


def ComputeMedian(df):   #Calcule la valeur de la mediane puis l'afficher
    df_vaccin = df['vaccin']
    median = df_vaccin.median()
    print("valeur medianne :", median)
    return median

if __name__ == '__main__':    #Lire notre fusion csv puis faire les calcules de la médianes et de la moyenne
    df1 = pd.read_csv('dataframe.csv')
    mean1 = ComputeMean(df1)
    median1 = ComputeMedian(df1)
    df2 = pd.read_csv('dataframe.csv')
    mean2 = ComputeMean(df2)
    median2 = ComputeMedian(df2)


#Programme non terminer