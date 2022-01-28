import pandas as pd
import glob
import os
import csv

files_joined = os.path.join('C:\\SAE15\\vaccination-covid\\data\\raw', "donnees-*.csv")

list_files = glob.glob(files_joined)


print("** Merging multiple csv files into a single pandas dataframe **")
dataframe = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
dataframe.to_csv("DataFrame.csv", index=False)
print(dataframe)
