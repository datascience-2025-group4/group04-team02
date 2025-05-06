import pandas as pd

df = pd.read_csv("data/ab_ag.tsv", sep="\t")
print(df.head())